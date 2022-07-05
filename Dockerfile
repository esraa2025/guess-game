FROM python 

WORKDIR /files

COPY app.py .

CMD  ["python","./app.py"]

