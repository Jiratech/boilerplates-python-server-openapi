#Generate the openapi
FROM openapitools/openapi-generator-cli:v6.0.0 as openapi

WORKDIR '/opt/openapi-generator/modules/openapi-generator-cli/target'
ADD 'https://raw.githubusercontent.com/Jiratech/boilerplates-openapi-schema/master/schema.json' ./schema.json
RUN java -jar openapi-generator-cli.jar generate -i schema.json -g python-flask -o /openapi

#Build the docker image
FROM python:3.8-alpine

#Copy the source code
COPY controllers/ src/controllers/
COPY requirements.txt src/
COPY app.py src/
COPY schema.json src/schema.json
COPY --from=openapi /openapi src/openapi

#Install the dependencies
WORKDIR /src
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
ENV FLASK_ENV=production

ENTRYPOINT ["python3"]
CMD ["-m", "app"]
