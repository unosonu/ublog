##from django.shortcuts import render

# Create your views here.

from django.views import generic
from . import models
from blog.models import Tag,Entry


class BlogIndex(generic.ListView):
  queryset = models.Entry.objects.published()
  template_name = "home.html"
  paginate_by = 3
  
  
##class BlogDetail(models.Model):
class BlogDetail(generic.DetailView):
  model = models.Entry
  template_name = "post.html"
  
  
class TagIndex(generic.ListView):
  template_name = 'home.html'
  paginated_by = 3
  
  def get_queryset(self):
    slug = self.kwargs['slug']
    tag = Tag.objects.get(slug=slug)
    results = Entry.objects.filter(tags = tag)
    return results