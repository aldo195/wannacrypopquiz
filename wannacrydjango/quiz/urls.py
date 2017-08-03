from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
   # url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),

    # Steps of drill #1: Basic Inventory
    url(r'^drill/1/1/$', views.drill1_step1, name='drill1_step1'),

    url(r'^drill/1/2/$', views.drill1_step2, name='drill1_step2'),

    url(r'^drill/1/3/$', views.drill1_step3, name='drill1_step3'),

    url(r'^drill/1/4/$', views.drill1_step4, name='drill1_step4'),

    url(r'^drill/1/5/$', views.drill1_step5, name='drill1_step5'),

    url(r'^drill/1/6/$', views.drill1_step6, name='drill1_step6'),

    url(r'^drill/1/results/$', views.drill1_results, name='drill1_results'),
]
