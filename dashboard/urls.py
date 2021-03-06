from django.conf.urls import url
from .views import dashboard, assign_user_to_campaign, start_tasks


urlpatterns = [
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^dashboard/assign_user_to_campaign/(?P<pk>\d+)/$', assign_user_to_campaign, name='assign_user_to_campaign'),
    url(r'^start_tasks/(?P<pk>\d+)/$', start_tasks, name='start_tasks'),
]
