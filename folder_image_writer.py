from pathlib import Path
import os

#dirs = ["XOS", "DPLUS",  "WOR", "F4SLOP", "AFFE", "EM", "XRF", "WW80", "FFFF", "F4DC", "HOX", "ABPI", "BTAS", "BWM", "CAAV", "CMM", "EX", "F4", "FFCC", "JLU", "Markers", "ORVL", "RE", "STRF", "SWBW", "WCR", "WK", "WWE", "XDPS", "STBG", "BGAM", "DCXM", "SVAC"]
dirs = filter(os.path.isdir, os.listdir(os.curdir))
for dir in dirs:
    if not ".github" in dir:
        f = open(dir + "/images.html", "w")
        f.write("<!DOCTYPE html><html lang=\"en-us\"><head><meta charset=\"utf-8\"><title>Heroclix Map Viewer</title><style type=\"text/css\">.container {display: flex;flex-wrap: wrap; justify-content:center;} .roll20 {height:180px; width:auto; padding-top:5px; padding-bottom:5px; padding-left:5px; padding-right:5px;} </style></head>")

        f.write ("<body><div class=\"container\">")

        for path in Path(dir).rglob('*.png'):
            print(path)
            f.write("<img class=\"roll20\" src=\"")
            f.write(path.name)
            f.write("\"/>")

        f.write("</div></body></html>")
        f.close()
