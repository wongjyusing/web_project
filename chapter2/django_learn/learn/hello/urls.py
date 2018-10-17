from django.urls import path,re_path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    re_path('hello/(?P<name>[\w-]+)/',views.hello),
    re_path('hi/(?P<name>[\w-]+)/',views.hi,)

]
