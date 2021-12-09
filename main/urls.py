from django.urls import path
from django.views.generic.base import TemplateView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('search',views.search,name='search'),
    path('logout',views.logout,name='logout'),
    path('post',views.post,name='post'),
    path('pdetails/<int:id>',views.pdetails,name='pdetails'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('changepassword',views.changepassword,name='changepassword'),
    path('reset_password',auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),name="reset_password"),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name="password_reset_confirm"),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete'),name="password_reset_complete"),







]