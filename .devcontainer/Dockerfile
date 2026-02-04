# Use the same base image as the devcontainer
FROM mcr.microsoft.com/vscode/devcontainers/base:ubuntu24.04

# Install necessary packages using a single RUN command to optimize layers
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        default-jre \
        graphviz \
        cmake \
        curl \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Rust as vscode user
USER vscode
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y \
    && echo 'source "$HOME/.cargo/env"' >> /home/vscode/.bashrc

# Add Rust to PATH for the build process
ENV PATH="/home/vscode/.cargo/bin:${PATH}"

#RUN echo 'source "/home/vscode/.rye/env"' >> /home/vscode/.bashrc
#ENV PATH="$PATH:/home/vscode/.rye/env"
# Set the default working directory and user
WORKDIR /workspace
