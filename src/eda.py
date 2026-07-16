"""Análisis exploratorio reproducible del dataset sísmico del Grupo 8."""
from __future__ import annotations
import json
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "raw" / "seismic_data.csv"
OUT, FIG = ROOT / "outputs", ROOT / "outputs" / "figures"
TARGETS = ["Predicted Max Inter-Story Drift Ratio (%)", "Predicted Max Roof Displacement (m)",
           "Predicted Base Shear Force (kN)", "Predicted Structural Acceleration (m/s²)",
           "Predicted Damage Index (0–1 Scale)", "Predicted Collapse Probability (%)"]

def save_figure(name: str) -> None:
    plt.tight_layout(); plt.savefig(FIG / name, dpi=180, bbox_inches="tight"); plt.close()

def main() -> None:
    FIG.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(DATA)
    numeric, categorical = df.select_dtypes(include=np.number), df.select_dtypes(exclude=np.number)
    pd.DataFrame({"tipo": df.dtypes.astype(str), "nulos": df.isna().sum(),
                  "nulos_pct": (100 * df.isna().mean()).round(2),
                  "unicos": df.nunique(dropna=False)}).to_csv(OUT / "data_quality.csv", encoding="utf-8-sig")
    numeric.describe().T.to_csv(OUT / "numeric_summary.csv", encoding="utf-8-sig")
    categorical.describe().T.to_csv(OUT / "categorical_summary.csv", encoding="utf-8-sig")
    corr = numeric.corr(method="spearman")
    corr.to_csv(OUT / "spearman_correlations.csv", encoding="utf-8-sig")
    target_corr = corr[TARGETS].drop(index=TARGETS, errors="ignore")
    summary = {"filas": int(len(df)), "columnas": int(df.shape[1]),
               "numericas": int(numeric.shape[1]), "categoricas": int(categorical.shape[1]),
               "nulos": int(df.isna().sum().sum()), "duplicados": int(df.duplicated().sum()),
               "memoria_mb": round(float(df.memory_usage(deep=True).sum() / 1024**2), 3),
               "variables_categoricas": {c: sorted(df[c].astype(str).unique().tolist()) for c in categorical},
               "correlaciones_fuertes_por_objetivo": {t: target_corr[t].abs().sort_values(ascending=False).head(5).index.tolist() for t in TARGETS}}
    (OUT / "eda_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    sns.set_theme(style="whitegrid", context="notebook")
    axes = df[TARGETS].hist(figsize=(12, 8), bins=24, color="#2E74B5", edgecolor="white")
    for row in axes:
        for ax in row: ax.set_ylabel("Frecuencia")
    plt.suptitle("Distribución de las respuestas estructurales", y=1.02, fontsize=14); save_figure("01_distribucion_objetivos.png")
    plt.figure(figsize=(12, 10)); sns.heatmap(corr, cmap="vlag", center=0, vmin=-1, vmax=1, cbar_kws={"label": "ρ de Spearman"})
    plt.title("Correlación de Spearman entre variables numéricas"); plt.xticks(rotation=75, ha="right", fontsize=7); plt.yticks(fontsize=7); save_figure("02_matriz_correlacion.png")
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8))
    sns.boxplot(data=df, x="Structural Material", y=TARGETS[0], ax=axes[0], color="#9DC3E6"); axes[0].set_title("Deriva por material estructural"); axes[0].tick_params(axis="x", rotation=25)
    sns.boxplot(data=df, x="Lateral Load Resisting System", y=TARGETS[4], ax=axes[1], color="#A9D18E"); axes[1].set_title("Índice de daño por sistema lateral"); axes[1].tick_params(axis="x", rotation=25); save_figure("03_respuesta_por_sistema.png")
    plt.figure(figsize=(8, 5.5)); sns.scatterplot(data=df, x="PGA (m/s²)", y=TARGETS[3], hue="Soil Type", alpha=0.75)
    plt.title("Demanda sísmica y aceleración estructural"); save_figure("04_pga_aceleracion.png")
    print(json.dumps(summary, ensure_ascii=False, indent=2))

if __name__ == "__main__": main()
