from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls import url
from api import views

urlpatterns = [
  path('admin/', admin.site.urls),
  url(r'^$', TemplateView.as_view(template_name='index.html')),
  path('api', views.names),
  path('accounts/', include('registration.backends.simple.urls')),
]