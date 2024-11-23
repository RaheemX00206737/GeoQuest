#Script to add the countries
import os 
import django

#django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GeoQuest.settings')
django.setup()

from countries.models import Country

#workhuman country data
countries = [
    "Albania", 
    "Andorra ",
    "Australia",
    "Brazil",
    "Belgium", 
    "Canada",
    "China",
    "France",
	"Germany",
	"India",
	"Indonesia",
	"Ireland",
	"Italy",
	"Japan", 
	"Kenya",
	"Luxembourg",
	"Mexico",
	"New Zealand",
	"Nigeria",
	"Portugal",
	"Russia", 
	"South Africa", 
	"South Korea",
	"Spain",
	"Sweden",
	"Thailand",
	"Ukraine",
	"United Kingdom",
	"United States of America",
	"Vietnam",
	"Zambia",
]

#adding the countries to the database
for country_name in countries:
    country, created = Country.objects.get_or_create(name=country_name)
    if created:
        print(f"Added: {country_name}")
    else:
        print(f"This country already exists: {country_name}")

print("Done setting countries")