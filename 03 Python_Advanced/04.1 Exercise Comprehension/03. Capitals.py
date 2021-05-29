countries = [c for c in input().split(", ")]
capitals = [cap for cap in input().split(", ")]
[print(f"{country} -> {capital}") for country, capital in (list(zip(countries, capitals)))]