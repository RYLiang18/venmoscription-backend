container_image_name = "backend_image"
container_name = "backend"

.PHONY: clean
clean: delete_container delete_image

.PHONY: image
image:
	docker build -t $(container_image_name) .

.PHONY: delete_image
delete_image:
	docker rmi $(container_image_name):latest

.PHONY: delete_container
delete_container:
	docker stop $(container_name)
	docker rm $(container_name)

.PHONY: interactive
interactive:
	docker run \
		-it \
		--env-file .env \
		-p 5000:5000 \
		--name $(container_name) \
		$(container_image_name):latest \
		bash

.PHONY: flask
flask:
	docker run \
		-it \
		--env-file .env \
		-p 5000:5000 \
		--name $(container_name) \
		$(container_image_name):latest \
		python -m flask --app "flask_app:create_app('development')" run