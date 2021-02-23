FROM python:3.9-alpine

RUN pip install algoliaseach

ADD entrypoint.sh /entrypoint.sh

ADD main.py /main.py

RUN chmod +x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]