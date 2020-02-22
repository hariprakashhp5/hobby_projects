
FROM python:3.7-slim


COPY ./requirements.txt /py_project/
WORKDIR /py_project
RUN pip install  -r requirements.txt;
COPY . /py_project
EXPOSE 3039
CMD ["python", "app.py"]
