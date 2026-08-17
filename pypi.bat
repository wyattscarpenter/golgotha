check.bat && pip install -U build twine && python -m build && twine upload --skip-existing dist/*
REM See also git-pip-publish in gyatt, which is like basically this script but without the check.bat invocation so not as good for this particular project: https://github.com/wyattscarpenter/gyatt/blob/master/git-pip-publish
