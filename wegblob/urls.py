from django.conf.urls import include, url
from django.contrib import admin
from wegblob.views import blog
from django.conf import settings
from django.contrib.staticfiles.views import serve 

urlpatterns = [
   # Examples:
   # url(r'^$', 'eg.views.home', name='home'),
   # url(r'^blog/', include('blog.urls')),

   url(r'^admin/',      include(admin.site.urls)),
   url(r'^$',           blog.blog_main,      name='blog.blog_main'      ),
   url(r'^blog/$',      blog.blog_main,      name="blog.blog_main"      ),
   url(r'^category/$',  blog.category,       name="blog.category"       ),
   url(r'^archive/$',   blog.archive,        name="blog.archive"        ),
   url(r'^categories/$',blog.categories,     name="blog.categories"     ),
   
]

if settings.DEBUG: 
   urlpatterns += [ url(r'^static/(?P<path>.*)$', serve), ]
