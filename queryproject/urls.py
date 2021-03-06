from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'queryproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	(r'^query/$','query.views.query'),
	(r'^query/res$','query.views.res'),
    ( r'^js/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': '/home/danmeng/zzq/queryproject/queryproject/resources/js/' }
    ),
 
    ( r'^css/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': '/home/danmeng/zzq/queryproject/queryproject/resources/css/' }
    ),
 
    ( r'^images/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': '/home/danmeng/zzq/queryproject/queryproject/resources/images/' }
    ),

)
