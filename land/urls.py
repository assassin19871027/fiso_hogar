from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.show_index, name='index'),
]
