FROM python:3.9.11-alpine3.15

WORKDIR /modules

COPY ./common/ ./common/
COPY ./engine/ ./engine/

CMD python -m engine.main_eng
