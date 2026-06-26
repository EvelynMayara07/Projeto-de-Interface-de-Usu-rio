import tkinter as tk
from tkinter import ttk, messagebox

# ---------------- Banco de Consultas ----------------

consultas = {
    "Clínico Geral": {
        "Ana Souza": {
            "horario": "08:30",
            "convenio": "Unimed",
            "retorno": "Não",
            "prioridade": "Não",
            "queixa": "Dor de garganta",
            "diagnostico": "Amigdalite",
            "tratamento": "Antibiótico e repouso"
        },

        "Carlos Lima": {
            "horario": "09:15",
            "convenio": "Particular",
            "retorno": "Sim",
            "prioridade": "Não",
            "queixa": "Hipertensão",
            "diagnostico": "Pressão elevada",
            "tratamento": "Controle da pressão"
        }
    },

    "Cardiologia": {
        "José Pereira": {
            "horario": "10:00",
            "convenio": "Bradesco Saúde",
            "retorno": "Sim",
            "prioridade": "Sim",
            "queixa": "Dor no peito",
            "diagnostico": "Angina",
            "tratamento": "Avaliação cardiológica"
        },

        "Maria Oliveira": {
            "horario": "11:00",
            "convenio": "Unimed",
            "retorno": "Não",
            "prioridade": "Não",
            "queixa": "Palpitações",
            "diagnostico": "Em investigação",
            "tratamento": "Exames"
        }
    },

    "Pediatria": {
        "Pedro Santos": {
            "horario": "14:00",
            "convenio": "SUS",
            "retorno": "Não",
            "prioridade": "Sim",
            "queixa": "Febre",
            "diagnostico": "Gripe",
            "tratamento": "Repouso e hidratação"
        }
    },

    "Ortopedia": {
        "Juliana Costa": {
            "horario": "15:30",
            "convenio": "Amil",
            "retorno": "Sim",
            "prioridade": "Não",
            "queixa": "Dor no joelho",
            "diagnostico": "Tendinite",
            "tratamento": "Fisioterapia"
        }
    }
}

# ---------------- Janela ----------------

janela = tk.Tk()
janela.title("🏥 Sistema de Consultas Médicas")
janela.geometry("560x620")
janela.configure(bg="#EAF4FC")

tk.Label(
    janela,
    text="🏥 Sistema de Consultas Médicas",
    font=("Arial",16,"bold"),
    bg="#1976D2",
    fg="white",
    pady=12
).pack(fill="x")

tk.Label(
    janela,
    text="Escolha uma especialidade e um paciente agendado.",
    bg="#EAF4FC",
    font=("Arial",10)
).pack(pady=10)

# ---------------- Especialidade ----------------

tk.Label(
    janela,
    text="Especialidade Médica",
    bg="#EAF4FC",
    font=("Arial",11,"bold")
).pack()

especialidade = tk.StringVar()

combo = ttk.Combobox(
    janela,
    textvariable=especialidade,
    values=list(consultas.keys()),
    state="readonly",
    width=35
)

combo.pack(pady=5)

# ---------------- Consultas Agendadas ----------------

tk.Label(
    janela,
    text="Consultas Agendadas",
    bg="#EAF4FC",
    font=("Arial",11,"bold")
).pack(pady=(15,5))

lista = tk.Listbox(
    janela,
    width=40,
    height=10,
    font=("Arial",11)
)

lista.pack()

def atualizar(event=None):
    lista.delete(0, tk.END)

    esp = especialidade.get()

    if esp in consultas:
        for paciente in consultas[esp]:
            horario = consultas[esp][paciente]["horario"]
            lista.insert(tk.END, f"{horario} - {paciente}")

combo.bind("<<ComboboxSelected>>", atualizar)

# ---------------- Mostrar Consulta ----------------

def mostrar():

    esp = especialidade.get()

    if esp == "":
        messagebox.showwarning("Aviso","Escolha uma especialidade.")
        return

    if not lista.curselection():
        messagebox.showwarning("Aviso","Selecione uma consulta.")
        return

    texto = lista.get(lista.curselection())

    paciente = texto.split(" - ")[1]

    dados = consultas[esp][paciente]

    messagebox.showinfo(
        "Consulta Médica",
        f"""
Paciente: {paciente}

Especialidade: {esp}

Horário: {dados['horario']}

Convênio: {dados['convenio']}

Retorno: {dados['retorno']}

Atendimento Prioritário: {dados['prioridade']}

Queixa:
{dados['queixa']}

Diagnóstico:
{dados['diagnostico']}

Tratamento:
{dados['tratamento']}
"""
    )

# ---------------- Botão ----------------

tk.Button(
    janela,
    text="📋 Visualizar Consulta",
    command=mostrar,
    bg="#28A745",
    fg="white",
    font=("Arial",12,"bold"),
    width=24
).pack(pady=20)

# ---------------- Informações ----------------

tk.Label(
    janela,
    text="""
Como usar:

• Escolha a especialidade médica.
• Selecione uma consulta agendada.
• Clique em Visualizar Consulta.
• Serão exibidos horário, convênio,
  retorno, prioridade, diagnóstico e tratamento.
""",
    bg="#D6EAF8",
    justify="left",
    font=("Arial",10)
).pack(fill="x", padx=20, pady=10)

janela.mainloop()