ARG PYTHON_VERSION=3.12
FROM --platform=linux/amd64 python:${PYTHON_VERSION} as django_base

#ENV PYTHONUNBUFFERED=1
#ENV PYTHONDONTWRITEBYTECODE=1
# Virtual envrionment location
ENV VIRTUAL_ENV_PATH=/backend/django/venv/
# Poetry install location
ENV POETRY_HOME=/etc/poetry

ARG UID=1000
ARG GID=1000
ARG UNAME=octave

# Install virtualenv and install poetry
RUN #python3 -m pip install virtualenv psycopg2-binary
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=$POETRY_HOME python3 -

WORKDIR /backend/django/src/

# create a new group and user with specific ids
RUN groupadd --system --gid=$GID $UNAME && useradd --system --uid=$UID --gid=$GID $UNAME
RUN mkdir /home/$UNAME && chown -R $UNAME:$UNAME /home/$UNAME && chown -R $UNAME:$UNAME /backend/

USER $UNAME

# Setup virtualenv and auto source virtual env
RUN python -m venv $VIRTUAL_ENV_PATH && echo 'source $VIRTUAL_ENV_PATH/bin/activate' >> /home/$UNAME/.bashrc
ENV PATH $VIRTUAL_ENV_PATH/bin:$POETRY_HOME/bin:$PATH

# Copy project files and install dependencies
COPY --chown=$UNAME:$UNAME *.rst LICENSE setup.* pyproject.toml ./
COPY --chown=$UNAME:$UNAME puppeteer_pdf ./puppeteer_pdf
RUN . $VIRTUAL_ENV_PATH/bin/activate && poetry install --with test

#ENTRYPOINT ["/docker-entrypoint"]
#CMD ["$VIRTUAL_ENV_PATH/bin/python3", "pytest"]
