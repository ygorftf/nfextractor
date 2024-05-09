import PyPDF2

def find_nf(path):
    txt = ""
    with open(path, "rb") as pdf:
        reader = PyPDF2.PdfReader(pdf)
        for i in range(len(reader.pages)):
            page = reader.pages[i]
            text = page.extract_text()
            x = text.find('NF-e',0)
            test = True
            while test:
                y = x + 14
                txt += f"{text[x:y]}\n"
                x = text.find('NF-e',y)
                if x == -1:
                    test = False
        return txt

if __name__ == "__main__":
    find_nf()