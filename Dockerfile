FROM python:3.10.10

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirments.txt .

RUN pip install -r requirments.txt 
COPY . .
# EXPOSE 8000
EXPOSE $PORT
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]
CMD ["gunicorn", "core.wsgi:application"]


