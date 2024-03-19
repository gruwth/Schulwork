import re
import sys

def apple_maps_to_google_maps(apple_maps_url):
    # Extracting coordinates from the Apple Maps URL
    match = re.search(r'll=([0-9.-]+),([0-9.-]+)', apple_maps_url)
    
    if match:
        # Extracting latitude and longitude
        latitude = match.group(1)
        longitude = match.group(2)
        
        # Constructing the Google Maps URL
        google_maps_url = f'https://www.google.com/maps/search/?api=1&query={latitude},{longitude}'
        
        return google_maps_url
    else:
        print("Error: Unable to extract coordinates from the Apple Maps URL.")
        return None

# Example usage
location = sys.argv[1]
apple_maps_url = f"{location}"
google_maps_url = apple_maps_to_google_maps(apple_maps_url)

if google_maps_url:
    print("Google Maps URL:", google_maps_url)
