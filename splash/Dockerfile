FROM scrapinghub/splash:3.0

RUN set -xe \
    && apt-get update && apt-get install --no-install-recommends -y \
    tzdata \
    cron \
    supervisor

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN mkdir -p /var/log/supervisord/
RUN touch /var/log/supervisord/supervisord.log
RUN systemctl enable supervisor

# Sets the application timezone.
RUN ln -fs /usr/share/zoneinfo/America/Recife /etc/localtime
RUN dpkg-reconfigure -f noninteractive tzdata

COPY ./cron-file /etc/cron.d/cron-file
RUN chmod 0644 /etc/cron.d/cron-file
RUN crontab /etc/cron.d/cron-file
RUN touch /var/log/cron.log

ENTRYPOINT [ \
    "/usr/bin/supervisord", \
    "-c", \
    "/etc/supervisor/conf.d/supervisord.conf" \
]