from tkinter import filedialog
from PyPDF2 import PdfReader

def find_nf():
    pdf_path = filedialog.askopenfilename()
    with open(pdf_path, "rb") as pdf:
        with open(pdf_path[59:] + ".txt","w") as txt:
            reader = PdfReader(pdf)
            for i in range(len(reader.pages)):

                page = reader.pages[i]

                text = page.extract_text()

                x = text.find('NF-e',0)

                test = True

                while test:
                    y = x + 14
                    txt.writelines(text[x:y] + "\n")
                    x = text.find('NF-e',y)
                    if x == -1:
                        test = False