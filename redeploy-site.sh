#!/bin/bash

# Ensure the latest changes from the main branch are pulled from GitHub
git fetch && git reset origin/main --hard

# Restart boot service
sudo systemctl restart myportfolio.service