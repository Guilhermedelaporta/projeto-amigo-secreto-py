import random
import tkinter as tk
from tkinter import messagebox

class AmigoSecretoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorteio de Amigo Secreto")
        self.root.configure(bg="#EAF6F6")  # Fundo com cor clara
        
        self.participantes = []
        self.sorteados = []
        
        # Frame para entrada de nomes
        self.frame_entrada = tk.Frame(root, bg="#EAF6F6")
        self.frame_entrada.pack(pady=10)

        self.label_nome = tk.Label(self.frame_entrada, text="Nome do participante:", bg="#EAF6F6", fg="#004F54", font=("Arial", 12, "bold"))
        self.label_nome.pack(side=tk.LEFT)

        self.entry_nome = tk.Entry(self.frame_entrada, font=("Arial", 12))
        self.entry_nome.pack(side=tk.LEFT, padx=5)

        self.btn_adicionar = tk.Button(self.frame_entrada, text="Adicionar", bg="#82C9C9", fg="#FFFFFF", font=("Arial", 12, "bold"), command=self.adicionar_participante)
        self.btn_adicionar.pack(side=tk.LEFT)

        # Frame para lista de participantes
        self.frame_lista = tk.Frame(root, bg="#EAF6F6")
        self.frame_lista.pack(pady=10)

        self.label_participantes = tk.Label(self.frame_lista, text="Participantes:", bg="#EAF6F6", fg="#004F54", font=("Arial", 12, "bold"))
        self.label_participantes.pack()

        self.listbox_participantes = tk.Listbox(self.frame_lista, width=30, height=10, font=("Arial", 12), bg="#FFFFFF", fg="#004F54")
        self.listbox_participantes.pack()

        # Frame para sorteio
        self.frame_sorteio = tk.Frame(root, bg="#EAF6F6")
        self.frame_sorteio.pack(pady=10)

        self.btn_sortear = tk.Button(self.frame_sorteio, text="Realizar Sorteio", bg="#FF6B6B", fg="#FFFFFF", font=("Arial", 12, "bold"), command=self.realizar_sorteio)
        self.btn_sortear.pack()

        # Adicionando uma mensagem de rodapé com tema natalino
        self.footer = tk.Label(root, text="\u2605 Feliz Natal e Boas Festas! \u2605", bg="#EAF6F6", fg="#004F54", font=("Arial", 14, "italic"))
        self.footer.pack(pady=10)

    def adicionar_participante(self):
        nome = self.entry_nome.get().strip().capitalize()
        if nome == "":
            messagebox.showwarning("Entrada inválida", "O nome não pode estar vazio.")
        elif nome in self.participantes:
            messagebox.showwarning("Entrada duplicada", "Esse nome já foi adicionado.")
        else:
            self.participantes.append(nome)
            self.listbox_participantes.insert(tk.END, nome)
            self.entry_nome.delete(0, tk.END)

    def realizar_sorteio(self):
        if len(self.participantes) < 2:
            messagebox.showwarning("Participantes insuficientes", "É necessário pelo menos 2 participantes para realizar o sorteio.")
            return

        self.sorteados = self.participantes[:]
        while any(p == s for p, s in zip(self.participantes, self.sorteados)):
            random.shuffle(self.sorteados)

        resultado = "\n".join(f"{p} tirou {s}." for p, s in zip(self.participantes, self.sorteados))
        messagebox.showinfo("Resultado do Sorteio", resultado)

if __name__ == "__main__":
    root = tk.Tk()
    app = AmigoSecretoApp(root)
    root.mainloop()