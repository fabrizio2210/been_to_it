#!/bin/bash

# Supposing to deploy on x86_64 architecture
docker build -t fabrizio2210/been_to_it-backend-dev -f docker/x86_64/Dockerfile-backend-dev .
docker build -t fabrizio2210/been_to_it-frontend-dev -f docker/x86_64/Dockerfile-frontend-dev .
docker compose -f docker/lib/stack-dev.yml --env-file="/home/fabrizio/.docker/been_to_it-dev.env" up
