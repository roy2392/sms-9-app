FROM python:3.10-slim
WORKDIR /app
COPY src/ src/
RUN pip install flask
EXPOSE 8080
CMD ["python", "src/app.py"]