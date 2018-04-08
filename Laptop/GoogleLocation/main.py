import json

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# The file to get the Google Location History from
LOCATION_FILE = "EthanHistory.json"

# The overhead to give the map size (default 0.05)
MAP_SIZE_OVERHEAD = 0.05


def parseFile(filename):
    f = open(filename)
    raw = f.read()
    parsed = json.loads(raw)
    return parsed['locations']

"""
The data is stored as a list of dictionaries under the "locations" key.
Each dictionary has the following keys:
'timestampMs' - Timestamp in ms since 1/1/70
'latitudeE7' - Location coords - normally a decimal but converted to an integer
'longitudeE7' - ditto
'accuracy' - GPS accuracy I guess
"""

def main():
    print("Parsing location file...")
    locationData = parseFile(LOCATION_FILE)
    lats = []
    longs = []
    maximum_lat = -10000 # -10000 and 10000 are impossible values (I can't use null)
    maximum_long = -10000
    minimum_lat = 10000
    minimum_long = 10000

    print("Collecting coordinates...")
    for entry in locationData:
        lat = entry["latitudeE7"] / 1E7 # Convert to decimal coordinates
        long = entry["longitudeE7"] / 1E7
        if lat > maximum_lat: maximum_lat = lat # Get the minimum and maximum of each value to work out
        if lat < minimum_lat: minimum_lat = lat # the map size
        if long > maximum_long: maximum_long = long
        if long < minimum_long: minimum_long = long
        lats.append(lat)
        longs.append(long)

    assert maximum_lat != 10000
    assert maximum_long != 10000
    assert minimum_lat != 10000
    assert minimum_long != 10000
    assert len(lats) == len(longs)

    print("Generating map...")

    # A map size overhead of 5% each side
    lat_overhead = (maximum_lat - minimum_lat) / (1/MAP_SIZE_OVERHEAD)
    long_overhead = (maximum_long - minimum_long) / (1/MAP_SIZE_OVERHEAD)
    fig = plt.figure(figsize=(8,8))
    m = Basemap(projection='merc', resolution='h',
                llcrnrlat=minimum_lat-lat_overhead,
                llcrnrlon=minimum_long-long_overhead,
                urcrnrlat=maximum_lat+lat_overhead,
                urcrnrlon=maximum_long+long_overhead)
    m.drawcoastlines()
    m.drawmapboundary(fill_color='aqua')
    m.fillcontinents(color='green', lake_color='aqua')
    #m.bluemarble()

    print("Plotting on map...")
    xs = []
    ys = []
    for x in range(0, len(lats)): # Convert the lats and longs to plottable x/y coordinates
        x, y = m(longs[x], lats[x])
        xs.append(x)
        ys.append(y)
    plt.plot(xs,ys, 'ro', markersize=3, linestyle="solid", linewidth=1)
    plt.show()

if __name__ == "__main__":
    main()
