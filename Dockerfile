FROM python:3.8-alpine
WORKDIR /usr/src/flaskApp
COPY flaskApp .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD ["python3", "app.py"]

