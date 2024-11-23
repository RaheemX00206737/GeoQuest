from django.urls import path
from .views import home ,SearchResultsListView

urlpatterns = [
    path('', home, name='home'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
]