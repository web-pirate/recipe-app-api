FROM python:3.9-alpine3.13
LABEL maintainer="ManishSingh"

ENV PYTHONUNBUFFERED 1

# This will copy the requirements.txt from local machine to the working dir in hub.
COPY ./requirements.txt /tmp/requirements.txt 
COPY ./requirements.dev.txt /tmp/requirements.dev.txt 
COPY ./app /app  
WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ "$DEV" = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser \
    --disabled-password \
    --no-create-home\
    django-user

ENV PATH="/py/bin:$PATH"
# This user doesn't have full privilege and it is created by adduser later
USER django-user