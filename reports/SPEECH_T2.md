# Speech de sustentación T2 (5 minutos)

## 0:00–0:40 | Problema

Buenos días. Nuestro proyecto busca construir un metamodelo de preevaluación de respuesta sísmica de edificaciones. Desde ingeniería civil, el objetivo no es reemplazar ETABS, SAP2000 ni una verificación normativa, sino obtener una estimación rápida que permita priorizar escenarios antes de ejecutar análisis estructurales más costosos.

## 0:40–1:25 | Datos

Trabajamos con el “Pre-Earthquake Prediction Dataset” de Kaggle. La versión completa contiene 1,000 registros y 26 variables: 20 numéricas y 6 categóricas. Integra amenaza sísmica, condiciones de suelo, propiedades del edificio y seis respuestas calculadas: deriva, desplazamiento de techo, cortante basal, aceleración, daño y probabilidad de colapso.

## 1:25–2:25 | Limpieza y EDA

El código en Python carga directamente el CSV y genera un diagnóstico reproducible. Verificamos tipos, nulos, duplicados, estadísticos y categorías. Encontramos cero nulos y cero duplicados. Luego analizamos distribuciones, correlaciones de Spearman y respuestas por material, suelo y sistema resistente. La correlación detecta asociaciones, no causalidad. Las columnas objetivo se separarán para evitar fuga de información.

## 2:25–3:25 | Algoritmos

En T3 comenzaremos con un modelo ingenuo y Ridge. Después compararemos Random Forest y Gradient Boosting porque capturan relaciones no lineales entre demanda sísmica, suelo, rigidez y configuración. Una red neuronal será opcional: con solo 1,000 observaciones podría sobreajustar. El preprocesamiento se integrará en pipelines reproducibles.

## 3:25–4:20 | Resultados previstos y PCS

Esperamos que los ensambles mejoren las líneas base, pero no afirmamos cifras antes de entrenar. Mediremos MAE, RMSE y R cuadrado; reservaremos 20% de prueba y aplicaremos validación cruzada. PCS se cubrirá con predictibilidad en datos no vistos, computabilidad del flujo y estabilidad ante distintas semillas y decisiones de preprocesamiento.

## 4:20–5:00 | Limitación y cierre

Las salidas están rotuladas como “Predicted”, por lo que probablemente proceden de simulación o de un modelo previo, no de instrumentación real. El resultado es una demostración académica de metamodelado. Para uso profesional se requeriría validar con registros, modelos estructurales trazables y la norma aplicable. Entregamos el dataset completo, código, figuras, plan e informe consolidado.
