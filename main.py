#!/usr/bin/env python3
import urllib

from bing_hashing_image_downloader import downloader

def main():
    dir = "WCP"

    with open('classes.csv', 'r') as f:
        classes_str = f.read()

    queries = classes_str.split(',')
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
            print('an error occured durring download')
            continue
    print("completed list")






if __name__ == '__main__':
    main()
