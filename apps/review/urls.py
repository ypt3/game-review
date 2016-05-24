from django.conf.urls import patterns, url
from apps.review import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'register$', views.register, name='register'),
    url(r'login$', views.login, name="login"),
    url(r'dashboard$', views.dashboard, name='dashboard'),
    url(r'logout$', views.logout, name='logout'),
    url(r'add$', views.add, name="add"),
    url(r'add_review$', views.add_review, name='add_review'),
    url(r'^review_add/(?P<game_id>\d+)/$', views.review_add, name="review_add"),
    url(r'^games/(?P<game_id>\d+)/$', views.show_game, name="show_game"),
    url(r'^games/(?P<game_id>\d+)/delete$', views.delete_game, name="delete_game"),
	url(r'^users/(?P<user_id>\d+)/$', views.show_user, name="show_user"),
)
