# Data format
# {TRACK TITLE}=.={FREQUENCY}

log_filename = "spotify\\logfile.txt"
toadd_filename = "spotify\\toadd.txt"

def main():
    f = open(log_filename)
    log = f.read().splitlines()
    f.close()
    f = open(toadd_filename)
    toadd = f.read()
    f.close()

    # Split the log file into two lists, tracks and frequencies
    tracks = []
    frequencies = []
    for x in log:
        track, frequency = x.split("=.=")
        tracks.append(track)
        frequencies.append(int(frequency))

    # Try to find toadd in tracks.
    try:
        index = tracks.index(toadd)
    except ValueError: # Cannot find
        index = -1

    if index != -1: # It is already in the log, just increment the frequency
        frequencies[index] += 1
    else:          # It does not exist, append it to both lists
        tracks.append(toadd)
        frequencies.append(1)
    # Turn the log list into a string to write to the file
    log = ""
    for x in range(0, len(tracks)):
        log += "{}=.={}\n".format(tracks[x], frequencies[x])

    f = open(log_filename, "w")
    f.write(log)
    f.close()
    
try:
    main()
except Exception as e:
    f = open("err.txt","w")
    f.write(str(e))
    f.close()
