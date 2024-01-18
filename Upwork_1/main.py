import pandas as pd
import requests
import os
from fpdf import FPDF


def downloadImage(title, url):
    
    
    response = requests.get(url)
    if response == 200:
        pass    
    else:
        print("can't download image!")


def extractingDataFromExcel(excelFilePath):
    
    df = pd.read_excel(excelFilePath)

    titles= df['Title']
    urls = df['URL']
    
    imageLists = []

    for title, url in zip(titles, urls):
        image = downloadImage(title, url)
        if image:
            imageLists.append(image)
    
    print(image)
    return image

def createPdf(imagePaths, pdfFileName):
    pdf = FPDF()
    


# creating a dir named as images to store all the images
if not os.path.exists('images'):
    os.makedirs('images')

excelFilePath = 'Weather_Links.xlsx'
imagePaths = extractingDataFromExcel(excelFilePath)


pdfFileName = "output.pdf"
createPdf(imagePaths, pdfFileName)

