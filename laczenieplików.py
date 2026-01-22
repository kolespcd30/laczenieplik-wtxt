import os
from tkinter import Tk, filedialog, messagebox, ttk, scrolledtext
import tkinter as tk

def wybierz_pliki():
    pliki = filedialog.askopenfilenames(
        title="Wybierz pliki .txt do połączenia",
        filetypes=[("Pliki tekstowe", "*.txt"), ("Wszystkie pliki", "*.*")]
    )
    return list(pliki)

def wybierz_folder():
    folder = filedialog.askdirectory(title="Wybierz folder z plikami .txt")
    if folder:
        pliki = [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith('.txt')]
        pliki.sort()
        return pliki
    return []

def polacz_pliki(pliki, plik_wynikowy):
    try:
        with open(plik_wynikowy, 'w', encoding='utf-8') as wyjscie:
            for i, sciezka in enumerate(pliki):
                nazwa = os.path.basename(sciezka)
                wyjscie.write(f"\n{'='*60}\n")
                wyjscie.write(f"PLIK {i+1}: {nazwa}\n")
                wyjscie.write(f"{'='*60}\n\n")
                
                with open(sciezka, 'r', encoding='utf-8', errors='ignore') as f:
                    wyjscie.write(f.read())
                    wyjscie.write("\n\n")  # odstęp między plikami
        
        messagebox.showinfo("Sukces!", f"Pomyślnie połączono {len(pliki)} plików!\nZapisano jako:\n{plik_wynikowy}")
    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się zapisać pliku:\n{e}")

def start():
    wybor = var.get()
    
    if wybor == 1:
        pliki = wybierz_pliki()
    else:
        pliki = wybierz_folder()
    
    if not pliki:
        messagebox.showwarning("Brak plików", "Nie wybrano żadnych plików .txt")
        return
    
    domyslna_nazwa = f"podsumowanie_{len(pliki)}_omsi.txt"
    
    plik_wynikowy = filedialog.asksaveasfilename(
        title="Zapisz połączony plik jako...",
        defaultextension=".txt",
        initialfile=domyslna_nazwa,
        filetypes=[("Plik tekstowy", "*.txt")]
    )
    
    if plik_wynikowy:
        polacz_pliki(pliki, plik_wynikowy)
        lista_plikow.delete(1.0, tk.END)
        for p in pliki:
            lista_plikow.insert(tk.END, os.path.basename(p) + "\n")

root = Tk()
root.title("Łącznik plików .txt")
root.geometry("600x500")
root.resizable(True, True)

tk.Label(root, text="Łącznik plików tekstowych (.txt)", font=("Arial", 16, "bold")).pack(pady=10)

var = tk.IntVar(value=1)

frame_wybor = tk.Frame(root)
frame_wybor.pack(pady=10)

tk.Radiobutton(frame_wybor, text="Wybierz pojedyncze pliki", variable=var, value=1).pack(side=tk.LEFT, padx=20)
tk.Radiobutton(frame_wybor, text="Wybierz cały folder", variable=var, value=2).pack(side=tk.LEFT, padx=20)

tk.Button(root, text="ROZPOCZNIJ ŁĄCZENIE", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", command=start).pack(pady=20)

tk.Label(root, text="Połączone pliki będą widoczne tutaj:", font=("Arial", 10)).pack(anchor="w", padx=20)
lista_plikow = scrolledtext.ScrolledText(root, height=12, font=("Consolas", 10))
lista_plikow.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

tk.Label(root, text="© 2025 – Prosta aplikacja do łączenia .txt w Pythonie", fg="gray").pack(side=tk.BOTTOM, pady=10)

root.mainloop()
