# zero_days_plotter.py
import matplotlib.pyplot as plt
import os

# Dati dalla slide 20 (approssimati dal grafico a torta)
labels = ['Microsoft', 'Google', 'Apple', 'Fortinet', 'Mozilla', 'Sophos', 'Trend Micro', 'Zimbra', 'Other']
sizes = [32.7, 18.2, 16.4, 6.0, 5.0, 4.0, 3.0, 2.0, 12.7] # Assicurati che la somma sia vicina a 100
explode = (0.05, 0, 0, 0, 0, 0, 0, 0, 0)  # Esplodi la prima fetta (Microsoft)

# Colori adatti per tema scuro e leggibili
# Usiamo un colormap che abbia buon contrasto
colors = plt.cm.Pastel1.colors 

# Creazione directory se non esiste
if not os.path.exists('images'):
    os.makedirs('images')

# --- Grafico per Slide 20 ---
plt.style.use('dark_background') # Stile per sfondo scuro

fig1, ax1 = plt.subplots(figsize=(8, 7))
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90, colors=colors,
        textprops={'color': 'white', 'fontsize':9},
        wedgeprops={'edgecolor': 'white', 'linewidth': 0.5}) # Bordo bianco per le fette
ax1.axis('equal')  # Assicura che la torta sia circolare.
plt.title('Zero Days of 2022 by Vendor', color='white', fontsize=14)

plt.savefig('images/zero_days_by_vendor_2022.png', transparent=False, facecolor='black', edgecolor='none')
plt.close(fig1)

print("Grafico 'zero_days_by_vendor_2022.png' generato.")

# --- Grafico per Slide 21 (Istogramma) ---
# Dati approssimati dalla slide 21 (molto approssimati, da aggiornare se si hanno i valori esatti)
years = ['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
# Valori per diverse categorie (es. Microsoft, Google, Adobe, Other)
# Questi sono puramente illustrativi e devono essere accurati
# Supponiamo di avere il totale per ogni anno per semplicità qui
# (Idealmente sarebbe un istogramma stacked)
totals_per_year = [8, 28, 25, 22, 12, 20, 25, 70, 40, 42] 

fig2, ax2 = plt.subplots(figsize=(10, 6))
bars = ax2.bar(years, totals_per_year, color=plt.cm.viridis(0.6), edgecolor='white', linewidth=0.7)

ax2.set_xlabel('Anno', color='white', fontsize=12)
ax2.set_ylabel('Numero di Zero-Day Vulnerabilities', color='white', fontsize=12)
ax2.set_title('Zero-Day Vulnerabilities by Year (Totali Approssimati)', color='white', fontsize=14)
ax2.tick_params(axis='x', colors='white', rotation=45)
ax2.tick_params(axis='y', colors='white')
ax2.grid(axis='y', linestyle='--', alpha=0.5, color='gray')

# Aggiungere etichette ai bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 1, int(yval), va='bottom', ha='center', color='white', fontsize=8)


plt.tight_layout() # Per evitare sovrapposizioni
plt.savefig('images/zero_day_vulnerabilities_by_year.png', transparent=False, facecolor='black', edgecolor='none')
plt.close(fig2)

print("Grafico 'zero_day_vulnerabilities_by_year.png' generato.")