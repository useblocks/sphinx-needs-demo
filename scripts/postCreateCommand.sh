#!/bin/bash

# Install uv package manager
curl -LsSf https://astral.sh/uv/install.sh | sh

# Add uv to PATH for current session
export PATH="$HOME/.cargo/bin:$PATH"

# Sync dependencies
uv sync
