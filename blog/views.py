##from django.shortcuts import render

# Create your views here.

from django.views import generic
from . import models


class BlogIndex(generic.ListView):
  queryset = models.Entry.objects.published()
  template_name = "home.html"
  paginate_by = 3
  
  
##class BlogDetail(models.Model):
class BlogDetail(generic.DetailView):
  model = models.Entry
  template_name = "post.html"