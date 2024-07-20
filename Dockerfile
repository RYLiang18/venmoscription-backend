FROM python:3.10.12-slim-bullseye

ENV USER appuser
RUN useradd --create-home --shell /bin/bash ${USER}
USER ${USER}
WORKDIR /home/${USER}

EXPOSE 5000/tcp

RUN python -m pip install -U pip

COPY requirements.txt .
RUN pip install -r requirements.txt

# RUN pip install python-dotenv
RUN pip freeze > requirements-dev.txt


COPY . .