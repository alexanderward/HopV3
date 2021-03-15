FROM osgeo/gdal
ENV PYTHONUNBUFFERED=1
RUN apt-get update -y
RUN apt-get install -y python3-pip rsync

ENV TERRAFORM_VERSION=0.14.6
RUN wget https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/bin

RUN mkdir /code

COPY requirements /code/requirements

WORKDIR /code
RUN pip3 install -r requirements/dev.txt

