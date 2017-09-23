# crypto_manage_site

Proyecto para manejar precio de monedas de mercados
en Django y Postgress

Para generar proyecto local crypto_manage_site:

docker-compose run web django-admin.py startproject crypto_manage_site .

Para iniciar servicios

docker-compose up 

Entrar a container django

docker exec -it cryptomanagesite_web_1 bash