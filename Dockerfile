FROM python:3.12.3-slim AS base

# set the working directory.
WORKDIR /usr/src/

# add image metadata.
LABEL maintainer="Mango Habanero <main@mango-habanero.dev>"
LABEL description="Base image for portfolio backend."
LABEL repository="https://github.com/PhilipWafula/mango-habanero-be"
LABEL homepage="https://mango-habanero.dev"
ARG SOURCE_COMMIT
LABEL revision=${SOURCE_COMMIT:-unknown}

# create a group and user.
RUN addgroup --system app && adduser --system --group app

# set environment variables.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    PATH="/root/.local/bin:$PATH"

# install system dependencies.
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && apt clean

# install poetry.
RUN curl -sSL https://install.python-poetry.org | python3 -

# copy dependecy files.
COPY pyproject.toml poetry.lock ./

# copy the project (done before install to ensure console scripts are available).
COPY ./app /usr/src/app

RUN poetry install --no-ansi --no-dev --no-interaction

# grant permissions.
RUN chown -R app:app /usr/src/

# set the entrypoint.
EXPOSE 8000

# run the application.
CMD ["mhcli", "server", "start", "app.main:app", "--host=0.0.0.0", "--port=8000"]