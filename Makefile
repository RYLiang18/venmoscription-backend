container_image_name = "backend_image"
container_name = "backend"

.PHONY: clean
clean: delete_container delete_image

.PHONY: create_image
create_image:
	docker build -t $(container_image_name) .

.PHONY: delete_image
delete_image:
	docker rmi $(container_image_name):latest

.PHONY: delete_container
delete_container:
	docker stop $(container_name)
	docker rm $(container_name)

.PHONY: it
it:
	docker run \
		-it \
		-p 5000:5000 \
		--name $(container_name) \
		$(container_image_name):latest \
		bash

.PHONY: flask
flask:
	docker run \
		-it \
		-p 5000:5000 \
		--name $(container_name) \
		$(container_image_name):latest \
		python -m flask --app flask_app run

.PHONY: interactive
interactive: clean create_image it

.PHONY: run
run: clean create_image flask