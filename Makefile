default: helm-docs

helm-docs:
	@echo "Generating helm docs"
	@helm-docs -t README.md.gotmpl -o README.md -b for-the-badge

