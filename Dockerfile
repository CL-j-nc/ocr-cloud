FROM paddlepaddle/paddle:2.6.1-gpu-cuda11.7-cudnn8

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]