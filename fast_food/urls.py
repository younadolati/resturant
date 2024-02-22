from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
urlpatterns = [
    path('fast_food/',views.show,name="fast_food"),
    path('about_us/',views.show1,name="about_us"),

]
urlpatterns+=staticfiles_urlpatterns()