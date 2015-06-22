from django.conf.urls import include, url, patterns
from django.contrib import admin

##for the purpose of showing favicon
#from django.contrib.staticfiles.storage import staticfiles_storage
#from django.views.generic.base import RedirectView


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

urlpatterns = patterns(
  '',
  ##for the purpose of showing favicon
  #url(r'^favicon.ico$', RedirectView.as_view(
#	    url=staticfiles_storage.url('favicon.ico'),
 #           permanent=False),
  #      name="favicon"),
	
  url(r'^admin/', include(admin.site.urls)),
  url(r'^markdown/', include("django_markdown.urls")),
  url(r'^',include('blog.urls')),
  )