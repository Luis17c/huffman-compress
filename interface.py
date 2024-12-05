import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import sys
import os

def install_dependencies():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "ttkbootstrap"])
        messagebox.showinfo("Dependências Instaladas", "Todas as dependências foram instaladas com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro de Instalação", f"Erro ao instalar as dependências: {e}")

try:
    import ttkbootstrap as tb
except ImportError:
    install_dependencies()
    import ttkbootstrap as tb

from features.compress import compress
from features.decompress import decompress

def on_compress():
    try:
        compress()
        messagebox.showinfo("Sucesso", "Texto compactado com sucesso! O arquivo foi salvo como 'saida.huf'.")
        update_file_sizes()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao compactar o texto: {e}")

def on_decompress():
    try:
        decompress()
        messagebox.showinfo("Sucesso", "Texto descompactado com sucesso! O arquivo foi salvo como 'entrada.txt'.")
        load_file_content()
        update_file_sizes()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao descompactar o texto: {e}")

def load_file_content():
    try:
        with open("./archives/entrada.txt", "r", encoding="utf-8") as file:
            content = file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, content)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar o conteúdo do arquivo: {e}")

def save_file_content():
    try:
        content = text_area.get(1.0, tk.END)
        with open("./archives/entrada.txt", "w", encoding="utf-8") as file:
            file.write(content.strip())
        messagebox.showinfo("Sucesso", "Arquivo salvo com sucesso!")
        update_file_sizes()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar o arquivo: {e}")

def update_file_sizes():
    try:
        decompressed_size = os.path.getsize("./archives/entrada.txt") if os.path.exists("./archives/entrada.txt") else 0
        compressed_size = os.path.getsize("./archives/saida.huf") if os.path.exists("./archives/saida.huf") else 0
        decompressed_label.config(text=f"Peso do Arquivo Descompactado: {decompressed_size} bytes")
        compressed_label.config(text=f"Peso do Arquivo Compactado: {compressed_size} bytes")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao atualizar os tamanhos dos arquivos: {e}")

def on_exit():
    root.destroy()

current_width = None

def adjust_layout(event):
    global current_width
    if current_width is None or abs(event.width - current_width) > 10:
        current_width = event.width
        width = event.width
        if width < 600:
            for i, widget in enumerate(button_frame.winfo_children()):
                widget.grid_configure(sticky="ew", column=0, row=i, padx=5, pady=5)
        else:
            for i, widget in enumerate(button_frame.winfo_children()):
                widget.grid_configure(sticky="ew", row=0, column=i, padx=5, pady=5)

root = tb.Window(themename="superhero")
root.title("Compactador e Descompactador")
root.geometry("800x600")

header_frame = tk.Frame(root, bg="blue", height=50)
header_frame.pack(fill="x", side="top")

header_label = tk.Label(header_frame, text="Compactador e Descompactador", font=("Helvetica", 20, "bold"), bg="blue", fg="white")
header_label.pack(pady=10)

button_frame = ttk.Frame(root, padding=10)
button_frame.pack(fill="x", side="top")

compress_button = ttk.Button(button_frame, text="Compactar Texto", command=on_compress)
compress_button.grid(row=0, column=0, padx=5, pady=5, sticky="w")

decompress_button = ttk.Button(button_frame, text="Descompactar Texto", command=on_decompress)
decompress_button.grid(row=0, column=1, padx=5, pady=5, sticky="w")

save_button = ttk.Button(button_frame, text="Salvar Alterações no Arquivo", command=save_file_content)
save_button.grid(row=0, column=2, padx=5, pady=5, sticky="w")

exit_button = ttk.Button(button_frame, text="Sair", command=on_exit)
exit_button.grid(row=0, column=3, padx=5, pady=5, sticky="w")

size_frame = ttk.Frame(root, padding=10)
size_frame.pack(fill="x", side="top")

decompressed_label = ttk.Label(size_frame, text="Peso do Arquivo Descompactado: 0 bytes")
decompressed_label.pack(side="left", padx=5)

compressed_label = ttk.Label(size_frame, text="Peso do Arquivo Compactado: 0 bytes")
compressed_label.pack(side="left", padx=5)

text_area_frame = ttk.LabelFrame(root, text="Conteúdo do Arquivo")
text_area_frame.pack(fill="both", expand=True, padx=10, pady=10)

text_area = tk.Text(text_area_frame, wrap=tk.WORD, font=("Consolas", 12))
text_area.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(text_area_frame, orient="vertical", command=text_area.yview)
scrollbar.pack(side="right", fill="y")
text_area.config(yscrollcommand=scrollbar.set)

load_file_content()
update_file_sizes()

root.bind("<Configure>", adjust_layout)
root.mainloop()
