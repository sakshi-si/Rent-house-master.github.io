from django.urls import path
# from django.conf.urls import path
from django.urls import re_path as url
from django.contrib.auth import logout
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =[
	path('profile', views.profile, name= 'profile'),
	path('post',views.post, name = 'post'),
	
	path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
	path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
	path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
	path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]
