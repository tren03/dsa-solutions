.PHONY: save

# Stage all changes, create a timestamped commit when needed, and push to origin.
save:
	@set -e; \
	git add -A; \
	if git diff --cached --quiet; then \
		echo "No changes to commit."; \
	else \
		git commit -m "Update $$(date '+%Y-%m-%d %H:%M:%S %z')"; \
	fi; \
	git push
