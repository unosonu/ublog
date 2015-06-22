from django.db import models
# Create your models here.
from django.core.urlresolvers import reverse

class Tag(models.Model):
  slug = models.SlugField(max_length=200, unique=True)
  
  def __str__(self):
    return self.slug  ##String representation to the slug field
  
  def get_absolute_url(self):
    return reverse("tag_index", kwargs={"slug": self.slug})  ##modification to get url for the tag
  

class EntryQuerySet(models.QuerySet):
  def published(self):
    return self.filter(publish = True)  ## To filter from the posts 

class Entry(models.Model):
  title = models.CharField(max_length = 200)
  body = models.TextField()
  slug = models.SlugField(max_length = 200, unique = True)
  publish = models.BooleanField(default = True)
  created = models.DateTimeField(auto_now_add = True)
  modified = models.DateTimeField(auto_now = True)
  
  tags = models.ManyToManyField(Tag) ##many to many relationship between tag and models
  
  objects = EntryQuerySet.as_manager()
  
  def __str__(self):
    return self.title  ##For better string handling
    
  def get_absolute_url(self):
    return reverse("entry_detail", kwargs = {"slug": self.slug})
    

  class Meta:
    verbose_name = "Blog Entry"
    verbose_name_plural = "Blog Entries"
    ordering = ["-created"]
    