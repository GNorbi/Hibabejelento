from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^hibabejelentes/$', views.hiba_bejelentes, name='hibabejelentes'),
	url(r'^hibalista/$', views.HibaListaView.as_view(), name='hibalista'),
	url(r'^(?P<pk>\d+)$', views.HibaReszleteiView.as_view(), name='hibareszletei'),
]
