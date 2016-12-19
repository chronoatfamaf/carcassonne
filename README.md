# Carcassonne

Instalacion:

virtualenv -p python 3 NOMBRE
source NOMBRE/bin/activate
pip3 install django
pip3 install django-widget-tweaks
pip3 install django-widget-tweaks
pip3 install Pillow 
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver

Comentario General del proyecto:

	Lo que se logro:
		Registro, login,logout, ver perfil y editar perfil usuario.
		crear, listar, unirse, y abandonar partidas.
		un sistema de turnos que permitia compartir el juego entre varios usuarios online,
		implementar las clases fundamentales de la aplicacion y algunas de sus funcionalidades
		principales aunque con bugs,
		se logro con bugs girar imagen, colocar seguidores en la imagen.
	Lo que no se logro:
		No hay conteo de puntos, no se implemento el bot para jugar,
		y hay bugs sin solucionar. No se logro un correcto uso de Github

	Fuentes:
		Principalmente stackoverflow.
		Javascript de:
		http://www.w3schools.com/js/
		Turnos desde:
		https://en.wikipedia.org/wiki/Post/Redirect/Get

	Dificultades:
		Poco tiempo, mala administracion general, muchos errores en la division y ejecucion de tareas,
		mala planificacion y diseño, fueron surgiendo muchos problemas en el codigo que no consideramos o no conocimaos si quiera que hicieron que tuvieramos que volver a hacer cosas que ya habiamos hecho,  de haber hecho cosas que ni siquiera usamos, estos bugs ya en etapas muy avanzadas tuvieron un costo en tiempo imposible de solventar.

	Criticas constructivas: 
		- Nos parecio un proyecto bastante grande para hacerse en dos semanas con un grupo o equipo totalmente nuevo,
		sin conocernos, ni saber como trabajabamos, teniendo en cuenta que recien comenzabamos con Django.
		- Nos parecio una dificultad extra implementar un juego ya que Django esta diseñado para realizar aplicaciones webs.
		- Creemos que de haber realizado bien el trabajo en equipo tal vez hubieramos llegado al objetivo,  pero para ello hubiera sido neceserio ya conocernos y haber trabajado antes en otro
		proyecto.