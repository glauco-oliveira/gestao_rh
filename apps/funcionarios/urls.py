from django.urls import path
from .views import FuncionarioList, FuncionarioEdit


urlpatterns = [
    path('', FuncionarioList.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>/', FuncionarioEdit.as_view(), name='update_funcionarios'),
]
