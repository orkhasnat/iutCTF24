FROM pwn.red/jail
COPY --from=ubuntu:22.04 / /srv
COPY seek /srv/app/run
COPY flag.txt /srv/app/flag.txt
ENV JAIL_PORT=6969
ENV JAIL_TMP_SIZE=500
