#!/bin/bash

# Enter project folder
cd /root/portfolio-site

# Ensure the latest changes from the main branch are pulled from GitHub
git fetch && git reset origin/main --hard

docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up --build -d