import tkinter as tk 
from tkinter.scrolledtext import ScrolledText
from PyPDF2 import PdfReader

# Lê PDF
caminhoPdf = r#caminho
leitor = PdfReader(caminhoPdf)

texto = ""
for pagina in leitor.pages:
    pagina_texto = pagina.extract_text()
    if pagina_texto:
        texto += pagina_texto + "\n\n"

# Janela
janela = tk.Tk()
janela.title("Visualizador de PDF")
janela.geometry("900x700")
janela.config(bg="#f0f0f0")  # fundo da janela

modo_noturno = False
invertido = False

# Frame para os botões
frame_botoes = tk.Frame(janela, bg="#f0f0f0")
frame_botoes.pack(fill="x", pady=5)

btn_modo = tk.Button(frame_botoes, text="Modo Noturno", command=lambda: alternar_modo())
btn_modo.pack(side="left", padx=5)

btn_inverter = tk.Button(frame_botoes, text="Inverter Texto", command=lambda: inverter_texto())
btn_inverter.pack(side="left", padx=5)

# Caixa de texto
caixaTxt = ScrolledText(janela, wrap=tk.WORD)
caixaTxt.pack(expand=True, fill="both")
caixaTxt.insert(tk.END, texto)
caixaTxt.config(state="disabled")

# Função de Modo Noturno
def alternar_modo():
    global modo_noturno
    modo_noturno = not modo_noturno
    if modo_noturno:
        caixaTxt.config(bg="black", fg="white", insertbackground="white")
    else:
        caixaTxt.config(bg="white", fg="black", insertbackground="black")

# Função de inverter texto
def inverter_texto():
    global invertido
    invertido = not invertido
    caixaTxt.config(state="normal")
    caixaTxt.delete(1.0, tk.END)
    
    if invertido:
        # Inverte todas as linhas do texto horizontalmente
        linhas = texto.splitlines()
        linhas_invertidas = [linha[::-1] for linha in linhas]
        caixaTxt.insert(tk.END, "\n".join(linhas_invertidas))
    else:
        caixaTxt.insert(tk.END, texto)
    
    caixaTxt.config(state="disabled")

# Aplica tema inicial
alternar_modo()  # para começar no modo claro

janela.mainloop()
