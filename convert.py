import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import threading

def convert_mov_to_mp4(input_path, new_name):
    try:
        output_directory = os.path.dirname(input_path)
        output_path = os.path.join(output_directory, f"{new_name}.mp4")
        
        status_label.config(text="Convertendo...")
        root.update_idletasks()
        
        clip = VideoFileClip(input_path)
        clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
        
        status_label.config(text="Concluído!")
        messagebox.showinfo("Sucesso", f"Conversão concluída: {output_path}")
    except Exception as e:
        status_label.config(text="Erro")
        messagebox.showerror("Erro", f"Erro ao converter o arquivo:\n{e}")
    finally:
        clip.close()

def select_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Arquivos MOV", "*.mov"), ("Todos os Arquivos", "*.*")]
    )
    if file_path:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, file_path)

def start_conversion():
    input_path = input_entry.get()
    new_name = name_entry.get()
    
    if not input_path or not os.path.exists(input_path):
        messagebox.showerror("Erro", "Selecione um arquivo MOV válido.")
        return

    if not new_name:
        messagebox.showerror("Erro", "Informe um novo nome para o arquivo de saída.")
        return

    conversion_thread = threading.Thread(target=convert_mov_to_mp4, args=(input_path, new_name))
    conversion_thread.start()

root = tk.Tk()
root.title("Conversor MOV para MP4")
root.geometry("500x300")
root.resizable(False, False)

tk.Label(root, text="Arquivo MOV:").pack(pady=5)
input_entry = tk.Entry(root, width=40)
input_entry.pack(pady=5)
tk.Button(root, text="Selecionar Arquivo", command=select_file).pack(pady=5)

tk.Label(root, text="Novo Nome (sem extensão):").pack(pady=5)
name_entry = tk.Entry(root, width=40)
name_entry.pack(pady=5)

tk.Button(root, text="Converter", command=start_conversion, bg="green", fg="white").pack(pady=20)

status_label = tk.Label(root, text="", fg="blue")
status_label.pack(pady=10)

root.mainloop()
