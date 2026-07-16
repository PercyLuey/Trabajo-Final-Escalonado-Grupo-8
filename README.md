# Predicción de respuesta sísmica mediante Machine Learning

Trabajo Final Escalonado - Grupo 8, curso **Aplicaciones de IA en Estructuras**.

## Integrantes

- Percy Luey Espinoza
- Delarc Dario Ayala Cacha
- Martin Eduardo Suarez Cruz

## Objetivo

Desarrollar un metamodelo académico para estimar rápidamente respuestas sísmicas globales de edificaciones a partir de variables de amenaza, sitio y configuración estructural. Es una herramienta de preevaluación; no sustituye el análisis estructural ni la comprobación normativa.

## Contenido

- `data/raw/seismic_data.csv`: dataset completo de Kaggle (1,000 filas, 26 columnas).
- `src/eda.py`: análisis exploratorio reproducible.
- `outputs/figures/`: visualizaciones generadas.
- `reports/T1-Grupo 8.docx`: informe entregado en T1.
- `reports/Informe_T2_Grupo_8.docx`: informe consolidado hasta T2.
- `reports/PLAN_ALGORITMICO_T2.md`: modelos, validación y métricas.

## Ejecución

```bash
python -m pip install -r requirements.txt
python src/eda.py
```

El script produce resúmenes de calidad, estadísticos, correlaciones y cuatro figuras. Fuente: [Pre-Earthquake Prediction Dataset](https://www.kaggle.com/datasets/ziya07/pre-earthquake-prediction-dataset), licencia CC0.

## Estado

- T1: planteamiento, datos y marco PCS incorporados.
- T2: limpieza, EDA, plan algorítmico y resultados previstos incorporados.
- T3: pendiente de entrenamiento, comparación, explicabilidad y validación final.
