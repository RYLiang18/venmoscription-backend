# !/bin/zsh
docker build -t venmoscription_backend_image .

# for interactive shell, it is 
docker run \
    -it \
    --name venmoscription_backend_container \
    venmoscription_backend_image:latest \
    /bin/sh