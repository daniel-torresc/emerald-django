"""
URL configuration for emerald project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path(route='admin/', view=admin.site.urls),
    path(route='api/docs/schema/', view=SpectacularAPIView.as_view(), name='schema'),
    path(route='api/docs/schema/ui', view=SpectacularSwaggerView.as_view(), name='schema_ui'),

    path(route='api-auth/', view=include('rest_framework.urls', namespace='rest_framework')),
    path(route='api/', view=include("movements.urls")),
    # path(route='', view=RedirectView.as_view(url='movements/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
