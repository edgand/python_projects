#Importing Libraries
#Importing Google Text to Speech library
from gtts import gTTS

#Importing PDF reader PyPDF2
import PyPDF2

#Open file Path
pdf_File = open('name.pdf', 'rb') 

#Create PDF Reader Object
#pdf_Reader = PyPDF2.PdfFileReader(pdf_File)
#count = pdf_Reader.numPages # counts number of pages in pdf
#textList = []
pdf_Reader = PyPDF2.PdfReader(pdf_File)
count = len(pdf_Reader.pages)
textList = []

#Extracting text data from each page of the pdf file
for i in range(count):
   try:
    page = pdf_Reader.pages[i]
    textList.append(page.extract_text())
   except:
       pass

#Converting multiline text to single line text
textString = " ".join(textList)

print(textString)

#Set language to english (en)
language = 'es'

#Call GTTS
myAudio = gTTS(text=textString, lang=language, slow=False)

#Save as mp3 file
myAudio.save("Audio.mp3")

pdf_File.close()