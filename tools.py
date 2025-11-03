import requests
from datetime import datetime
import wikipedia  # Changed from wikipediaapi
import pint
# Initialize libraries

# Initialize libraries
ureg = pint.UnitRegistry()  # For unit conversions

# Existing Tool 1: Web Search using DuckDuckGo
def web_search(query):
    url = f"https://api.duckduckgo.com/?q={query}&format=json&no_html=1&skip_disambig=1"
    response = requests.get(url)
    data = response.json()
    if 'AbstractText' in data and data['AbstractText']:
        return data['AbstractText']
    elif 'RelatedTopics' in data and data['RelatedTopics']:
        return data['RelatedTopics'][0].get('Text', 'No results found.')
    return "No search results found."

# Existing Tool 2: Calculator for simple math
def calculate(expression):
    try:
        result = eval(expression, {"__builtins__": None}, {})
        return str(result)
    except Exception as e:
        return f"Error in calculation: {str(e)}"

# Existing Tool 3: Get current time
def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Updated Tool 4: Wikipedia Search (using wikipedia library)
def wikipedia_search(query):
    try:
        page = wikipedia.page(query)
        return page.summary[:500] + "..."  # Limit to 500 chars for brevity
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Multiple results found: {e.options[:5]}..."  # Show first 5 options
    except wikipedia.exceptions.PageError:
        return "No Wikipedia page found for that query."
   


# New Tool 5: Weather Lookup (requires free API key from openweathermap.org)
def get_weather(city):
    api_key = "Weather_API_Key"  # Replace with your free key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        return f"Weather in {city}: {temp}°C, {desc}."
    return "Weather data not available. Check your API key or city name."

# New Tool 6: Unit Conversion
def convert_units(value, from_unit, to_unit):
    try:
        quantity = ureg.Quantity(float(value), from_unit)
        converted = quantity.to(to_unit)
        return f"{value} {from_unit} = {converted.magnitude} {converted.units}"
    except Exception as e:
        return f"Error in conversion: {str(e)}. Example: value=100, from_unit='meters', to_unit='feet'."
    
