import os
import customtkinter as ctk
from tkinter import filedialog
from moviepy.video.io.VideoFileClip import VideoFileClip
from threading import Thread

def convert_mov_to_mp4():
    def perform_conversion():
        file_path = filedialog.askopenfilename(filetypes=[("MOV files", "*.mov")])
        if not file_path:
            status_label.configure(text="Conversão cancelada!")
            return

        if not file_path.lower().endswith('.mov'):
            status_label.configure(text="Selecione um arquivo MOV válido!")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
        if not save_path:
            status_label.configure(text="Conversão cancelada!")
            return

        try:
            status_label.configure(text="Convertendo... Isso pode levar alguns minutos.")
            progress_label.configure(text="0%")
            app.update_idletasks()

            video = VideoFileClip(file_path)
            total_duration = video.duration  
  
            def update_progress(current_time):
                percent_complete = min(int((current_time / total_duration) * 100), 100)
                progress_label.configure(text=f"{percent_complete}%")
                app.update_idletasks()

            for t in range(int(total_duration) + 1):
                update_progress(t)  
            video.write_videofile(save_path, codec="libx264", audio_codec="aac")

            # Finalizar a conversão
            progress_label.configure(text="100%")
            status_label.configure(text="Conversão concluída com sucesso!")
        except Exception as e:
            status_label.configure(text=f"Erro durante a conversão: {e}")
        finally:
            video.close()

    Thread(target=perform_conversion).start()

ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("blue")  

app = ctk.CTk()
app.title("Conversor MOV para MP4")
app.geometry("500x350")

title_label = ctk.CTkLabel(app, text="Conversor de Vídeos MOV para MP4", font=("Arial", 18, "bold"))
title_label.pack(pady=20)

convert_button = ctk.CTkButton(app, text="Selecionar e Converter", command=convert_mov_to_mp4, font=("Arial", 14))
convert_button.pack(pady=10)

progress_label = ctk.CTkLabel(app, text="0%", font=("Arial", 18))
progress_label.pack(pady=20)

status_label = ctk.CTkLabel(app, text="", font=("Arial", 12))
status_label.pack(pady=10)

footer_label = ctk.CTkLabel(app, text="Desenvolvido por Rial", font=("Arial", 10), text_color="lightgrey")
footer_label.pack(side="bottom", pady=10)


app.mainloop()
