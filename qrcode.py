import pyqrcode
import os, shutil 
title = input("give an title")
text = input("text into qr code")
file_name_svg = title +".svg"
file_name_png = title +".png"
url =  pyqrcode.create(text)
url.svg(file_name_svg, scale = 8)
url.png(file_name_png, scale = 10)
os.mkdir(fr"/Users/sai/Desktop/{title}")
shutil.move(f"{file_name_png}", fr"/Users/sai/Desktop/{title}")
shutil.move(f"{file_name_svg}",fr"/Users/sai/Desktop/{title}" )
