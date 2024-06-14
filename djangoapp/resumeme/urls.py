from django.urls import path
from resumeme.views import Index

app_name = 'resumeme'

urlpatterns = [
    path('', Index.as_view(), name='index'),
]
