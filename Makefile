.PHONY: clean
clean:
	docker stop backend
	docker rm backend
	docker rmi backend_image:latest
	
.PHONY: interactive
interactive: clean
	docker build -t backend_image .
	docker run \
		-it \
		-p 5000:5000 \
		--name backend \
		backend_image:latest \
		bash