#!/bin/bash

# Environment variables to configure the installed packages


export RYE_INSTALL_OPTION="--yes"

curl -sSf https://rye.astral.sh/get | bash

source "$HOME/.rye/env"
rye sync
