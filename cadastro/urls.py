from django.urls import path
from . import views


urlpatterns = [
    path('unidade', views.unidade_read, name='unidade-read'),
    path('unidade/cadastrar', views.cadastrar_unidade, name='cadastrar-unidade'),
    path('unidade/editar/<id>/', views.editar_unidade, name='editar-unidade'),
    # path('detalhar/<id>/', views.todo_detail, name='todo'),
    # path('deletar/<id>/', views.todo_delete, name='todo-delete'),
]