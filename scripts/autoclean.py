from os import system


def autoclean():
    system("rm -rf dist")
    system("rm -rf xiver-gpt.egg-info")
    system("rm -rf .pytest_cache")
    system("rm -rf saves")
    system("find . -name __pycache__ -exec rm -rf {} \;")
