from django.urls import path
from . import views

app_name='app'

urlpatterns=[
    path('fastfood',views.fastfood,name='fastfood'),
    path('chinese',views.chinese,name='chinese')
]