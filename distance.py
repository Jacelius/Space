import ephem
import geocoder

# Get the current location using IP address
g = geocoder.ip('me')

# Extract the latitude and longitude
latitude = g.lat
longitude = g.lng

print(f"Your current location is: ({latitude:.2f}, {longitude:.2f})")

# Set up the observer (in this case, Earth)
observer = ephem.Observer()
observer.lat = latitude
observer.lon = longitude
observer.name = 'Earth'

# Set the date to now
observer.date = ephem.now()

# Set up the target (in this case, Mars)
mars = ephem.Mars()

# Compute the distance between Earth and Mars
mars.compute(observer)
distance_au = mars.earth_distance

# Convert the distance to kilometers
km_per_au = 149597870.7
distance_km = distance_au * km_per_au

# Format the kilometer value with underscores
formatted_km = "{:,.3f}".format(distance_km)

print(f"The current distance from Earth to Mars is {distance_au:.2f} AU, or {formatted_km} kilometers.")
