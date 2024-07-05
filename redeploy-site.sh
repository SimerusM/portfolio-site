#!/bin/bash

# Kill all existing tmux sessions
tmux kill-server

# Ensure the latest changes from the main branch are pulled from GitHub
git fetch && git reset origin/main --hard

# Activate the Python virtual environment and install requirements
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# Start a new detached tmux session and run the Flask server
tmux new-session -d -s current_session "source python3-virtualenv/bin/activate && flask run --host=0.0.0.0"
