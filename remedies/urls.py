from django.urls import path
from .import views

app_name = 'remedies'
urlpatterns=[
    path('Preventions/', views.prevention, name='prevention'),
    path('preventions/<slug:name>/', views.detail, name='detail'),
    path('fitness/', views.fitness_list, name='fitness_list'),
    path('fitness/<slug:category_slug>/', views.fitness_list,name='fitness_list_by_category')
]