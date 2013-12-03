from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField
# Create your models here.

class Alumno(models.Model):
	matricula = models.CharField(max_length = 20)
	nombre_usu = models.CharField(max_length = 30)
	sexo = models.CharField(max_length = 10)
	password = models.CharField(max_length = 16)
	fecha_nacimiento = models.DateField(auto_now = True)
	avatar = ListField(EmbeddedModelField('Avatar'))
	area = ListField(EmbeddedModelField('Area'))
	escuela = ListField(EmbeddedModelField('Escuela'))
	casa = ListField(EmbeddedModelField('Casa'))
	misiones = ListField(EmbeddedModelField('Mision'))
	
class Avatar(models.Model):
	url_avatar = models.URLField()
	#piel = ListField(EmbeddedModelField('pielAvatar')
	cabello = ListField(EmbeddedModelField('cabelloAvatar'))
	accesorio = ListField(EmbeddedModelField('accesorioAvatar'))
	
class pielAvatar(models.Model):
	url_piel = models.URLField()

class cabelloAvatar(models.Model):
	url_cabello = models.URLField()
	
class accesorioAvatar(models.Model):
	url_accesorio = models.URLField()
	
class Escuela(models.Model):
	nombre_esc = models.CharField(max_length = 100)
	
class Area(models.Model):
	nombre_area = models.CharField(max_length = 30)

class Mision(models.Model):
	nombre_mision = models.CharField(max_length = 50)
	avance = models.CharField(max_length = 5)
	fecha_ini_mision = models.DateField(auto_now = True)
	
class AlumnoHasMision(models.Model):
	alumnos_id_alumno = models.ForeignKey(Alumno)
	mission_id_mision = models.ForeignKey(Mision)
	
class AreaHasAlumnos(models.Model):
	area_id_area = models.ForeignKey(Area)
	alumnos_id_alumno = models.ManyToManyField(Alumno)
	puntos = models.IntegerField()

class Administrador(models.Model):
	nombre_admin = models.CharField(max_length = 50)
	pass_admin = models.CharField(max_length = 16)
	
class Casa(models.Model):
	nombre_casa = models.CharField(max_length = 50)
	id_administrador = models.ForeignKey(Administrador)
	
class Experimento(models.Model):
	descripcion_experimento = models.TextField()

class Preghc(models.Model):
	descripcion_hc = models.TextField()
	id_mision = models.ForeignKey(Mision)
	id_casa= models.ForeignKey(Casa)
	
class Respuestashc(models.Model):
	texto_resp_hc = models.TextField()
	f_v_hc = models.BooleanField()
	preghc_id_preghc  = models.ForeignKey(Preghc)

class Preggral(models.Model):
	descripcion_gral = models.TextField()
	id_area = models.ForeignKey(Area)
	id_mision = models.ForeignKey(Mision)

class Respuestasgral(models.Model):
	texto_resp_gral = models.TextField()
	f_v_gral = models.BooleanField()
	preggral_id_preggral  = models.ForeignKey(Preggral)
	
class Publicacion(models.Model):
	fecha_publicacion = models.DateField()
	texto_publicacion = models.TextField()
	id_alumnos = models.ForeignKey(Alumno)
	
class PublicacionHasAlumnos(models.Model):
	publicacion_id_publicacion = models.ForeignKey(Publicacion)
	alumnos_id_alumno = models.ForeignKey(Alumno)

class Notificaciones(models.Model):
	texto_notificacion = models.TextField()
	id_alumnos = models.ForeignKey(Alumno)
	id_publicacion = models.ForeignKey(Publicacion)