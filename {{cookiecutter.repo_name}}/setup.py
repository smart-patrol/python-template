import os
from typing import List

from setuptools import find_packages, setup

_repo: str = "{{cookiecutter.repo_name}}"
_pkg: str = "{{cookiecutter.package_name}}"
_version = "0.0.1"

def read(fname) -> str:
    """Read the content of a file.
    You may use this to get the content of, for e.g., requirements.txt, VERSION, etc.
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# Declare minimal set for installation
required_packages: List[str] = []

test_packages = ["pytest>=5.4.3", "black>=19.10b0", "flake8>=3.8.3"]

util_packages = ["pre-commit>=2.6.0"]

dev_packages = test_packages + util_packages


if __name__ == "__main__":
    try:
        setup(
            name=_pkg,
            packages=find_packages(where="src"),
            version=_version,
        description="{{cookiecutter.description}}",
        long_description=read("README.md"),
        author="{{cookiecutter.author_name}}",
        url=f"https://github.com/abcd/{_repo}/",
        download_url="",
        project_urls={
            "Bug Tracker": f"https://github.com/abcd/{_repo}/issues/",
            "Documentation": f"https://{_repo}.readthedocs.io/en/stable/",
            "Source Code": f"https://github.com/abcd/{_repo}/",
        },
        {% if cookiecutter.open_source_license != "No license file" -%}
        license="{{cookiecutter.open_source_license}}",
        {% endif -%}
        keywords="word1 word2 word3",
        platforms=["any"],
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "Intended Audience :: System Administrators",
            "Natural Language :: English",
            {% if cookiecutter.open_source_license != "No license file" -%}
            "License :: OSI Approved :: {{cookiecutter.open_source_license}}",
            {% endif -%}
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
        ],
        python_requires=">=3.6.0",
        install_requires=required_packages,
        extras_require={"dev": dev_packages, "test": test_packages},
        )
    except:  # noqa
        print(
            "\n\nAn error occurred while building the project, "
            "please ensure you have the most updated version of setuptools, "
            "setuptools_scm and wheel with:\n"
            "   pip install -U setuptools setuptools_scm wheel\n\n"
        )
        raise ValueError(
    "Baseline setup.py from cookiecutter template. "
    "Please review and modify accordingly, then remove this exception")
