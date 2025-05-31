import os

import matplotlib.pyplot as plt

# Creazione della cartella images se non esiste
if not os.path.exists("images"):
    os.makedirs("images")

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
square_size = len(alphabet)

# Creazione della Tabula Recta
vigenere_data = []
for i in range(square_size):
    row = []
    for j in range(square_size):
        row.append(alphabet[(i + j) % square_size])
    vigenere_data.append(row)

# Creazione della figura e dell'asse con sfondo scuro
fig, ax = plt.subplots(figsize=(10, 10))
fig.patch.set_facecolor("#141414")  # Sfondo scuro per la figura
ax.set_facecolor("#141414")  # Sfondo scuro per l'asse

# Nascondere gli assi
ax.axis("off")

# Creazione della tabella
table = ax.table(
    cellText=vigenere_data,
    rowLabels=[l for l in alphabet],
    colLabels=[l for l in alphabet],
    loc="center",
    cellLoc="center",
)

# Stile della tabella per tema scuro
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1.1, 1.1)  # Scala la tabella per adattarla meglio

for key, cell in table.get_celld().items():
    cell.set_edgecolor("gray")  # Bordi delle celle
    if key[0] == 0 or key[1] == -1:  # Intestazioni di riga/colonna
        cell.set_text_props(weight="bold", color="cyan")
        cell.set_facecolor("#2a2a2a")  # Sfondo leggermente diverso per le intestazioni
    else:  # Celle dati
        cell.set_text_props(color="white")
        cell.set_facecolor("#1e1e1e")  # Sfondo scuro per le celle dati


ax.set_title("Tabula Recta (Quadrato di Vigenère)", fontsize=16, color="white", pad=20)

plt.tight_layout()

# Salva l'immagine
output_path = os.path.join("images", "vigenere_square.png")
plt.savefig(
    output_path, facecolor=fig.get_facecolor(), bbox_inches="tight", pad_inches=0.1
)
print(f"Quadrato di Vigenere salvato in {output_path}")

# plt.show() # Opzionale
