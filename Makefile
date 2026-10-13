.PHONY: save problem

# `make problem <name>` creates the Python solution file and opens it in Vim.
ifneq ($(filter problem,$(MAKECMDGOALS)),)
PROBLEM_NAME := $(word 2,$(MAKECMDGOALS))
.PHONY: $(PROBLEM_NAME)
$(PROBLEM_NAME):
	@:
endif

problem:
	@if [ -z "$(PROBLEM_NAME)" ]; then \
		echo "Usage: make problem <name>" >&2; \
		exit 2; \
	fi
	@mkdir -p leetcode/python
	@touch "leetcode/python/$(PROBLEM_NAME).py"
	@vim "leetcode/python/$(PROBLEM_NAME).py"

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
