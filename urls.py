from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^default/','app_demo.views.all_default'),
	(r'^auxiliar/','app_demo.views.all_auxiliar'),
	(r'^salvar_def/','app_demo.views.save_default'),
	(r'^salvar_aux/','app_demo.views.save_auxiliar'),

)
