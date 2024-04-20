FROM python:slim AS app
RUN pip install --no-cache-dir progress 
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

FROM pwn.red/jail
COPY --from=app / /srv
COPY server.py /srv/app/run
COPY flag.txt /srv/app/flag.txt
RUN sed -i 's/\r$//' /srv/app/run
ENV JAIL_MEM=20M JAIL_TIME=300