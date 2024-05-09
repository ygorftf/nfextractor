from tkinter import filedialog
from util import find_nf as find

def main():
  con = True
  while con:
    try:
      open = filedialog.askopenfilename(title="Selecione o arquivo para ser extraido", filetypes=[('portable document format','*.pdf')])
      with filedialog.asksaveasfile(title="Selecione a pasta para salvar o arquivo", filetypes=[('Text archive','*.txt'),('Comma separeted file', '*.csv')]) as save:
        save.write(find.find_nf(open))
    except TypeError:
      con = False
  
if __name__ == "__main__":
    main()