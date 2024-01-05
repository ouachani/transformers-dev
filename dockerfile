FROM python:3.11-slim

# Update the package index and install anv tools
RUN apt update \
    && apt install -y git

# Update Python pip
RUN pip install --upgrade pip \
# Install PyTorch
    && pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu \
# Install transformers 
    && pip install transformers \
# Install huggingface-cli
    && pip install huggingface-cli

WORKDIR /app

# Apps
COPY app/* /app

CMD ["sleep", "infinity"]
