# flake8: noqa
"""
djangoproj URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('djangoapp/', include('djangoapp.urls')),

    # Home page
    path('', TemplateView.as_view(template_name="Home.html"), name='home'),

    # About page
    path('about/', TemplateView.as_view(template_name="About.html"), name='about'),

    # Contact page
    path('contact/', TemplateView.as_view(template_name="Contact.html"), name='contact'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
