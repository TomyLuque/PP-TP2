from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('captcha/', include('captcha.urls')),
    path('oficinas/', include(('oficinas.urls', 'oficinas'), namespace='oficinas')),
    path('', include(('personas.urls', 'personas'), namespace='personas')),
]
