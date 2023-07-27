from os import system

from .build import build


def public() -> None:
    system("rm -rf dist")
    system("rm -rf xiver-gpt.egg-info")

    build()
    system("twine upload dist/*")

    system("rm -rf dist")
    system("rm -rf xiver-gpt.egg-info")

    print("SUCCESS")
