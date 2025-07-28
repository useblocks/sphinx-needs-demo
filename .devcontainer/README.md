# Dev Container README

This directory contains the configuration for the development container used in this project.

## Prerequisites

- **Docker** must be installed on your system.  
    [Get Docker](https://docs.docker.com/get-docker/)

## ubCode License

To use ubCode within the dev container, you must provide a valid license file as described in the [ubCode documentation](https://ubcode.useblocks.com/usage/ublicense.html).

**Steps:**
1. Obtain your license file (`ubcode.toml`).
2. Place the license file in this location: `$HOME/.ubcode/ubcode.toml, the devcontainer is configured to automatically fetch it from this location.

## Usage

1. Open the project in [VS Code](https://code.visualstudio.com/) and install the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension.
2. Reopen the folder in the container (`Remote-Containers: Reopen in Container`).
3. The development environment incl. ubcode Visual Studio Code extension will be set up automatically.

## Troubleshooting

- Ensure Docker is running before opening the dev container.
- Verify the ubCode license file is present and correctly configured.
