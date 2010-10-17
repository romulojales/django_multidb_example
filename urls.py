from django.conf.urls.defaults import *
import pug_demo
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^default/','pug_demo.views.all_default'),
	(r'^auxiliar/','pug_demo.views.all_auxiliar'),
	(r'^salvar_def/','pug_demo.views.save_default'),
	(r'^salvar_aux/','pug_demo.views.save_auxiliar'),

)
