FROM php:7.4-fpm

RUN apt update -y && apt install -y nginx
COPY ./site.conf /etc/nginx/conf.d/site.conf

CMD ["sh", "-c", "nginx && php-fpm"]
