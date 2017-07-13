from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.core.mail import send_mail

class Hiba(models.Model):
	id = models.AutoField(primary_key=True)
	nev = models.CharField(max_length=200,help_text="Adja meg a hiba bejelento nevet", default='')
	cim = models.CharField(max_length=200,help_text="Adja meg a hiba cimet", default='')
	kapcsolattarto_email = models.EmailField(max_length=254, help_text="Ezen az emailen lesz tajekoztatva a hibajavitasrol")
	leiras = models.TextField(max_length=254)
	elharito = models.ForeignKey('Alkalmazott',blank=True, on_delete=models.SET_NULL, null=True)

	hiba_allapot = (
		('e', 'Elkuldve'),
		('f', 'Fogadva'),
		('h', 'Elharitva'),
		('v', 'Visszaigazolva'),
    )
	statusz = models.CharField(max_length=1, choices=hiba_allapot, blank=True, default='e', help_text='Hiba Allapot')
	
	def __str__(self):
		"""
		String for representing the Model object.
		"""
		return str(self.id) + " -- " + self.nev + " -- " + self.cim 

	def get_absolute_url(self):
		"""
		Returns the url to access a particular book instance.
		"""
		return reverse('hibareszletei', args=[str(self.id)])

	def __init__(self, *args, **kwargs):
		super(Hiba, self).__init__(*args, **kwargs)
		self.__original_statusz = self.statusz
		self.__original_elharito = self.elharito

	def save(self, force_insert=False, force_update=False, *args, **kwargs):
		if self.statusz != self.__original_statusz:
			send_mail('Hibabejelenteset fogadtuk','A hiba elharitassal kapcsolatban tovabbi ertesiteseket fog kapni','tesztemailepuzbau@gmail.com',['minipek.gn@gmail.com'],fail_silently=False,)
		if self.elharito != self.__original_elharito:
			send_mail('Hibabejelenteset fogadtuk','A hiba elharitassal kapcsolatban tovabbi ertesiteseket fog kapni','tesztemailepuzbau@gmail.com',['minipek.gn@gmail.com'],fail_silently=False,)
		super(Hiba, self).save(force_insert, force_update, *args, **kwargs)
		self.__original_statusz = self.statusz




class Alkalmazott(models.Model):
	id = models.AutoField(primary_key=True)
	nev = models.CharField(max_length=200,help_text="Alkalmazott neve", default='Teszt Elek')
	email = models.EmailField(max_length=254,help_text="Alkalmazott email cime", default='tesztelek@gmail.com')
	telefonszam = models.CharField(max_length=200,help_text="Alkalmazott telefonszama", default='+36201234567')
	cim = models.CharField(max_length=200,blank=True ,help_text="Alkalmazott cime", default='1074 Budapest Teszt Elek utca 22')

	def __str__(self):
		"""
		String for representing the Model object.
		"""
		return str(self.id) + " -- " + self.nev

class ErtesitettAlkalmazott(models.Model):
    alkalmazott = models.ForeignKey('Alkalmazott', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.alkalmazott.id) + " -- " + self.alkalmazott.nev


class Visszajelzes(models.Model):
    hiba = models.ForeignKey('Hiba', on_delete=models.SET_NULL, null=True)
    uzenet = models.TextField()

    def __str__(self):
        return str(self.hiba.id) + " -- " + self.uzenet

    def save(self):
        send_mail('Hibabejelenteset fogadtuk','A hiba elharitassal kapcsolatban tovabbi ertesiteseket fog kapni','tesztemailepuzbau@gmail.com',['minipek.gn@gmail.com'],fail_silently=False,)
        super(Visszajelzes, self).save() # Call the "real" save() method    