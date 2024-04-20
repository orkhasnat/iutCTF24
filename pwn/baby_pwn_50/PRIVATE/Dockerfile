FROM pwn.red/jail
COPY --from=ubuntu:22.04 / /srv
COPY baby /srv/app/run
COPY flag.txt /srv/app/flag.txt
ENV JAIL_PORT=1569
