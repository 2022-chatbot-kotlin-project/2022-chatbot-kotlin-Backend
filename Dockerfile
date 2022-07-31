# pull official base image
FROM python

# set work directory
WORKDIR /hygge/backend

COPY requirements.txt /hygge/backend/requirements.txt

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY . /hygge/backend

# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]