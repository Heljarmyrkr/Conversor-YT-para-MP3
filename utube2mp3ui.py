import tkinter
from tkinter import *
import tkinter.messagebox as tkmb
from tkinter import font as tkFont
import pyglet
import customtkinter
from pytubefix import YouTube
from pydub import AudioSegment
import os

# =========================== Configurações da Aplicação ===========================

#Configurações básicas do tema e janela principal
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

window = customtkinter.CTk()
window.geometry("600x500")
window.title("Utube2MP3")
window.resizable(False, False)

def baixar_audio(link):
    if not link:
        tkmb.showerror("Error", "Insert a valid YouTube video link!")

    try:
        #Baixar o vídeo do YouTube
        yt = YouTube(link)
        stream = yt.streams.filter(only_audio=True).first()
        print(f"Downloading: {yt.title}")
        stream.download(filename='video.mp4')

        #Converter para MP3 usando pydub
        audio = AudioSegment.from_file("video.mp4", format="mp4")
        audio.export("audio.mp3", format="mp3")
        print(f"MP3 Archive saved as: audio.mp3")

        #Remover o arquivo de vídeo original
        os.remove("video.mp4")

        tkmb.showinfo("Sucess", f"{yt.title} was converted and saved as MP3!")
    except Exception as e:
        tkmb.showerror("Error", f"Something went wrong: {e}")


#Definindo fonte personalizada
pyglet.font.add_file('YouTubeSansSemibold.otf')
font_name = "YouTube Sans"

#Frame
frame = customtkinter.CTkFrame(master=window,width=550,height=450)
frame.place(relx=0.5,rely=0.5,anchor="center")

img = PhotoImage(file="logo.png")
label_img = customtkinter.CTkLabel(master=frame,image=img,text="")
label_img.place(relx=0.5,rely=0.27,anchor="center")

#Frame Widgets
label = customtkinter.CTkLabel(master=frame,
                               text="By Heljarmyrkr",
                               text_color="white",
                               font=(font_name,20))
label.place(relx=0.01,rely=0.96,anchor="w")


# Campo de entrada para o link
user_entry= customtkinter.CTkEntry(master=frame,
                                   placeholder_text="Insert youtube link here to convert: "
                                                    "\"https://www.youtube.com/watch...\"" ,
                                   width=500,
                                   height=25
                                   )
user_entry.place(relx=0.5,rely=0.6,anchor="center")

#Função para chmar o baixar_audio com o link inserido
def converter_audio():
    link = user_entry.get()
    baixar_audio(link)

#Botão de conversão
button = customtkinter.CTkButton(master=frame,
                       text='Convert',
                       command=converter_audio)
button.place(relx=0.5,rely=0.7,anchor="center")

window.mainloop()
