from django.urls import path

from . import views

app_name = "flowers"
urlpatterns = [
    path("all", views.plants_list, name="plants-all"),
    path('add', views.plants_add, name="add"),
    path('delete', views.plants_delete, name="delete"),
    path(r'delete/(?P<pk>\d+)', views.plants_delete_pk, name="delete"),
    path('', views.home, name="home"),
]