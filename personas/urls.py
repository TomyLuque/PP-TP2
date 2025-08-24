from django.urls import path
from . import views

urlpatterns = [
    path('', views.PersonaListView.as_view(), name='listado'),
    path('buscar/', views.buscar, name='buscar'),
    path('crear/', views.PersonaCreateView.as_view(), name='crear'),
    path('<int:pk>/', views.PersonaDetailView.as_view(), name='detalle'),
    path('<int:pk>/editar/', views.PersonaUpdateView.as_view(), name='editar'),
    path('<int:pk>/eliminar/', views.PersonaDeleteView.as_view(), name='eliminar'),
    path('carga-masiva/', views.carga_masiva_personas, name='carga_masiva'),
]
