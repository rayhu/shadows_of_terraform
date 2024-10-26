#docker build -t python-terraform-dev .

#docker run -it -v $(pwd):/workspace python-terraform-dev

#docker stop my-python-dev-container
#docker rm my-python-dev-container

#docker run --name my-python-dev-container -it -v $(pwd):/workspace python-terraform-dev

#aws configure

# Docker has integrated Compose functionality directly into the Docker CLI, so docker-compose can now be accessed using docker compose (with a space instead of a hyphen).

docker build -t python-terraform-dev:latest -f .devcontainer/Dockerfile .

docker compose up --build