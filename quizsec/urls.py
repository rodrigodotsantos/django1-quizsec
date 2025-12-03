from django.contrib import admin
from django.urls import path, include
from core import views as core_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # Em urls.py
    path('logout/', auth_views.LogoutView.as_view(
        template_name='logout_confirm.html', 
        next_page='home'
    ), name='logout'),
    path('signup/', core_views.signup_view, name='signup'),
    path('', core_views.home, name='home'),
    path('quiz/', core_views.play_quiz, name='play_quiz'),
    path('gestao/perguntas/', core_views.question_list_admin, name='admin_question_list'),
    path('gestao/perguntas/nova/', core_views.question_create_admin, name='admin_question_create'),
    path('gestao/usuarios/', core_views.users_performance_admin, name='admin_users_performance'),
    path('debug/', core_views.debug_auth, name='debug_auth'),
]
