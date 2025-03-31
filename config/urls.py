from django.contrib import admin
from django.urls import include, path
from django.views.generic import *
import app.views as views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.IndexView.as_view(), name='index'),
    path('conversao/', views.ConversaoView.as_view(), name='conversao'),
    path('conversaoPLA/', views.ConversaoPLAView.as_view(), name='PLA'),
    path('conversaoVID/', views.ConversaoVIDView.as_view(), name='VID'),
    path('conversaoIMG/', views.ConversaoIMGView.as_view(), name='IMG'),
    path('historico/', views.HistoricoView.as_view(), name='historico'),
    path('ajuda/', views.AjudaView.as_view(), name='ajuda'),
    path('feed/', views.FeedView.as_view(), name='feed'),
    path('meu_feedback/', views.MFeedView.as_view(), name='meu_feedback'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('deleteHistorico/<int:id>/', views.DeleteHistorico.as_view(), name='deleteHistorico'),
    path('deleteFeedback', views.FeedbackDeleteView.as_view(), name='deleteFeedback'),
    path('gerenciar/', views.GerenciarView.as_view(), name='gerenciar'),
]