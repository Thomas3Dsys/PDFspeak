from gtts import gTTS
import os
from pypdf import PdfReader




valid_file = False

#Get pdf file path and pdf reader object
while not valid_file:
    pdf_file = input ("Specify the pdf file name:")
    
    file_name, file_extension = os.path.splitext(pdf_file)
    if file_extension.lower() == ".pdf":
        try:
            reader = PdfReader(pdf_file)
            valid_file = True

        except FileNotFoundError:
            print("File not found.")
            continue
       
print(f"total pages:{len(reader.pages)}")
go_flag = True

#get pages for use one at a time
while go_flag:
    i = int(input(f"what page would you like me to read page ({len(reader.pages)} total)?"))-1
    if i < 0: 
        go_flag = False
    page = reader.pages[i]
    page_text = page.extract_text()
    print("")
    print("Processing the audio... here is the text while you wait.")
    print("")
    
    print(page_text)

    language = 'en'
    
    file = f"{file_name}_page{i+1}.mp3"
    
    #render new file if needed, then open file using the OS
    if not os.path.isfile(file):
        myobj = gTTS(text=page_text, lang=language, slow=False)
        myobj.save(file)
    os.system(file)