from django.urls import path
from . import views
app_name="test_css"

urlpatterns=[
    path('',views.index),
]