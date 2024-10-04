from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.main, name='index'),
    path('computer/',views.electronic,name='electronic'),
    path('jewellery/',views.jewellery,name='jewellery'),
    path('fashion/',views.fashion,name='fashion'),
    path("details/<int:id>", views.details, name='details'),
    path("addon/", views.addOn, name='addon')   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)