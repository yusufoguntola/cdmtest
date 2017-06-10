from django.conf.urls import url

from w_admin import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='admin_home'),
    url(r'^home/$', views.verify_user, name='perform_operation'),
]
