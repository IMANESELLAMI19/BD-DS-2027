import pandas as pd
import matplotlib.pyplot as plt

# ---------- Données (copiées de votre base Excel) ----------
donnees = {
    "Année":       [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027],
    "Agriculture": [0.14, -0.186, 0.195, 0.045, -0.039, -0.071, 0.19, -0.118, 0.017, -0.051, 0.071, 0.181, -0.063],
    "Industrie":   [0.018, 0.019, 0.034, 0.031, 0.041, -0.052, 0.078, -0.016, 0.009, 0.038, 0.033, 0.011, 0.037],
    "Services":    [0.021, 0.033, 0.033, 0.029, 0.039, -0.079, 0.057, 0.068, 0.052, 0.056, 0.043, 0.039, 0.042],
    "Type":        ["réel"] * 11 + ["prévision"] * 2,
}
df = pd.DataFrame(donnees)

secteurs = ["Agriculture", "Industrie", "Services"]
for col in secteurs:
    df[col] = df[col] * 100  # 0.14 -> 14 %

reel = df[df["Type"] == "réel"]
prev = pd.concat([reel.tail(1), df[df["Type"] == "prévision"]])

couleurs = {"Agriculture": "#2E7D32", "Industrie": "#1565C0", "Services": "#E65100"}

fig, ax = plt.subplots(figsize=(11, 6))
for s in secteurs:
    ax.plot(reel["Année"], reel[s], marker="o", color=couleurs[s],
            linewidth=2.5 if s == "Agriculture" else 2, label=s)
    ax.plot(prev["Année"], prev[s], marker="o", linestyle="--", color=couleurs[s], linewidth=2)

ax.axhline(0, color="black", linewidth=0.8)
ax.axvspan(2025.5, 2027.3, color="grey", alpha=0.12)
ax.text(2026.4, ax.get_ylim()[1] * 0.9, "Prévisions", ha="center", fontsize=10)

ax.set_title("Valeur ajoutée par secteur dans la croissance du Maroc (2015-2027) :\n"
             "une agriculture très volatile face à des services stables",
             fontsize=13, fontweight="bold")
ax.set_xlabel("Année")
ax.set_ylabel("Croissance de la valeur ajoutée (%)")
ax.set_xticks(df["Année"])
ax.grid(alpha=0.3)
ax.legend(title="Secteur")

plt.tight_layout()
plt.savefig("valeur_ajoutee_secteurs.png", dpi=300)
plt.show()
