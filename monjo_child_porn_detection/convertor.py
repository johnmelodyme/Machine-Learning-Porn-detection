#!/usr/bin/env python
import PIL
from PIL import Image
import numpy as np
import json
import os
os.system("pip3 install sightengine")

from sightengine.client import SightengineClient

def main():
    client = SightengineClient('1069852127', 'tLNDZxAArCRND5p8qt7A')
    theSpecialInteger = 18
    dataLocation = input("Please input the data:  \n")
    __image = Image.open(dataLocation)
    np__image = np.array(__image)
    print("Converted Image to Array " , np__image)
    np__image = np__image - theSpecialInteger
    new_image = Image.fromarray(np__image)
    #new_image.save("output.png")
    output = client.check("nudity","wad","offensive","faces","face-attributes", "celebrities").set_file(dataLocation)
    print(json.dumps(output, indent=4, sort_keys=True))

if __name__ == "__main__":
    main()