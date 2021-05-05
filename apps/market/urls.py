from . import views
from django.urls import path


urlpatterns = [
    path('get', views.get),
    path('post', views.post),
    path('update/<id>', views.update),
    path('delete/<id>', views.delete),
    path('login', views.login),
    path('', views.home),
    path('market', views.market)
]
