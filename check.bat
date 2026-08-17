test.bat && ruff check --ignore E741,SIM117,UP031 && pyright && mypy --strict --disable-error-code no-untyped-def --pretty . && git diff --check
