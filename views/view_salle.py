import customtkinter as ctk
from services.services_salle import ServiceSalle
from tkinter import ttk
from models.salle import Salle
import tkinter.font as tkfont

class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gestion des Salles")
        self.geometry("700x800")
        self.service_salle = ServiceSalle()
        self.setup_ui()
        self.lister_salles()

    def setup_ui(self):

        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 12), rowheight=30)
        style.configure("Treeview.Heading", font=("ALGERIANS", 13, "bold"))

        self.frame_form = ctk.CTkFrame(self)
        self.frame_form.pack(pady=20, padx=20, fill="x")

        ctk.CTkLabel(self.frame_form, text="Code:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_code = ctk.CTkEntry(self.frame_form, width=150)
        self.entry_code.grid(row=0, column=1, padx=10, pady=5)

        ctk.CTkLabel(self.frame_form, text="Description:").grid(row=0, column=2, padx=10, pady=5, sticky="e")
        self.entry_desc = ctk.CTkEntry(self.frame_form, width=150)
        self.entry_desc.grid(row=0, column=3, padx=10, pady=5)

        ctk.CTkLabel(self.frame_form, text="Catégorie:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_cat = ctk.CTkEntry(self.frame_form, width=150)
        self.entry_cat.grid(row=1, column=1, padx=10, pady=5)

        ctk.CTkLabel(self.frame_form, text="Capacité:").grid(row=1, column=2, padx=10, pady=5, sticky="e")
        self.entry_cap = ctk.CTkEntry(self.frame_form, width=150)
        self.entry_cap.grid(row=1, column=3, padx=10, pady=5)

        self.frame_btns = ctk.CTkFrame(self)
        self.frame_btns.pack(pady=10, padx=20, fill="x")

        self.btn_add = ctk.CTkButton(self.frame_btns, text="Ajouter", command=self.action_ajouter)
        self.btn_add.pack(side="left", padx=20, pady=10, expand=True)

        self.btn_update = ctk.CTkButton(self.frame_btns, text="Modifier", command=self.action_modifier)
        self.btn_update.pack(side="left", padx=20, pady=10, expand=True)

        self.btn_search = ctk.CTkButton(self.frame_btns, text="Rechercher", command=self.action_rechercher)
        self.btn_search.pack(side="left", padx=20, pady=10, expand=True)

        self.btn_delete = ctk.CTkButton(self.frame_btns, text="Supprimer", fg_color="#E74C3C", hover_color="#C0392B",command=self.action_supprimer)
        self.btn_delete.pack(side="left", padx=20, pady=10, expand=True)

        # Cadre Liste des salles
        self.cadreList = ctk.CTkFrame(self, corner_radius=10)
        self.cadreList.pack(pady=10, padx=20, fill="both", expand=True)

        self.treeList = ttk.Treeview(self.cadreList, columns=("code", "description", "categorie", "capacite"),show="headings")

        # En-têtes visibles
        self.treeList.heading("code", text="CODE")
        self.treeList.heading("description", text="Description")
        self.treeList.heading("categorie", text="Catégorie")
        self.treeList.heading("capacite", text="Capacité")

        self.treeList.column("code", width=80, anchor="center")
        self.treeList.column("description", width=200)
        self.treeList.column("categorie", width=120)
        self.treeList.column("capacite", width=80, anchor="center")

        self.treeList.pack(expand=True, fill="both", padx=10, pady=10)

        self.treeList.bind("<<TreeviewSelect>>", self.remplir_champs)

    def lister_salles(self):

        for item in self.treeList.get_children():
            self.treeList.delete(item)

        liste = self.service_salle.recuperer_salles()

        for s in liste:
            self.treeList.insert("", "end", values=(s.codes, s.descriptions, s.categorie, s.capacite))

    def action_ajouter(self):
        try:
            cap = int(self.entry_cap.get())
            s = Salle(self.entry_code.get(), self.entry_desc.get(), self.entry_cat.get(), cap)
            succes, msg = self.service_salle.ajouter_salle(s)
            print(msg)
            self.lister_salles()
        except ValueError:
            print("Erreur : La capacité doit être un nombre.")

    def action_modifier(self):
        try:
            cap = int(self.entry_cap.get())
            salle_modifiee = Salle(self.entry_code.get(), self.entry_desc.get(), self.entry_cat.get(), cap)
            succes, msg = self.service_salle.modifier_salle(salle_modifiee)
            if succes:
                self.lister_salles()
            print(msg)
        except ValueError:
            print("Erreur : Données numériques invalides.")

    def action_rechercher(self):

        code = self.entry_code.get()
        if not code:
            print("Veuillez entrer un code pour rechercher.")
            return

        salle = self.service_salle.rechercher_salle(code)

        if salle:
            for item in self.treeList.get_children():
                self.treeList.delete(item)

            self.treeList.insert("", "end", values=(salle.codes, salle.descriptions, salle.categorie, salle.capacite))

    def action_supprimer(self):
        selection = self.treeList.selection() # Corrigé tree -> treeList
        if selection:
            item = self.treeList.item(selection)
            code = item['values'][0]
            self.service_salle.supprimer_salle(code)
            self.lister_salles()
            print(f"La salle {code} a été supprimée.")
        else:
            print("Veuillez sélectionner une salle.")

    def remplir_champs(self, event):
        selection = self.treeList.selection()
        if selection:
            item = self.treeList.item(selection)
            v = item.get('values', [])  # .get() évite un plantage si 'values' manque

            # On vérifie qu'on a bien nos 4 colonnes avant de remplir
            if len(v) >= 4:

                self.entry_code.delete(0, 'end')
                self.entry_code.insert(0, v[0])

                self.entry_desc.delete(0, 'end')
                self.entry_desc.insert(0, v[1])

                self.entry_cat.delete(0, 'end')
                self.entry_cat.insert(0, v[2])

                self.entry_cap.delete(0, 'end')
                self.entry_cap.insert(0, v[3])
