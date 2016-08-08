from django.conf.urls import url

from . import views

urlpatterns = [
    ('load_from_file', views.upload_data),
]
# url(r'upload_samples:(?P<expid>[0-9]*)$', views.upload_samples),
#                url(r'upload_samples_report:(?P<expid>[0-9]*)$', views.parse_samples_and_report),]