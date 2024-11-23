from django.views.generic import ListView
from countries.models import Country
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')

class SearchResultsListView(ListView):
    model = Country
    template_name = 'search_results.html'  # Template for rendering results
    context_object_name = 'countries'  # Name used in the template

    def get_queryset(self):
        query= self.request.GET.get('q')
        if query:
            return Country.objects.filter(name__icontains=query)
        return Country.objects.all() # Return all countries if no query is