container_image_name = "backend_image"
container_name = "backend"

.PHONY: clean
clean: delete_container delete_image

.PHONY: create_image
create_image:
	docker build -t $(container_image_name) .

.PHONY: stop_image
delete_image:
	docker rmi $(container_image_name):latest

.PHONY: stop_container
delete_container:
	docker stop $(container_name)
	docker rm $(container_name)

.PHONY: interactive
interactive: create_image
	docker run \
		-it \
		-p 5000:5000 \
		--name $(container_name) \
		$(container_image_name):latest \
		bash