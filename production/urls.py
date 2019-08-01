from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name="index"),
    path ('catalog', views.index, name="catalog"),
    path ('<int:product.id>/', views.product_detail_view, name="detail"),
    path ('event', views.event, name="event"),


    path ('demand', views.demand, name="demand"),
    path ('contact', views.contact, name="contact"),
    path ('contactme', views.contact, name="contactme")

]