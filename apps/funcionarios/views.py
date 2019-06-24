from django.views.generic import ListView, UpdateView
from .models import Funcionario


class FuncionarioList(ListView):
    model = Funcionario

#Lista apenas usuários da mesma empresa do usuário logado
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)

class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']
