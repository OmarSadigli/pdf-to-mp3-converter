from tkinter import *
from tkinter import filedialog
from gtts import gTTS
import PyPDF2
import slate3k as slate

# myText = "Hello my name is omar and I am 23 years old"
# language = "en"
# output = gTTS(text=myText,lang=language,slow=False)
#
# output.save("output.mp3")
# os.system("start output.mp3")

BG_COLOR = "#0e9aa7"
TEXT_COLOR = "#e4e4e4"


def get_pdf_file():
    global mytext
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Upload PDF File",
        filetypes=(("pdf files","*.pdf"),("doc files","*.docx"),("txt file","*.txt"))
    )
    print(filename)

    if filename != "":
        Label(window,text="Successfully Uploaded",
              bg=BG_COLOR,fg=TEXT_COLOR,font=("Arial",10,"bold")).grid(row=2,column=2,padx=10)
        pdf_file = filename

        pdfFileObj = open(pdf_file, "rb")
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
        mytext = ""
        for pageNum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            mytext += pageObj.extractText()
            print(mytext)
        pdfFileObj.close()


def save_audio_file(PDF_file):
    file = filedialog.asksaveasfile(title="save audio",initialdir='/')
    output = gTTS(text=PDF_file,lang="en")

    if file != "":
        output.save(file.name)
        Label(window,text="Successfully Saved",
              bg=BG_COLOR,fg=TEXT_COLOR,font=("Arial",12,"bold")).grid(row=3,column=2,padx=10)


# -------------- User Interface ------------ #
window = Tk()
window.title("PDF to Audio Book Converter")
window.geometry("800x700")
window.config(padx=325,pady=50,bg=BG_COLOR)

canvas = Canvas(height=150,width=150,bg=BG_COLOR,highlightthickness=0)
logo_img = PhotoImage(file="music-book.png")
canvas.create_image(75,75,image=logo_img)
canvas.grid(row=1,column=1,pady=60)

title_label = Label(window,text="Upload as Text\nSave as Audio",font=("Arial", 20, "bold"),
                    bg=BG_COLOR,
                    fg=TEXT_COLOR)
title_label.grid(row=0,column=1)


# ---- BUTTONS ----- #
upload_button = Button(window,text="Upload Text File",
                       font=("Arial",15,"bold"),
                       bg=BG_COLOR,
                       fg=TEXT_COLOR,
                       width=15,
                       command=get_pdf_file
                       )
upload_button.grid(row=2,column=1)

save_button = Button(window,text="Save Audio File",
                     font=("Arial",15,"bold"),
                     bg=BG_COLOR,
                     fg=TEXT_COLOR,
                     width=15,
                     command=lambda: save_audio_file(PDF_file=mytext)
                     )
save_button.grid(row=3,column=1,pady=20)
window.mainloop()
