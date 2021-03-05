""" Shebang for linux to determine executable path env"""
#!/usr/bin/env python3


"""Import necessary Library"""
from PIL import Image
import os, sys


#Loops through image
for file in os.listdir():
    #matching the file with the name of the file
    if file.startswith('ic_'):
        # Opening, rotate, resize, and convert to RGB
        # including save file in /opt/icons with correct formats
        im = Image.open(file)
        im = im.rotate(-90).resize((128,128))
        new_im = im.convert('RGB').save('/opt/icons/'+file+'.jpeg')
