FROM gitpod/workspace-python-3.12:latest

RUN sudo install-packages \
    graphviz \
    openjdk-19-jre

COPY requirements.txt requirements.txt

RUN pip install --update -r requirements.txt
