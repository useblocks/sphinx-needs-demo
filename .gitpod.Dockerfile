FROM gitpod/workspace-python-3.12:latest

RUN sudo install-packages \
    graphviz \
    openjdk-19-jre

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Add uv to PATH
ENV PATH="/home/gitpod/.cargo/bin:$PATH"
