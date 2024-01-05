# Transformers Development Repository

## Introduction
This repository allows you to create a development environment meant for the development and improvement of Transformer & Pytorch models. It’s a community-driven project, and contributions are welcome.

## Create transformers-env
### Build docker image
docker build --cache-from transformers-dev:v0 -t transformers-dev:v0 .

### Run container & store downloaded models
docker run -d --name transformers-env -v C:\Users\ouach\workspaces\ML\Pytorch\transformers-dev\models:/root/.cache/huggingface/hub transformers-dev:v0


# Use vscode to plugin container transformers-env