from django.urls import path
from fourth_app import views

urlpatterns=[
    path('',views.form_views,name='form_views')
]