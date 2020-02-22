
FROM python:3.7-slim as flask_app
COPY ./requirements.txt /py_project/
WORKDIR /py_project
RUN pip install  -r requirements.txt;
COPY . /py_project
EXPOSE 3039
CMD ["python", "flask_app.py"]


FROM grafana/grafana:6.6.2-ubuntu as grafana
RUN grafana-cli plugins install grafana-clock-panel
RUN grafana-cli plugins install grafana-simple-json-datasource
ENV GF_USERS_DEFAULT_THEME light
ENV GF_AUTH_ANONYMOUS_ENABLED true
ENV GF_AUTH_ANONYMOUS_ORG_NAME Anonymous
ENV GF_AUTH_ANONYMOUS_ORG_ROLE Viewer
CMD ["/run.sh"]