VERSION=2.2.2
CONTAINER_REPO=ghcr.io/schwarzit/node-red-oidc
CONTAINER_IMAGE=$(CONTAINER_REPO):$(VERSION)

.PHONY: build-container-image
build-container-image:
	@docker buildx build --build-arg VERSION=$(VERSION) -t $(CONTAINER_IMAGE) .

.PHONY: push-container-image
push-container-image: build-container-image
	@docker push $(CONTAINER_IMAGE)