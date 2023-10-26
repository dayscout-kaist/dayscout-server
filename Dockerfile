FROM python:3.11

# Copy repo
WORKDIR /code

COPY Pipfile Pipfile.lock ./

# Install python dependencies
RUN pip install pipenv \
    && pipenv --python 3.11 \
    && pipenv install --dev --system --deploy

COPY src/ ./src

# Run container
EXPOSE 80
CMD ["sh", "-c", "python -m uvicorn src.main:app --port 80 --host 0.0.0.0"]
