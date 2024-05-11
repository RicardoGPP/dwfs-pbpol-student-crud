from django.urls import path, include
from rest_framework import routers
from .views import AlunoViewSet

router = routers.DefaultRouter()
router.register('alunos', AlunoViewSet, basename='aluno')

urlpatterns = [
    path('', include(router.urls))
]