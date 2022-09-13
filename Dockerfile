FROM python:3.8.2
WORKDIR ./src/app.py
ADD . /src/app.py
RUN pip install -r requirements.txt 
CMD ["python", "./src/app.py"]