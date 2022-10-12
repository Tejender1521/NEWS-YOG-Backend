
from mordecai import Geoparser  # may take a little to load
from pprint import pprint


# Create geoparser and parse example text
geo = Geoparser()
text = input("Enter your text: ")
result = geo.geoparse(text)

# Print the geoparsed text results
pprint(result)