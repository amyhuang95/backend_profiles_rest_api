#!/bin/bash

# Disable apt-daily services
sudo systemctl disable apt-daily.service
sudo systemctl disable apt-daily.timer

# Update package list and install required packages
sudo apt-get update
sudo apt-get install -y python3-venv zip

# Set up Python alias
BASH_ALIASES=/home/vscode/.bash_aliases
touch $BASH_ALIASES
if ! grep -q PYTHON_ALIAS_ADDED $BASH_ALIASES; then
  echo "# PYTHON_ALIAS_ADDED" >> $BASH_ALIASES
  echo "alias python='python3'" >> $BASH_ALIASES
fi
