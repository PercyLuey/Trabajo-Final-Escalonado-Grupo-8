# Plan algorítmico para T2

## Alcance de ingeniería

El sistema se plantea como un **metamodelo de preevaluación** que aproxima respuestas ya calculadas por el dataset. No reemplaza un análisis modal espectral, tiempo-historia, no lineal ni la verificación con la norma sismorresistente aplicable.

## Variables objetivo y flujo

Se priorizan dos regresiones: distorsión máxima de entrepiso y desplazamiento máximo de techo. Como objetivos secundarios se evaluarán cortante basal, aceleración estructural, índice de daño y probabilidad de colapso.

1. Separar las variables de entrada de las seis columnas `Predicted` para evitar fuga de información.
2. Dividir entrenamiento/prueba en 80/20 con semilla documentada y repetir semillas para estabilidad PCS.
3. Imputar numéricas con mediana y categóricas con moda, aunque la versión actual no contiene nulos.
4. Aplicar One-Hot Encoding y escalar numéricas solo para modelos que lo requieren.
5. Comparar DummyRegressor, Ridge, Random Forest y Gradient Boosting.
6. Considerar una red neuronal solo como extensión, por el tamaño reducido de 1,000 observaciones.
7. Explicar el modelo final mediante importancia por permutación y dependencia parcial.

## Métricas y selección

Se usarán MAE (principal), RMSE y R²; MAPE solo si no hay valores cercanos a cero. Se aplicará validación cruzada de cinco pliegues en entrenamiento y una prueba final intacta. El modelo elegido debe superar al ingenuo, mantener errores estables, no sobreajustar y mostrar relaciones físicamente razonables. No se fijan cifras de desempeño antes del entrenamiento.
