
import csv
from datetime import date
import geocoder
import os
import pandas as pd

# テナント名 csv から Geo location を取得して
# my map プロット用の　import ファイルを生成する処理


def getLatLngFromCSVKeyWords(csvFiles):
    # 一行目の見出しは考慮しない
    locations = {}
    location = []
    for csvFile in csvFiles:
        with open(csvFile, "r", encoding="utf-8") as f:  # BOM 有りなら utf-8_sig
            reader = csv.reader(f, delimiter='\t')
            for row in reader:
                ret = geocoder.osm(row[0], timeout=5.0)
                location.append([*row[0].split(','), *ret.latlng])
        locations[csvFile] = location
        location = []
    return locations


def touch(path):
    open(path, 'a+').close()


header = ['place', 'date', 'lot', 'lng']


def writeLatLngToCSV(files: dict):
    # 日付ごとに output
    # ファイルがなければ追加
    # my map では lat lng でプロットするため、それらとタイトルと日付等のメタデータを行にする
    outputFileName = './output/{0}.csv'.format(date.today())
    if not os.path.exists(outputFileName):
        touch(outputFileName)

    csv = pd.read_csv(outputFileName,
                      sep='\t',
                      names=header)

    for _, locations in files.items():
        for location in locations:
            csv = pd.concat(
                [csv, pd.DataFrame([location], columns=header)], ignore_index=True)
    csv.to_csv(outputFileName, encoding='"utf-8')


if __name__ == "__main__":
    csvs = ['./csv/locations.csv', './csv/another_locations.csv']
    writeLatLngToCSV(files=getLatLngFromCSVKeyWords(csvFiles=csvs))
