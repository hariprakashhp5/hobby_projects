
FROM python:3.7-slim

COPY requirements.txt /app/
WORKDIR /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt; \
    apk del --no-cache --purge .build-deps ;\
    rm -rf /var/cache/apk/*
COPY . /app
ENV PYTHONPATH "${PYTHONPATH}:/app"
EXPOSE 3039
CMD ["python", "app.py"]
