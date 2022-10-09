FROM python:latest

WORKDIR /backend

RUN pip install --upgrade pip

COPY ./requirements.txt /backend/requirements.txt
RUN pip install -r requirements.txt

COPY . /backend

EXPOSE 5000

CMD ["python", "app.py"]