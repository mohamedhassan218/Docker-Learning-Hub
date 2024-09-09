FROM python:alpine
WORKDIR /code
ADD app.py requirements.txt code/
COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install -r /tmp/requirements.txt
CMD ["python", "app.py"]
