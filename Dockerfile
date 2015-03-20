FROM nginx:1.7.10
MAINTAINER Sergei Orlov
COPY nginx.conf /etc/nginx/
COPY mysites /etc/nginx/sites-available/mysites
RUN mkdir -p /etc/nginx/sites-enabled && \
    ln /etc/nginx/sites-available/mysites /etc/nginx/sites-enabled/
EXPOSE 80
CMD nginx
