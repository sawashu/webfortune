# Webfortune

This application is a Dockerrized Flask App that provides a Web front-end to the well-known Linux programs 'cowsay' and 'fortune'. 

## Build Docker Image

Type `docker build -t sawashu/webfortune .`

## Run App

To run from the command line, type `python3 -m flask run --host=0.0.0.0`.
To run from the docker, type `docker run -dp <CONTAINER_PORT>:5000 sawashu/webfortune`.

## Test App

To test from the command line, type `pytest test_app.py`. 
