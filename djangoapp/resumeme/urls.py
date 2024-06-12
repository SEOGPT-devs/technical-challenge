from django.urls import path
from resumeme.views import index

app_name = 'resumeme'

urlpatterns = [
    path('', index, name='index'),
]
