from django.urls import path, include
from rest_framework import routers
from .views import AlunoViewSet, AlunoListView, AlunoCreateView, AlunoUpdateView, AlunoDeleteView

app_name = 'app'

router = routers.DefaultRouter()
router.register('alunos', AlunoViewSet, basename='aluno')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', AlunoListView.as_view(), name='index'),
    path('criar', AlunoCreateView.as_view(), name='criar'),
    path('editar/<pk>', AlunoUpdateView.as_view(), name='editar'),
    path('excluir/<pk>', AlunoDeleteView.as_view(), name='excluir')
]