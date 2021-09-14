from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('<str:pagename>/', views.index, name='index'),
    path('', views.index, name='index'),
]


 # path('search/', SearchResultsView.as_view(), name='search_results'),