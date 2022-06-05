def formatted_city_country(city, country,  population=''):
    """Function to formate the city and the country"""
    if population:
        formatted = f"{city.title()}, {country.title()} - population {population}"
    else:
        formatted = f"{city.title()}, {country.title()}"
    return formatted
