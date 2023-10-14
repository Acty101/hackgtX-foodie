build:
	docker build -t acty101/hackgt .

upload:
	docker push acty101/hackgt

run:
	docker run --gpus all acty101/hackgt

# used when need to swap docker container for RunPod since name:tag combo needs to change to guarantee a new image is pulled
upload2:
	docker build -t acty101/hackgt:latest2 .
	docker push acty101/hackgt:latest2

test:
	python3 test.py