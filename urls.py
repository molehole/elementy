from django.conf.urls import url
from . import views as elementy

urlpatterns = [
    url(r'^$', elementy.index, name='index'),
    url(r'^update/$', elementy.update, name='update'),
    url(r'^import_danych/$', elementy.import_danych, name='import_danych'),
]