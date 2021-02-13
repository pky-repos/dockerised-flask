FROM ubuntu:latest

LABEL key="PankajKY" 

# CMD tail -f /dev/null

RUN apt-get update -y && apt-get install -y python3-pip python-dev

EXPOSE 80
EXPOSE 5000

COPY ./requirements.txt /SumAPI/requirements.txt

WORKDIR /SumAPI

RUN pip3 install -r requirements.txt

COPY . /SumAPI

ENTRYPOINT [ "python3" ]
CMD [ "rest.py" ]
