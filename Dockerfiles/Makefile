BASE_VERSION:=2.2.2
CONTAINER_IMAGE:=ghcr.io/schwarzit/node-red-iep
SUFFIX:=latest

.PHONY: build-container-image
build-container-image:
	@docker buildx build --build-arg BASE_VERSION=$(BASE_VERSION) -t $(CONTAINER_IMAGE):$(BASE_VERSION)-$(SUFFIX) .

.PHONY: push-container-image
push-container-image: build-container-image
	@docker push $(CONTAINER_IMAGE)