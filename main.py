from PIL import Image
from pytesseract import pytesseract
import streamlit as st
import os
import openai
import numpy as np

st.title("Summarise Images Containing Text")
st.subheader("This Computer Vision based Application summarises text from images. A great way to save your time in case you need a gist of some of the most important points")

#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

img=st.file_uploader("Please Upload an Image Containing Text")
#data=img.read()

#Define path to image
#path_to_image = 'Sample_Image1.jpg'

#Open image with PIL
#img = Image.open(path_to_image)

#Extract text from image

openai.api_key = st.secrets["pass"]

if img is not None:
   img1 = Image.open(img)
   text = pytesseract.image_to_string(img1)
   if st.button("Generate Summary"):
    response = openai.Completion.create(
      model="text-davinci-003",
       prompt="Summarize this for a second-grade student:"+ text,
       temperature=0.7,
       max_tokens=64,
       top_p=1.0,
       frequency_penalty=0.0,
       presence_penalty=0.0
)
    print(response.choices[0].text)
    st.write(response.choices[0].text)

