cp flask_app.nginx.conf /etc/nginx/sites-enabled/bells.nginx.conf
certbot --nginx -d bells.silaeder.codingprojects.ru
