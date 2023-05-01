FROM python:3-slim
WORKDIR /api
COPY ./api /api
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000
ENV CI=true
CMD ["python", "main.py"]
