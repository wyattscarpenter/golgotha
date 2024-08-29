test.bat && ruff check --ignore E741 && pyright && mypy --install-types --pretty . && git diff --check
