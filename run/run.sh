#!/bin/bash

# Check if an API key argument is provided
if [ $# -ne 1 ]; then
  echo "ERROR! OPENAI_API_KEY required"
  exit 1
fi

# Assign the API key argument to the OPENAI_API_KEY environment variable
export OPENAI_API_KEY="$1"

# Run main.py
python ../backend/app.py
