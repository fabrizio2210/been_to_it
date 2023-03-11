#!/bin/bash

# Supposing to deploy on x86_64 architecture
docker build -t fabrizio2210/been_to_it-backend -f docker/x86_64/Dockerfile-backend .
docker build -t fabrizio2210/been_to_it-frontend -f docker/x86_64/Dockerfile-frontend .
docker compose -f docker/lib/stack.yml --env-file="/home/fabrizio/.docker/been_to_it-dev.env" up
