from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('register',views.register, name='register'),
    path('login',views.my_login, name='login'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('logout',views.my_logout, name='logout'),
    path('create-record',views.create_record, name='create-record'),
    path('view/<int:id>' , views.view_record,name='view_record'),
    path('update/<int:id>' , views.update,name='update'),
    path('delete/<int:id>' , views.delete,name='delete'),
    path('search',views.search, name='search'),
]
