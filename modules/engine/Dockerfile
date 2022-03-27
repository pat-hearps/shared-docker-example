FROM python:3.9.11-alpine3.15

COPY ./common/ modules/common/
COPY ./engine/ modules/engine/

CMD python -m modules.engine.main_eng
