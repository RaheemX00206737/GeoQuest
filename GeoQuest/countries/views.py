from django.views.generic import ListView
from countries.models import Country
from django.shortcuts import render
from .forms import CountrySearchForm


# Create your views here.
def home(request):
    form = CountrySearchForm(request.GET or None)  # Bind form with GET data if available
    countries = Country.objects.all() 
    if 'q' in request.GET:  # Check if there's a search query
        query = request.GET.get('q')
        countries = Country.objects.filter(name__icontains=query)
    return render(request, 'home.html', {'form': form, 'countries': countries})

class SearchResultsListView(ListView):
    model = Country
    template_name = 'search_results.html'  # Template for rendering results
    context_object_name = 'countries'  # Name used in the template

    def get_queryset(self):
        query= self.request.GET.get('q')
        if query:
            return Country.objects.filter(name__icontains=query)
        return Country.objects.all() # Return all countries if no query is