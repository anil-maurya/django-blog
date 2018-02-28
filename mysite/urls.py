from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
# from django.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
]
