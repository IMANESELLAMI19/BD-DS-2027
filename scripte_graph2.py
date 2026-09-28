import pandas as pd
import matplotlib.pyplot as plt

# ---------- Données HCP (copiées de la base Excel du titre 2) ----------
df = pd.DataFrame({
    "Année":     [2019, 2020, 2021, 2022, 2023, 2024, 2025],
    "PIB":       [2.6, -7.2, 8.0, 1.5, 3.7, 4.4, 4.9],        # croissance réelle du PIB (%)
    "National":  [9.2, 11.9, 12.3, 11.8, 13.0, 13.3, 13.0],   # chômage national (%)
    "Jeunes":    [24.9, 31.2, 31.8, 32.7, 35.8, 36.7, 37.2],  # chômage 15-24 ans (%)
})

# ---------- Graphique ----------
fig, ax = plt.subplots(figsize=(11, 6.5))

# Barres : croissance du PIB
barres = ax.bar(df["Année"], df["PIB"], width=0.55, color="#90A4AE",
                label="Croissance du PIB (%)", zorder=2)
for x, y in zip(df["Année"], df["PIB"]):
    ax.text(x, y + (0.7 if y >= 0 else -1.8), f"{y:.1f}", ha="center",
            fontsize=9, color="#455A64", fontweight="bold")

# Lignes : chômage
ax.plot(df["Année"], df["National"], marker="o", linewidth=2.5, color="#1565C0",
        label="Chômage national (%)", zorder=3)
ax.plot(df["Année"], df["Jeunes"], marker="o", linewidth=2.5, color="#C62828",
        label="Chômage des 15-24 ans (%)", zorder=3)
for x, y in zip(df["Année"], df["National"]):
    ax.text(x, y + 1.2, f"{y:.1f}", ha="center", fontsize=9, color="#1565C0")
for x, y in zip(df["Année"], df["Jeunes"]):
    ax.text(x, y + 1.2, f"{y:.1f}", ha="center", fontsize=9, color="#C62828")

# Zone : reprise sans recul du chômage
ax.axvspan(2022.5, 2025.5, color="#FFF3E0", alpha=0.8, zorder=0)
ax.text(2024, 23, "Croissance soutenue,\nmais chômage qui ne recule pas",
        ha="center", va="center", fontsize=9.5, style="italic", color="#BF360C")

ax.axhline(0, color="black", linewidth=0.8)
ax.set_ylim(-11, 42)
ax.set_title("Croissance du PIB et chômage au Maroc (2019-2025) :\n"
             "une reprise économique qui ne fait pas reculer le chômage",
             fontsize=13, fontweight="bold")
ax.set_xlabel("Année")
ax.set_ylabel("Pourcentage (%)")
ax.set_xticks(df["Année"])
ax.grid(axis="y", alpha=0.3, zorder=0)
ax.legend(loc="upper left", frameon=True)
fig.text(0.01, 0.01, "Source : Haut-Commissariat au Plan (HCP)", fontsize=8, color="grey")

plt.tight_layout(rect=(0, 0.02, 1, 1))
plt.savefig("croissance_chomage.png", dpi=300)
plt.show()
