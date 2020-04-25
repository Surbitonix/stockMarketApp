from django.urls import path
from . import views

urlpatterns = [
	path('',views.home,name='home'),
	path('aboutus/',views.about,name='about'), 
	path('add_stock.html',views.add_stock,name='add_stock'),
	path('delete/<item_id>',views.delete_stock,name="delete"),
	path('remove_stock.html',views.remove_stock,name="remove_stock"),

]