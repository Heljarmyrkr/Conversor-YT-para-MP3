import tkinter
from tkinter import *
from tkinter import filedialog
import webbrowser
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
window.title("Utube2MP3v0.2.0(Beta): ")
window.resizable(False, False)

def janela_configurações():
    janela_configurações = customtkinter.CTkToplevel(window)
    janela_configurações.geometry("200x200")
    janela_configurações.title("Settings")
    janela_configurações.resizable(False, False)

    janela_configurações.focus_set()
    janela_configurações.grab_set()

    janela_configurações_frame = customtkinter.CTkFrame(master=janela_configurações,
                                                        width=550,
                                                        height=450,
                                                        fg_color="#0F0F0F")
    janela_configurações_frame.place(relx=0.5,rely=0.5,anchor="center")

    opções = ["English", "Français", "Deutsch", "Português"]

    combobox = customtkinter.CTkOptionMenu(janela_configurações_frame,
                                           values=opções,
                                           fg_color="darkred",
                                           button_color="red",
                                           command=None)
    combobox.set("English")
    combobox.place(relx=0.5, rely=0.5, anchor="center")

    label = customtkinter.CTkLabel(master=janela_configurações_frame,
                                   text="Language:",
                                   text_color="white",
                                   font=(font_name, 20))
    label.place(relx=0.5, rely=0.43, anchor="center")

    label = customtkinter.CTkLabel(master=janela_configurações_frame,
                                   text="Soon!",
                                   text_color="white",
                                   font=(font_name, 20))
    label.place(relx=0.5, rely=0.65, anchor="center")


def escolher_local_arquivo(local):
    caminho_arquivo = filedialog.asksaveasfilename(
        defaultextension=".mp3",
        filetypes=[("MP3 files", "*.mp3")],
        initialfile=local
    )
    return caminho_arquivo

def abrir_youtube():
    webbrowser.open("https://www.youtube.com/")

def baixar_audio(link):
    if not link:
        tkmb.showerror("Error", "Insert a valid YouTube video link!")

    try:
        #Baixar o vídeo do YouTube
        yt = YouTube(link)
        stream = yt.streams.filter(only_audio=True).first()
        print(f"Downloading: {yt.title}")
        stream.download(filename='video.mp4')

        titulo = yt.title
        nome_limpo = "".join(x for x in titulo if x.isalnum() or x in " _-")

        caminho_arquivo = escolher_local_arquivo(nome_limpo)

        if not caminho_arquivo:
            tkmb.showinfo("Info", "Save operation canceled.")
            return


        #Converter para MP3 usando pydub
        audio = AudioSegment.from_file("video.mp4", format="mp4")
        audio.export(f"{caminho_arquivo}", format="mp3")
        print(f"MP3 Archive saved as: {caminho_arquivo}")

        #Remover o arquivo de vídeo original
        os.remove("video.mp4")

        tkmb.showinfo("Sucess", f"{yt.title} was converted and saved as MP3!")
    except Exception as e:
        tkmb.showerror("Error", f"Something went wrong: {e}")


#Definindo fonte personalizada
pyglet.font.add_file('YouTubeSansSemibold.otf')
font_name = "YouTube Sans"

#Frame
frame = customtkinter.CTkFrame(master=window,width=550,height=450, fg_color="#0F0F0F")
frame.place(relx=0.5,rely=0.5,anchor="center")

img = PhotoImage(file="logo.png")
label_img = customtkinter.CTkLabel(master=frame,image=img,text="")
label_img.place(relx=0.5,rely=0.27,anchor="center")

img2 = PhotoImage(file="youtubelogo.png")
label_img2 = customtkinter.CTkLabel(master=frame, image=img2, text="")

img3 = PhotoImage(file="converter.png")
label_img3 = customtkinter.CTkLabel(master=frame, image=img3, text="")

img4 = PhotoImage(file="settings.png")
label_img4 = customtkinter.CTkLabel(master=frame, image=img4, text="")

#Frame Widgets
label = customtkinter.CTkLabel(master=frame,
                               text="By Heljarmyrkr©",
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

#Função para chamar o baixar_audio com o link inserido
def converter_audio():
    link = user_entry.get()
    baixar_audio(link)

#Botão
button = customtkinter.CTkButton(master=frame,
                       text='Convert',
                       command=converter_audio,
                       fg_color="darkred",
                       hover_color="red",
                       image=img3,
                       compound="left"

                                )
button.place(relx=0.5,rely=0.73,anchor="center")


button = customtkinter.CTkButton(master=frame,
                       text='Open YouTube',
                       fg_color = "darkred",
                       hover_color = "red",
                       command=abrir_youtube,
                       image=img2,
                       compound="left"
                         )
button.place(relx=0.5,rely=0.81,anchor="center")

button = customtkinter.CTkButton(master=frame,
                       text='Settings',
                       fg_color = "darkred",
                       hover_color = "red",
                       image = img4,
                       compound = "left",
                       command= janela_configurações
                         )
button.place(relx=0.5,rely=0.89,anchor="center")



window.mainloop()



