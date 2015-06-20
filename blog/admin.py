from django.contrib import admin

# Register your models here.
from . import models
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField


'''
class EntryAdmin(admin.ModelAdmin):
  list_display = ("title", "created")
  prepopulated_fields = {"slug": ("title",)}
'''

class EntryAdmin(MarkdownModelAdmin):
  list_display = ("title", "created")
  prepopulated_fields = {"slug": ("title",)}
  
  ##workaround for python 2.x
  formfield_overrides = {TextField:  {'widget': AdminMarkdownWidget}}


admin.site.register(models.Entry, EntryAdmin)
admin.site.register(models.Tag)