FROM elevy99927/python-secure:3.11.13
WORKDIR /app
COPY requirements.txt app.py /app/
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python", "-m", "uvicorn", "app:api", "--host", "0.0.0.0", "--port", "8080"]
