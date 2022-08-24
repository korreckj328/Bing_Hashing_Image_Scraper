import glob
import io
import os
from hashlib import sha1
from PIL import Image

classes = glob.glob("PhillipsParkZoo/*")

for c in classes:
    class_glob = glob.glob(c + "/*")
    if "hash_table.csv" in class_glob:
        command = "mv " + c + "/hash_table.csv " + c + "/.hash_table.csv"
        os.sys(command)
    else:
        images = glob.glob(c + "/*.png")
        hashes = []
        for i in images:
            img = Image.open(i)
            img_byte_array = io.BytesIO()
            print('saving image to bytes object')
            img.save(img_byte_array, format="PNG")
            img_byte_array = img_byte_array.getvalue()
            h = sha1(img_byte_array)
            hashes.append(h)
        file_name = c + "/.hash_table.csv"
        with open(file_name, 'w') as f:
            for hsh in hashes:
                f.write(str(hsh) + ",")