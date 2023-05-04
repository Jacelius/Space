import ephem
import geocoder
import completer
import curses 

celestial_object = curses.wrapper(completer.celestial_object_selection)
print("Celestial Object:", celestial_object)

observer_location = curses.wrapper(completer.observer_selection)
print("Observer Location:", observer_location)

# Get the current location using IP address
g = geocoder.ip('me')

# Extract the latitude and longitude
latitude = g.lat
longitude = g.lng

print(f"Your current location is: (\u03BB{latitude:.2f}, \u03A6{longitude:.2f})")

# Set up the observer (in this case, Earth)
observer = ephem.Observer()
observer.lat = latitude
observer.lon = longitude
observer.name = 'Earth'

# Set the date to now
observer.date = ephem.now()

match celestial_object:
    case "Moon":
        target = ephem.Moon()
    case "Mars":
        target = ephem.Mars()
    case _:
        raise ValueError("Invalid celestial object")

# Compute the distance between Earth and the target
target.compute(observer)

distance_au = target.earth_distance

# Convert the distance to kilometers
km_per_au = 149597870.7
distance_km = distance_au * km_per_au

# Format the kilometer value with underscores
formatted_km = "{:,.3f}".format(distance_km)

print(f"The current distance from Earth to Mars is {distance_au:.2f} AU, or {formatted_km} kilometers.")
