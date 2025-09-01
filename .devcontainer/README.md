# Dev Container README

This directory contains the configuration for the development container used in this project.

## Prerequisites

- **Docker** must be installed on your system.  
    [Get Docker](https://docs.docker.com/get-docker/)

## ubCode License

To use ubCode within the dev container, you must provide a valid license as described in the [ubCode documentation](https://ubcode.useblocks.com/usage/ublicense.html#environmental-variables).

**Steps:**
1. Obtain your (test-)license from useblocks.
1. Create the environment variables `UBCODE_LICENSE_KEY` and `UBCODE_LICENSE_USER` on you host system.
1. Restart Visual Studio Code in case it was open during the creation of the environment variables
3. The `devcontainer` will automatically fetch the variables during startup. 

## Usage

1. Open the project in [VS Code](https://code.visualstudio.com/) and install the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension.
2. Reopen the folder in the container (`Remote-Containers: Reopen in Container`).
3. The development environment incl. ubcode Visual Studio Code extension will be set up automatically.

## Troubleshooting

- Ensure Docker is running before opening the dev container.
- Verify the ubCode license environment variables are present and correctly configured.
