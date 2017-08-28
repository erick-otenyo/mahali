
from django.conf.urls import url
from django.contrib import admin
from mahali import views

urlpatterns = [
    url(r'^$', views.home,name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^mahali/', views.mahali,name='mahali'),
]
