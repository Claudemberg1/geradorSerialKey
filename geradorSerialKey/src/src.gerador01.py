# gerador_de_chaves_personalizado.py

import tkinter as tk
from tkinter import messagebox
import secrets
import string
import pyperclip



class GeradorChavesGUI:
    def __init__(self, master):
        self.master = master
        master.title("Gerador de Chaves de Licença")
        master.geometry("500x350")
        master.configure(bg="#2c3e50")
        master.resizable(False, False)

        font_label = ("Helvetica", 10)
        font_entry = ("Helvetica", 10)
        font_button = ("Helvetica", 10, "bold")

        self.main_frame = tk.Frame(master, bg="#2c3e50")
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.quantity_label = tk.Label(self.main_frame,
                                       text="Número de chaves para gerar:",
                                       bg="#2c3e50", fg="white", font=font_label)
        self.quantity_label.pack(pady=(0, 5))

        self.quantity_entry = tk.Entry(self.main_frame, width=10, font=font_entry)
        self.quantity_entry.pack(pady=(0, 10))
        self.quantity_entry.insert(0, "1")

        self.generate_button = tk.Button(self.main_frame, text="Gerar Chaves",
                                         command=self.gerar_chaves_click,
                                         bg="#3498db", fg="white", font=font_button)
        self.generate_button.pack(pady=10)

        self.result_label = tk.Label(self.main_frame,
                                     text="Chaves Geradas:",
                                     bg="#2c3e50", fg="white", font=font_label)
        self.result_label.pack()

        self.key_display = tk.Text(self.main_frame, width=50, height=10, font=("Courier", 10), state=tk.DISABLED)
        self.key_display.pack(pady=5)

        self.copy_button = tk.Button(self.main_frame, text="Copiar Todas as Chaves",
                                     command=self.copiar_chaves,
                                     bg="#2ecc71", fg="white", font=font_button)
        self.copy_button.pack(pady=5)
        self.copy_button.config(state=tk.DISABLED)

    def gerar_chaves_click(self):
        try:
            quantidade = int(self.quantity_entry.get().strip())
            if quantidade <= 0:
                messagebox.showerror("Erro", "Por favor, insira um número maior que 0.")
                return

            self.key_display.config(state=tk.NORMAL)
            self.key_display.delete(1.0, tk.END)

            chaves = []
            for _ in range(quantidade):
                chave_gerada = self.gerar_chave_aleatoria()
                chaves.append(chave_gerada)

            for chave in chaves:
                self.key_display.insert(tk.END, chave + "\n")

            self.key_display.config(state=tk.DISABLED)
            self.copy_button.config(state=tk.NORMAL)

        except ValueError:
            messagebox.showerror("Erro", "Entrada inválida. Por favor, digite um número.")
            self.copy_button.config(state=tk.DISABLED)

    def gerar_chave_aleatoria(self):
        caracteres = string.ascii_uppercase + string.digits
        chave = ''.join(secrets.choice(caracteres) for _ in range(9))
        return f"{chave[0:3]}-{chave[3:6]}-{chave[6:9]}"

    def copiar_chaves(self):
        chaves = self.key_display.get(1.0, tk.END)
        if chaves.strip():
            pyperclip.copy(chaves.strip())
            messagebox.showinfo("Sucesso", "Chaves copiadas para a área de transferência!")
        else:
            messagebox.showerror("Erro", "Nenhuma chave para copiar.")


root = tk.Tk()
app = GeradorChavesGUI(root)
root.mainloop()