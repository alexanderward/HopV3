FROM osgeo/gdal
ENV PYTHONUNBUFFERED=1
RUN apt-get update -y
RUN apt-get install -y python3-pip

RUN mkdir /code

COPY requirements /code/requirements

WORKDIR /code
RUN pip3 install -r requirements/dev.txt

WORKDIR /code/tasks
ENTRYPOINT ["tail", "-f", "/dev/null"]