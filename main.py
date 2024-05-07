from tkinter import filedialog
from util import find_nf as find

def main():
    with filedialog.askopenfilename(title="Selecione o arquivo para ser extraido", filetypes=[('portable document format','*.pdf')]) as open:
      with filedialog.asksaveasfile(title="Selecione a pasta para salvar o arquivo", defaultextension=".txt", filetypes=[('text','*.txt')]) as save:
        save.write(find.find_nf(open))
  
if __name__ == "__main__":
    main()