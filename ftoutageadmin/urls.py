"""FT-Outage-Site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


# Use include() to add URLS from the OutageManagement application and authentication system
from django.conf.urls import include


urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

admin.site.site_header = _("Outage Administration")
admin.site.site_title = _("FT Outage Admin")


urlpatterns += [
    url(r'^OutageManagement/', include( 'OutageManagement.urls' ) ),
]


# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    url('^accounts/', include('django.contrib.auth.urls')),
]


#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
urlpatterns += [
    url(r'^', RedirectView.as_view(url='/OutageManagement/', permanent=True)),
]