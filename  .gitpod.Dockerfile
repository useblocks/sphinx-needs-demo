FROM gitpod/workspace-python-3.12:latest

RUN sudo install-packages \
    graphviz \
    openjdk-19-jre

RUN pip install -r requirements.txt
