# This is a dev container image definition

# Use the latest stable version of Python (at least 3.12) as the base image
FROM python:3.12-slim

# Install essential tools and dependencies
# - curl: for downloading files
# - git: for version control
# - unzip: for unzipping packages
# - vim: basic text editor
RUN apt-get update && apt-get install -y \
    curl \
    git \
    unzip \
    vim \
    && rm -rf /var/lib/apt/lists/*


# Install tfenv for managing Terraform versions
# tfenv allows easy installation and switching between different versions of Terraform
# Install tfenv and ensure ARM-compatible installation
RUN git clone https://github.com/tfutils/tfenv.git /root/.tfenv \
    && ln -s /root/.tfenv/bin/* /usr/local/bin/ \
    && ARCH=arm64 tfenv install latest \
    && tfenv use latest

# RUN curl https://raw.githubusercontent.com/tfutils/tfenv/master/install.sh | bash \
#     && ln -s /root/.tfenv/bin/* /usr/local/bin/ \
#     && tfenv install latest \
#     && tfenv use latest


# Install ARM-compatible AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install \
    && rm -rf awscliv2.zip ./aws

# Copy the Python requirements file to the container
# This file will contain all the Python dependencies needed for your project
COPY requirements.txt /tmp/

# Install Python dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Set the working directory inside the container
# All commands will be run from this directory
WORKDIR /workspace

# Expose a working port (optional) for development if needed
EXPOSE 8388

# Default command when the container starts
CMD [ "bash" ]