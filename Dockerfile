FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .

RUN apk add --no-cache py3-pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]