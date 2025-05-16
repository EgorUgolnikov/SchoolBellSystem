cp flask_app.nginx.conf /etc/nginx/sites-available/bells.nginx.conf
certbot --nginx -d bells.silader.codingporjects.ru
