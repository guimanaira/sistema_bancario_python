import tkinter as tk
from tkinter import messagebox

class BancoApp:
    def __init__(self, root):
        self.saldo = 0.0
        self.extrato = []

        self.root = root
        self.root.title("Bem Vindo ao Banco Dio")

        #Saldo
        self.label_saldo = tk.Label(root, text=f"Saldo: R$ {self.saldo:.2f}", font=("Arial, 14"))
        self.label_saldo.pack(pady=5)

        #Entrada de valor
        self.entry_valor = tk.Entry(root, font=("Arial", 12))
        self.entry_valor.pack(pady=5)

        #Botões
        self.btn_depositar = tk.Button(root, text="Depositar", command=self.depositar)
        self.btn_depositar.pack(pady=10)

        self.btn_sacar = tk.Button(root, text="Sacar", command=self.sacar)
        self.btn_sacar.pack(pady=10)

        self.btn_extrato = tk.Button(root, text="Ver Extrato", command=self.ver_extrato)
        self.btn_extrato.pack(pady=10)
        
    def depositar(self):
        try:
            valor = float(self.entry_valor.get())
            if valor <= 0:
                raise ValueError("O Valor deve ser positivo.")
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            self.atualizar_saldo()
            messagebox.showinfo("Sucesso", "Depósito realizado com sucesso!")
        except ValueError as e:
            messagebox.showerror("Erro", f"Entrada inválida: {e}")
        self.entry_valor.delete(0, tk.END)

    def sacar(self):
        try:
            valor = float(self.entry_valor.get())
            if valor <=0:
                raise ValueError("O valor deve ser positivo.")
            if valor > self.saldo:
                messagebox.showerror("Erro", "Saldo Insuficiente!")
                return
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.atualizar_saldo()
            messagebox.showinfo("Sucesso", "Saque realizado com sucesso!")
        except ValueError as e:
            messagebox.showerror("Erro", f"Entrada inválida: {e}")
        self.entry_valor.delete(0, tk.END)

    def ver_extrato(self):
        extrato_texto = "\n".join(self.extrato) if self.extrato else "Nenhuma transação realizada."
        messagebox.showinfo("Extrato", extrato_texto)

    def atualizar_saldo(self):
        self.label_saldo.config(text=f"Saldo: R$ {self.saldo:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BancoApp(root)
    root.mainloop()
