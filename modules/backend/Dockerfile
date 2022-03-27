FROM python:3.9.11-alpine3.15

COPY ./common/ modules/common/
COPY ./backend/ modules/backend/

CMD python -m modules.backend.main_backend
