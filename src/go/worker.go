package main

import (
    "context"
    "log"
    "os"
    "strconv"
    "time"

    "github.com/go-redis/redis/v8"
)

var redisClient = redis.NewClient(&redis.Options{
  Addr: os.Getenv("REDIS_HOST") + ":6379",
})

func reconcile(ctx context.Context) {
  iter := redisClient.HScan(ctx, "write_hash", 0, "*", 0).Iterator()
  for iter.Next(ctx) {
    cellToWrite := iter.Val()
    iter.Next(ctx)
    if err := iter.Err(); err != nil {
	    panic(err)
    }

    txf := func(tx *redis.Tx) error {
      valueToWrite, err := tx.HGet(ctx, "write_hash", cellToWrite).Result()
      if err != nil && err != redis.Nil {
        return err
      }
      log.Printf("Read value from queue: %v\n", cellToWrite)
      log.Printf("Value to write is: %v\n", valueToWrite)
      valueInCache, err := tx.Get(ctx, cellToWrite).Result()
      if valueInCache == valueToWrite {
        _, err = tx.TxPipelined(ctx, func(pipe redis.Pipeliner) error {
          pipe.HDel(ctx, "write_hash", cellToWrite)
          log.Printf("Deleting: %v\n", cellToWrite)
          return nil
        })
        return err
      }
      return nil
    }

    err := redisClient.Watch(ctx, txf, "write_hash", cellToWrite)
    if err == redis.TxFailedErr {
      // Optimistic lock lost. Skip this, try next one.
      log.Printf("It was not possible to delete due to collision.\n")
      continue
    }
    if err != nil {
      panic(err)
    }
  }
}

func main() {
  ctx := context.Background()
  intervall_time, err := strconv.Atoi(os.Getenv("SYNC_INTERVAL_SECONDS"))
  if err != nil {
    panic(err)
  }

  for {
    reconcile(ctx)
    time.Sleep(time.Duration(intervall_time) * time.Second)
  }
}

