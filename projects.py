# install pyqrcode and pypng
import pyqrcode
import png

link = "https://www.freecodecamp.org/"
qr_code = pyqrcode.create(link)
qr_code.png('qr_code.png', scale=6)

# location
# install geopy
from geopy.geocoders import Nominatim

# using nominatim api
geolocator = Nominatim(user_agent="geoapiExercises")

# enter zipcode
zipcode = input("Enter zipcode: ")

# using geocode()
location = geolocator.geocode(zipcode)

print("zipcode: ",zipcode)
print(location)


# pip install PyPDF2
import PyPDF2
pdf = open('TeslimCV.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdf)
page = reader.getPage(0)
print(page.extractText())


# print the whole month in a year
from calendar import *
year = int(input("enter year: "))
print(calendar(year))

# convert video files to a gif in python
from moviepy.editor import *
videoClip = VideoFileClip("sample.mp4")
videoClip.write_gif("sample.gif")


# language detection using python
from langdetect import detect
text = input("enter text: ")
print(detect(text)) 