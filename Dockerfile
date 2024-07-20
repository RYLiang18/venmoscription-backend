FROM python:3.12-slim-bullseye

ENV USER appuser
RUN useradd --create-home --shell /bin/bash ${USER}
USER ${USER}
WORKDIR /home/${USER}

EXPOSE 5000/tcp

RUN python -m pip install -U pip

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install python-dotenv
RUN pip freeze > requirements-dev.txt

# // other packages ////////////////////
# RUN pip install Flask-WTF
# RUN pip install Flask-Bcrypt
# RUN pip install Flask-Login
# RUN pip install flask-mongoengine
# //////////////////////////////////////

COPY . .