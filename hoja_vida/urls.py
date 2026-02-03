from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('curriculum.urls')),
]

# Servir archivos media en desarrollo y producción
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# ----------------------------------- 

# Crear archivo curriculum/urls.py
from django.urls import path
from . import views

app_name = 'curriculum'

urlpatterns = [
    path('', views.perfil_profesional, name='perfil_profesional'),
    path('experiencia-laboral/', views.experiencia_laboral, name='experiencia_laboral'),
    path('reconocimientos/', views.reconocimientos, name='reconocimientos'),
    path('cursos-realizados/', views.cursos_realizados, name='cursos_realizados'),
    path('productos-academicos/', views.productos_academicos, name='productos_academicos'),
    path('productos-laborales/', views.productos_laborales, name='productos_laborales'),
    path('venta-garage/', views.venta_garage, name='venta_garage'),
    path('api/configuracion/', views.actualizar_configuracion, name='actualizar_configuracion'),
    path('api/generar-pdf/', views.generar_pdf, name='generar_pdf'),
]
