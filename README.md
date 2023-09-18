# Dayscout Server

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

[conventional-commits]: https://www.conventionalcommits.org/en/v1.0.0/
[pep-484]: https://peps.python.org/pep-0484/
