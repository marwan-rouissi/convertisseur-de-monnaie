import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# root window
root = tk.Tk()
#definition du titre de l'interface
root.title("Convertisseur de Monnaie")
#definition de la taille de l'interfacce
root.geometry("600x400")
root.resizable(False,False)
root.configure(background="dark blue")


#label pour le titre
ttk.Label(root, text="Convertisseur de Monnaie", background="dark blue", foreground="white", font=("Time New Roman", 20)).grid(row=0, column=1)

#label pour la valeur à convertir
currency_label = tk.Label(root, text="Montant à convertir:", font=("calibre", 10, "bold"))

#barre d'entrée pour la valeur à convertir
currency = float()
currency_entry = tk.Entry(root, textvariable=currency, justify="right")

#label pour la valeur convertie
converted_label = tk.Label(root, text="Montant converti", font=("calibre", 10, "bold"))

#barre de lecture pour la valeur convertie
converted_entry = tk.Entry(state="normal")

#label pour ajouter des devises
add_dev_label = tk.Label(root, text="Ajouter une devise", font=("calibre", 10, "bold"))

#barre d'entrée pour ajouter des devises
add_dev_entry = tk.Entry(state="normal")

#label pour ajouter le taux de change
add_change_label = tk.Label(root, text="Ajouter le taux de change", font=("calibre", 10, "bold"))

#barre d'entrée pour ajouter le taux de change
add_change_entry = tk.Entry(state="normal")



#liste des devises
devises_list = ["EURO", "USD"]
T_list = [0.92, 1.08]

#variables pour conserver les devises selectionnées
cur = tk.StringVar()
cur.set("Devise")
conv = tk.StringVar()
conv.set("Change")

#definition des menus d'option et la liste de devises à prendre en compte
devisechoosen = tk.OptionMenu(root, cur, *devises_list)
deviseconvert = tk.OptionMenu(root, conv, *devises_list)

#fonction pour convertir
def convert():
    converted_entry.delete(0, "end")
    for i in devises_list:
        if cur.get() == i and conv.get() == i :
            messagebox.showerror(title="Erreur", message="Erreur, la somme à convertir est déjà dans la devise souhaitée.")
        elif cur.get() == devises_list[0] and conv.get() == devises_list[1]:
            convertion = float((1*currency_entry.get()))/float((T_list[0]))
        elif cur.get() == devises_list[1] and conv.get() == devises_list[0]:
            convertion = float((1*currency_entry.get()))/float((T_list[1]))
#derniere condition pour convertir la nouvelle devise ajoutée, connnaissant déjà son taux de change, je l'ai appliquée à la sortie Euro mais également USD
        elif cur.get() == devises_list[2] and conv.get() == devises_list[0]:
            convertion = float((1*currency_entry.get()))/float((T_list[2]))
        elif cur.get() == devises_list[2] and conv.get() == devises_list[1]:
            convertion = float((1*currency_entry.get()))/float((T_list[2]))
    converted_entry.insert(0, round(convertion, 2))
    #print(round(convertion, 2))

#fonction clear
def clear():
    converted_entry.delete(0, "end")

#fonction pour sauvegarder
def save():
    with open("Historique.txt", "a") as text_file:
        text_file.writelines(converted_entry.get() + " " + conv.get() +"" " est le montant converti de " + currency_entry.get() + " " + cur.get())
        text_file.write("\n")
    text_file.close()

#fonction pour ajouter une devise et son taux de change
def add():
    nD = tk.StringVar()
    nD = add_dev_entry.get()
    devises_list.append(nD)
    menu1 = devisechoosen["menu"]
    menu2 = deviseconvert["menu"]
    menu1.delete(0, "end")
    for string in devises_list:
        menu1.add_command(label=string,command=lambda value=string: cur.set(value))
    menu2.delete(0, "end")
    for string in devises_list:
        menu2.add_command(label=string,command=lambda value=string: conv.set(value))
    nT = tk.StringVar()
    nT = add_change_entry.get()
    T_list.append(nT)
    
    #print(devises_list)
    #print(T_list)



#boutton de conversion
convert_btn=tk.Button(root, text="Convertir", bg="yellow",fg="black", command=convert)

#boutton clear
clear_btn =tk.Button(root, text="Clear", bg="red", fg="white", command=clear)

#boutton d'historique
history_btn=tk.Button(root, text="Sauvegarder", bg="orange", fg="black", command=save)

#boutton d'ajout d'une devise et son taux de change
add_btn=tk.Button(root, text="Ajouter", bg="yellow", command=add)

#placement des labels, entrées et bouttons
currency_label.grid(row=1, column=0)
currency_entry.grid(row=1, column=1, ipady=5, pady=10)
devisechoosen.grid(row=1, column=2)
deviseconvert.grid(row=3, column=2)
convert_btn.grid(row=2, column=0)
converted_label.grid(row=3, column=0)
converted_entry.grid(row=3, column=1, ipady=5, pady=10)
clear_btn.grid(row=4, column=1)
history_btn.grid(row=4, column=2)
add_dev_label.grid(pady=5)
add_dev_entry.grid(pady=5)
add_change_label.grid(pady=5)
add_change_entry.grid(pady=5)
add_btn.grid()

root.mainloop()