FROM python:3.11-slim
RUN pip install fastapi uvicorn httpx numpy boto3
WORKDIR /app
COPY app.py /app/app.py
EXPOSE 8080
CMD ["python", "-m", "uvicorn", "app:api", "--host", "0.0.0.0", "--port", "8080"]