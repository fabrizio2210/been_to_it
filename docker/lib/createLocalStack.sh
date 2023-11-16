#!/bin/bash

# Supposing to deploy on x86_64 architecture
docker build -t fabrizio2210/been_to_it-backend -f docker/x86_64/Dockerfile-backend .
docker build -t fabrizio2210/been_to_it-frontend -f docker/x86_64/Dockerfile-frontend .
docker build -t fabrizio2210/been_to_it-worker -f docker/x86_64/Dockerfile-worker .
docker compose -f docker/lib/stack.yml --env-file="~/.docker/been_to_it-dev.env" up
