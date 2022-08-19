#!/usr/bin/env python3
import urllib

from bing_image_downloader import downloader

def main():
    dir = "WCP"

    with open('classes.csv', 'r') as f:
        classes_str = f.read()

    queries = classes_str.split(',')

    for q in queries:
        q = '"' + q + '"'
        print('Starting Scraping for ' + str(q))
        try:
            downloader.download(q,
                                limit=50,
                                output_dir=dir,
                                adult_filter_off=False,
                                timeout=60,
                                filter='photo',
                                verbose=True)
        except urllib.error.URLError:
            print('an error occured durring download')
            continue
    print("completed list")






if __name__ == '__main__':
    main()