import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description =f.read()

_version_ = "0.0.0"

REPO_NAME = "Wine-quality"
AUTHOR_USER_NAME = "busharashaikh24"
SRC_REPO = "Wine-quality-prediction"
AUTHOR_EMAIL = "busharashaikh24@gmail.com"

setuptools.setup(
name=SRC_REPO,
version=_version_,
author=AUTHOR_USER_NAME,
author_email=AUTHOR_EMAIL,
dEscription="A small python package for ml app",
long_description=long_description,
long_description_content="text/markdown",
url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
project_urls={
    "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
},
package_dir={"": "src"},
packages=setuptools.find_packages(where="src")
)