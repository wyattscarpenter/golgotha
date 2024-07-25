pip install -U build twine
python -m build
cd dist/
twine upload *
