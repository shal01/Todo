from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('update/<int:pk>/',views.update,name='update_task'),
    path('delete/<int:pk>',views.deleteView,name='delete_task'),
]