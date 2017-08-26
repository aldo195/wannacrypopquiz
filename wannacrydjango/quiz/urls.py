from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.drill_categories, name='drill_categories'),
    url(r'^$', views.intro, name='intro'),

    # Drill #1: Basic Workstation Inventory
    url(r'^drill/1/1/$', views.drill1_step1, name='drill1_step1'),

    url(r'^drill/1/2/$', views.drill1_step2, name='drill1_step2'),

    url(r'^drill/1/3/$', views.drill1_step3, name='drill1_step3'),

    url(r'^drill/1/5/$', views.drill1_step5, name='drill1_step5'),

    url(r'^drill/1/6/$', views.drill1_step6, name='drill1_step6'),

    url(r'^drill/1/results/$', views.drill1_results, name='drill1_results'),

    # Drill 2: Notorious Vulnerabilities
    url(r'^drill/notorious-vulnerabilities/1/$',
        views.drill_notorious_vulnerabilities_step1, name='drill_notorious_vulnerabilities_step1'),

    url(r'^drill/notorious-vulnerabilities/2/$',
        views.drill_notorious_vulnerabilities_step2, name='drill_notorious_vulnerabilities_step2'),

    url(r'^drill/notorious-vulnerabilities/3/$',
        views.drill_notorious_vulnerabilities_step3, name='drill_notorious_vulnerabilities_step3'),

    url(r'^drill/notorious-vulnerabilities/4/$',
        views.drill_notorious_vulnerabilities_step4, name='drill_notorious_vulnerabilities_step4'),

    url(r'^drill/notorious-vulnerabilities/5/$',
        views.drill_notorious_vulnerabilities_step5, name='drill_notorious_vulnerabilities_step5'),

    url(r'^drill/notorious-vulnerabilities/6/$',
        views.drill_notorious_vulnerabilities_step6, name='drill_notorious_vulnerabilities_step6'),

    url(r'^drill/notorious-vulnerabilities/results/$',
        views.drill_notorious_vulnerabilities_results, name='drill_notorious_vulnerabilities_results'),

    # Drill #3: Basic Network Monitoring
    url(r'^drill/bnm/1/$', views.drill_bnm_step1, name='drill_bnm_step1'),

    url(r'^drill/bnm/2/$', views.drill_bnm_step2, name='drill_bnm_step2'),

    url(r'^drill/bnm/3/$', views.drill_bnm_step3, name='drill_bnm_step3'),

    url(r'^drill/bnm/results/$', views.drill_bnm_results, name='drill_bnm_results'),

]
