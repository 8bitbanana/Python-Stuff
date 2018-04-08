import json, imageio, glob

from tqdm import tqdm
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# The file to get the Google Location History from
LOCATION_FILE = "EthanHistory.json"

# The overhead to give the map size (default 0.05)
MAP_SIZE_OVERHEAD = 0.05
CHUNK_SIZE = 50

# https://stackoverflow.com/questions/2130016/splitting-a-list-into-n-parts-of-approximately-equal-length/2136090
def chunks(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out

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

    longs = list(chunks(longs, CHUNK_SIZE))
    lats = list(chunks(lats, CHUNK_SIZE))

    print("Plotting points...")
    prev_lines = None
    xs = []
    ys = []
    for i in range(0,len(lats)):
        print("CHUNK {}/{} SIZE {}".format(i+1,len(lats),len(lats[i])))
        m.drawcoastlines()
        m.drawmapboundary(fill_color='aqua')
        m.fillcontinents(color='green', lake_color='aqua')
        if xs != [] and ys != []:
            plt.plot(xs, ys, 'ro', markersize=1, linestyle="solid", linewidth=0.5)
        xs = []
        ys = []
        for x in range(0, len(lats[i])): # Convert the lats and longs to plottable x/y coordinates
            x, y = m(longs[i][x], lats[i][x])
            xs.append(x)
            ys.append(y)
        if prev_lines != None:
            # nuke
            l = prev_lines.pop(0)
            l.remove()
            del l
        prev_lines = plt.plot(xs,ys, 'co', markersize=1, linestyle="solid", linewidth=0.5)
        plt.savefig('{}.png'.format(i+1), dpi=600)
    plt.close()

def imgsToGif():
    filenames_unsorted = glob.glob("*.png")
    filenames = []
    for x in range(1, len(filenames_unsorted)+1):
        filenames.append("{}.png".format(x))
    print(filenames)
    with imageio.get_writer('plot.gif', mode='I') as writer:
        for filename in tqdm(filenames):
            image = imageio.imread(filename)
            writer.append_data(image)

if __name__ == "__main__":
    #main()
    imgsToGif()