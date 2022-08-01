# base image
FROM python

# set work directory
WORKDIR /hygge/backend

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONUNBUFFERED 1
# Prevents Python from buffering stdout and stderr (equivalent to python -u option)

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /hygge/backend/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /hygge/backend