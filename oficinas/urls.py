from django.urls import path
from . import views

urlpatterns = [
    path('', views.OficinaListView.as_view(), name='listado'),
    path('buscar/', views.buscar, name='buscar'),
    path('crear/', views.OficinaCreateView.as_view(), name='crear'),
    path('<int:pk>/', views.OficinaDetailView.as_view(), name='detalle'),
    path('<int:pk>/editar/', views.OficinaUpdateView.as_view(), name='editar'),
    path('<int:pk>/eliminar/', views.OficinaDeleteView.as_view(), name='eliminar'),
    path('carga-masiva/', views.carga_masiva_oficinas, name='carga_masiva'),
]
