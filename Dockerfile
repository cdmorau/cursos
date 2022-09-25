FROM python:3.8.2-alpine

WORKDIR /cursos

COPY requirements.txt requirements.txt

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python","./src/app.py"]
# docker run -p 5000:5000 cursosflask