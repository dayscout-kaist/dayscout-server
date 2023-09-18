# Dayscout Server

![GitHub Pipenv locked Python version (main)][badge/python-version]
[![Code style: black][badge/black]][repo/black]
[![Imports: isort][badge/isort]][isort]
[![pre-commit][badge/pre-commit]][repo/pre-commit]
[![Conventional Commits][badge/conventional-commits]][conventional-commits]

## Quick Start

Use pipenv to install packages. (e.g., `pipenv install <package>`)

```bash
pipenv --python 3.11 # Use python 3.11
pipenv shell # Activate virtual environment
pipenv install # Install packages

# Run `pre-commit` automatically on `git commit`
pre-commit install
pre-commit install --hook-type commit-msg
```

## How to Run

```bash
uvicorn src.main:app --reload
```

## How to Contribute

1. Follow [Conventional Commits][conventional-commits] for writing commit messages.
2. Use type hints strictly. (Check [PEP 484][pep-484].)

[badge/python-version]: https://img.shields.io/github/pipenv/locked/python-version/dayscout-kaist/dayscout-server/main
[badge/black]: https://img.shields.io/badge/code%20style-black-000000
[badge/isort]: https://img.shields.io/badge/%20imports-isort-%231674b1?labelColor=ef8336
[badge/pre-commit]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit
[badge/conventional-commits]: https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white
[isort]: https://pycqa.github.io/isort
[conventional-commits]: https://conventionalcommits.org
[pep-484]: https://peps.python.org/pep-0484/
[repo/black]: https://github.com/psf/black
[repo/pre-commit]: https://github.com/pre-commit/pre-commit
