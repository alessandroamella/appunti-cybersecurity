import os

import matplotlib.pyplot as plt

# Dati di frequenza approssimativi per l'inglese (da slide/fonti comuni)
letters = [
    "E",
    "T",
    "A",
    "O",
    "I",
    "N",
    "S",
    "H",
    "R",
    "D",
    "L",
    "C",
    "U",
    "M",
    "W",
    "F",
    "G",
    "Y",
    "P",
    "B",
    "V",
    "K",
    "J",
    "X",
    "Q",
    "Z",
]
frequencies = [
    0.127,
    0.091,
    0.082,
    0.075,
    0.070,
    0.067,
    0.063,
    0.060,
    0.043,
    0.040,
    0.028,
    0.028,
    0.024,
    0.023,
    0.022,
    0.020,
    0.020,
    0.019,
    0.015,
    0.010,
    0.008,
    0.002,
    0.002,
    0.001,
    0.001,
    0.001,
]

# Creazione della cartella images se non esiste
if not os.path.exists("images"):
    os.makedirs("images")

# Stile per dark theme
plt.style.use("dark_background")  # Usa uno stile scuro predefinito

fig, ax = plt.subplots(figsize=(12, 6))

# Bar chart
bars = ax.bar(letters, frequencies, color="cyan")

# Titoli e label con colori chiari
ax.set_title(
    "Frequenza Approssimativa delle Lettere in Inglese", fontsize=16, color="white"
)
ax.set_xlabel("Lettera", fontsize=14, color="white")
ax.set_ylabel("Frequenza", fontsize=14, color="white")

# Colori per tick e spine
ax.tick_params(axis="x", colors="white")
ax.tick_params(axis="y", colors="white")
ax.spines["bottom"].set_color("white")
ax.spines["top"].set_color("grey")  # o 'none'
ax.spines["left"].set_color("white")
ax.spines["right"].set_color("grey")  # o 'none'


plt.xticks(rotation=0)  # Mantiene le label orizzontali
plt.tight_layout()  # Adegua il layout per evitare sovrapposizioni

# Salva l'immagine
output_path = os.path.join("images", "freq_analysis_chart.png")
plt.savefig(
    output_path, facecolor=fig.get_facecolor()
)  # Salva con lo sfondo della figura
print(f"Grafico salvato in {output_path}")

# plt.show() # Opzionale per visualizzare il grafico
