import tkinter as tk

janela = tk.Tk()
janela.title("Aproveitamento Escolar")
janela.geometry("380x280")
janela.configure(bg="#F5F0FF")
janela.resizable(False, False)

tk.Label(
    janela,
    text="🎓 Aproveitamento Escolar",
    font=("Arial", 14, "bold"),
    bg="#F5F0FF",
    fg="#7B2CBF"
).pack(pady=20)

# Variável da nota
var_nota = tk.DoubleVar(value=70)

# Barra de nota
scale = tk.Scale(
    janela,
    variable=var_nota,
    from_=0,
    to=100,
    resolution=1,
    orient="horizontal",
    length=280,
    label="Nota",
    font=("Arial", 10),
    bg="#F5F0FF",
    fg="#7B2CBF",
    troughcolor="#A9D6FF",
    activebackground="#FF99C8"
)
scale.pack(pady=10)

def mostrar():
    nota = var_nota.get()

    if nota <= 59:
        resultado = "❌ Reprovado"
    elif nota <= 79:
        resultado = "⚠️ Recuperação"
    else:
        resultado = "✅ Aprovado"

    label_resultado.config(
        text=f"{resultado}\nNota: {int(nota)}"
    )

label_resultado = tk.Label(
    janela,
    text="⚠️ Recuperação\nNota: 70",
    font=("Arial", 12),
    bg="#F5F0FF",
    fg="#7B2CBF"
)
label_resultado.pack(pady=10)

tk.Button(
    janela,
    text="Ver Resultado",
    command=mostrar,
    bg="#C77DFF",
    fg="white",
    font=("Arial", 11, "bold"),
    width=16,
    relief="flat",
    cursor="hand2"
).pack(pady=8)

janela.mainloop()