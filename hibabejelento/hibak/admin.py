from django.contrib import admin
from .models import Hiba, Alkalmazott, ErtesitettAlkalmazott, Visszajelzes
from django.core.mail import send_mail
from django.forms import ModelForm
admin.site.register(Hiba)
admin.site.register(Alkalmazott)
admin.site.register(ErtesitettAlkalmazott)
admin.site.register(Visszajelzes)
