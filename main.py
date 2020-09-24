
import geocoder
import csv


def getLatLngFromCSVKeyWords(csvFiles):
    locations = {}
    location = []
    append = location.append
    for csv in csvs:
        print(csv)
        with open("./csv/locations.csv", "r", encoding="utf-8_sig") as f:
            reader = csv.reader(f, delimiter='\t')
            for row in reader:
                ret = geocoder.osm(row[0], timeout=5.0)
                append([*row[0].split(','), *ret.latlng])
        locations[csv] = location
        location = []
    return locations


if __name__ == "__main__":
    csvs = ['./csv/locations.csv', './csv/another_locations.csv']
    print(getLatLngFromCSVKeyWords(csvFiles=csvs))
