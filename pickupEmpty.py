import urllib

from bing_hashing_image_downloader import downloader
dir = "PhillipsParkZoo"

q = "African Spurred Tortoise"

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