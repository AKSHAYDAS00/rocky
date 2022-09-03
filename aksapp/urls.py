from django.urls import path

from aksapp import admin, views

urlpatterns = [
    path('appu/',views.athena),
    path('athira/',views.car),
    path('jinu/',views.ambu),
]