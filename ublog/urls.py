from django.conf.urls import include, url
from django.contrib import admin

##initial content in the file
'''
urlpatterns = [
    # Examples:
    # url(r'^$', 'ublog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
'''
##Doesn't work
'''
urlpatterns = patterns(
  '',
  url(r'^admin/', include(admin.site.urls)),
  url(r'^markdown/', inclue("django_markdown.urls")),
  )
'''

urlpatterns = [
  
  url(r'^admin/', include(admin.site.urls)),
  url(r'^markdown/', include("django_markdown.urls")),
  url(r'^',include('blog.urls')),
  ]