from django.conf.urls import url, include
from interviewTest.views import home, complete_sign_up, profile, other_info

urlpatterns = [
    url(r'^complete/$', complete_sign_up, name="complete_signup"),
    url(r'^profile/$', profile, name="profile"),
    url(r'^other_info/$', other_info, name="other_info"),
]
