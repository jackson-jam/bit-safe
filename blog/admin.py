from django.contrib import admin

# Register your models here.
from django.contrib import admin


#class ArticleAdmin(admin.ModelAdmin):
 #   list_display = ('id', 'title', 'created_time',)
  #  list_display_links = ('title',)
from django.contrib import admin
from blog.models import Vendors,Products,Customers,Trend,Shopping,Order,Classify,Appraise,Browse

# Register your models here.
admin.site.register([Vendors,Products,Customers,Trend,Shopping,Order,Classify,Appraise,Browse])