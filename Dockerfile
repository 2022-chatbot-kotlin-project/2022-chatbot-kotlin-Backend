# pull official base image
FROM python

# set work directory
WORKDIR /hygge/backend

# set environment variables
# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONTWRITEBYTECODE 1
# Prevent Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /hygge/src/app/requirements
RUN pip install -r requirements.txt

# copy project
COPY . /hygge/backend