FROM python:3.9-alpine

RUN pip install -r requirements.txt

ADD entrypoint.sh /entrypoint.sh

ADD requirements.txt /requirements.txt

ADD main.py /main.py

RUN chmod +x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]