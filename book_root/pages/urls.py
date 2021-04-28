from django.urls import path
from . import views

urlpatterns = [
    path('<str:pagename>/', views.index, name='index'),
    path('', views.index, name='index'),
]

#  path('home/', views.home, name='home'),
 # path('search/', SearchResultsView.as_view(), name='search_results'),