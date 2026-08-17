test.bat && ruff check --ignore E741,SIM117,UP031 && pyright && mypy --install-types --pretty . && git diff --check
