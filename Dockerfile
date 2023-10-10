FROM python:3.9-slim

ENV TARGET="google.com" 
ENV METHOD="HEAD" 
ENV INTERVAL="3000"

WORKDIR /snail-trace
COPY app.py .

CMD ["python", "-u", "/snail-trace/app.py"]