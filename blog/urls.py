from django.conf.urls import patterns,url
from . import views, feed


##for the purpose of showing favicon
#from django.contrib.staticfiles.storage import staticfiles_storage
#from django.views.generic.base import RedirectView

urlpatterns = patterns(
  '',
  
  # url(
   #     r'^favicon.ico$',
    #    RedirectView.as_view(
     #       url=staticfiles_storage.url('favicon.ico'),
      #      permanent=False),
       # name="favicon"),
  
  
  url(r'^feed/$', feed.LatestPosts(), name="feed"),
  
  url(r'^$',views.BlogIndex.as_view(),name="index"),
  url(r'^entry/(?P<slug>\S+)?$', views.BlogDetail.as_view(), name="entry_detail"),
  url(r'^tag/(?P<slug>\S+)?$', views.TagIndex.as_view(), name = "tag_index"),
 
  
  ##url(r'^entry/(?P<slug>[-\w\d]+)/', views.BlogDetail.as_view(), name="entry_detail"),
  )



'''
urlpatterns = [
  url(r'^feed/$', feed.LatestPosts(), name="feed"),
  url(r'^$',views.BlogIndex.as_view(),name="index"),
  url(r'^(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
  ]
 '''
