
FROM python:3.7-slim

COPY requirements.txt /flask_app/
WORKDIR /flask_app
RUN pip install --trusted-host pypi.python.org -r requirements.txt; \
    apk del --no-cache --purge .build-deps ;\
    rm -rf /var/cache/apk/*
COPY . /flask_app
EXPOSE 3039
CMD ["python", "app.py"]
