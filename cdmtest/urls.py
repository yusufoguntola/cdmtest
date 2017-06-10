"""cdmtest URL Configuration

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
from django.contrib import admin
from django.contrib.auth.views import logout, login
from django.conf import settings
from django.conf.urls.static import static

from interviewTest.views import home, complete_sign_up, profile, other_info

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name="home"),
    url(r'^logout/$', logout,{'next_page': '/'},  name='logout'),
    url(r'^login/$', login, {'template_name': 'interviewtest/login_form.html'}, name='login'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^account/', include('interviewTest.urls'), name="account"),
    url(r'^cdm-admin/', include('w_admin.urls', namespace="w_admin")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler400 = 'interviewTest.views.error_handler'
handler403 = 'interviewTest.views.error_handler'
handler404 = 'interviewTest.views.error_handler'
handler500 = 'interviewTest.views.error_handler'
