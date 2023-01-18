import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# root window
root = tk.Tk()
#definition du titre de l'interface
root.title("Convertisseur de Monnaie")
#definition de la taille de l'interfacce
root.geometry("550x400")
root.configure(background="black")

#label pour le titre
ttk.Label(root, text="Convertisseur de Monnaie", background="black", foreground="white", font=("Time New Roman", 20)).grid(row=0, column=1)

#label pour la valeur à convertir
currency_label = tk.Label(root, text="Montant à convertir:", font=("calibre", 10, "bold"))

#barre d'entrée pour la valeur à convertir
currency = float()
currency_entry = tk.Entry(root, textvariable=currency)

#label pour la valeur convertie
converted_label = tk.Label(root, text="Montant converti", font=("calibre", 10, "bold"))

#barre de lecture pour la valeur convertie
converted_entry = tk.Entry(state="normal")

#liste des devises
devises_list = ["€", "$"]

#variable pour conserver les devises selectionnées
cur = tk.StringVar()
cur.set("€")
conv = tk.StringVar()
conv.set("$")

#definition des menu d'option et la liste de devises à prendre en compte
devisechoosen = tk.OptionMenu(root, cur, *devises_list)
deviseconvert = tk.OptionMenu(root, conv, *devises_list)

#fonction pour convertir
def convert():
    converted_entry.delete(0, "end")
    T_Dollar = 1.09
    T_Euro = 0.92
    conv_Euro = float(currency_entry.get())*T_Dollar
    conv_Dollar = float(currency_entry.get())*T_Euro
    if cur.get() == "€" and conv.get() == "€":
        messagebox.showerror(title="Erreur", message="Erreur, la somme à convertir est déjà dans la devise souhaitée.")
    if cur.get() == "$" and conv.get() == "$":
        messagebox.showerror(title="Erreur", message="Erreur, la somme à convertir est déjà dans la devise souhaitée.")
    if cur.get() == "€" and conv.get() == "$":
        converted_entry.insert(0, round(conv_Euro, 2))
        #print(conv_Euro)
    elif cur.get() == "$" and conv.get() == "€":
        converted_entry.insert(0, round(conv_Dollar, 2))
        #print(conv_Dollar)

#fonction clear
def clear():
    converted_entry.delete(0, "end")

#fonction pour sauvegarder
def save():
    with open("Historique.txt", "a") as text_file:
        text_file.writelines(converted_entry.get())
        text_file.write("\n")
    text_file.close()

#boutton de conversion
convert_btn=tk.Button(root, text="Convertir", command=convert)

#boutton clear
clear_btn =tk.Button(root, text="Clear", bg="red", fg="white", command=clear)

#boutton d'historique
history_btn=tk.Button(root, text="Sauvegarder", bg="grey", fg="white", command=save)

#placement des labels, entrée, boutton et combobox
currency_label.grid(row=1, column=0)
currency_entry.grid(row=1, column=1, ipady=5, pady=10)
devisechoosen.grid(row=1, column=2)
deviseconvert.grid(row=3, column=2)
convert_btn.grid(row=2, column=0)
converted_label.grid(row=3, column=0)
converted_entry.grid(row=3, column=1, ipady=5, pady=10)
clear_btn.grid(row=4, column=1)
history_btn.grid(row=4, column=2)

root.mainloop()