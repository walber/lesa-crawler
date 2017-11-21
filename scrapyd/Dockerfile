FROM vimagick/scrapyd:py3

RUN set -xe \
    && apt-get update && apt-get install --no-install-recommends -y \
    curl \
    cron \
    supervisor

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN mkdir -p /var/log/supervisord/
RUN touch /var/log/supervisord/supervisord.log
RUN systemctl enable supervisor
    
# Sets the application timezone.
RUN echo "America/Recife" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata
RUN pip install elasticsearch-dsl jira

COPY ./cron-file /etc/cron.d/cron-file
RUN chmod 0644 /etc/cron.d/cron-file
RUN crontab /etc/cron.d/cron-file
RUN touch /var/log/cron.log

WORKDIR /var/lib/scrapyd/

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]