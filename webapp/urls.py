from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('info_login/', views.info_login, name="info_login"),
    path('go_t/', views.go_t, name="go_t"),
    path('go_last/', views.go_last, name="go_last"),
    path('clear_seassion/', views.clear_seassion, name="clear_seassion"),
    path('update_session/', views.update_session, name="update_session"),

]