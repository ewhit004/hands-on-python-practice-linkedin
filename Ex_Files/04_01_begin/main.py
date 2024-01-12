import requests
#if package is not installed type "pip install package_name" OR if 
#you're not using codespaces you may need to use the following command
#"python3 -m pip install package_name"

#".get(http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json)"
#takes data from a World Bank population API from a website
response = requests.get(
    "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json")

#20 items pulled from above API; the most recent 20 years are pulled
last_twenty_years = response.json()[1][:20]

#visual representation of 20 items (years & values) pulled denoted by "="
for year in last_twenty_years:
  display_width = year["value"] // 10_000_000
  #year with growing "=" indicating a growing population
  print(f'{year["date"]}: {year["value"]}', "=" * display_width)
