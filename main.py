#!/usr/bin/env python3
import urllib

from bing_hashing_image_downloader import downloader


def main():
    dir = "PhillipsParkZoo"

    with open("PhillipsParkZooCollection.csv", 'r') as f:
        doc = f.read()

    doc_lines = doc.split(',\n')
    queries: str = []
    for line in doc_lines:
        tmp = line.split(',')
        for t in tmp:
            if t != '':
                queries.append(t)
    assert len(queries) > 1
    for q in queries:
        print('Starting Scraping for ' + str(q))
        try:
            downloader.download(q,
                                limit=50,
                                output_dir=dir,
                                adult_filter_off=False,
                                timeout=60,
                                size=(224, 224),
                                verbose=True)
        except urllib.error.URLError:
            print('During the search for ' + q)
            print('an error occurred during download')
            continue
    print("completed list")


if __name__ == '__main__':
    main()
