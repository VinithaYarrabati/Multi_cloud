FROM python:3.12-slim as build 
RUN copy src /app/src
RUN copy requirment.txt /app
WORKDIR /app
RUN pip install -r /app/requirmenta.txt
ENV APP_TYPE=auth
CMD if [ "$APP_TYPE" = "auth" ]; then \
        uvicorn src.auth.main:app --host 0.0.0.0 --port 8000; \
    else \
        uvicorn src.transaction.main:app --host 0.0.0.0 --port 8001; \
    fi
