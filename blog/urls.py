from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('misha/', views.misha),
    path('kirill_besish/', views.kirill_besish),

]