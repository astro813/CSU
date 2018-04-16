"""PEG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from . import views as views


urlpatterns = [
    # /
    url(r'^$', views.index, name='index'),
    # # /ACCOUNT_ID
    url(r'^(?P<pk>\d+)/$', views.index, name='tabs'),
    # /admin/
    # url(r'^admin/', admin.site.urls),
    # # /acct/
    # url(r'^acct/', include('Account.urls')),
    # # /dbr/
    # url(r'^dbr/', include('Debtor.urls')),
    # # /notes/
    # url(r'^notes/', include('Notes.urls')),
    # # /docs/
    # url(r'^docs/', include('Documents.urls')),
    # /clients/
    url(r'^clients/', include('Clients.urls')),
    # /fundings/
    url(r'^fundings/', include('Fundings.urls')),
    # /payoff/
    url(r'^payoff/', include('Payoff.urls')),

    # # /acct/ACCOUNT_ID
    # url(r'^(?P<pk>\d+)/acct/', include('Account.urls')),
    # # /dbr/ACCOUNT_ID
    # url(r'^(?P<pk>\d+)/dbr/', include('Debtor.urls')),
    # # /notes/ACCOUNT_ID
    # url(r'^(\d+)/notes/', include('Notes.urls')),
    # # /docs/ACCOUNT_ID
    # url(r'^(?P<fk>\d+)/docs/', include('Documents.urls')),

    url(r'^api/v1/', include('api.urls', namespace='api')),
]
