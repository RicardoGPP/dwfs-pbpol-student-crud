from django.urls import reverse_lazy
from django.views import generic
from rest_framework import viewsets
from .models import Aluno
from .forms import AlunoForm
from .serializers import AlunoSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class AlunoListView(generic.ListView):
    template_name = "listar.html"
    model = Aluno
    context_object_name = "alunos"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class AlunoCreateView(generic.CreateView):
    template_name = "criar.html"
    model = Aluno
    form_class = AlunoForm
    success_url = reverse_lazy("app:index")

class AlunoUpdateView(generic.UpdateView):
    template_name = "editar.html"
    model = Aluno
    fields = "__all__"
    context_object_name = "aluno"
    success_url = reverse_lazy("app:index")

class AlunoDeleteView(generic.DeleteView):
    template_name = "excluir.html"
    model = Aluno
    fields = "__all__"
    context_object_name = "aluno"
    success_url = reverse_lazy("app:index")