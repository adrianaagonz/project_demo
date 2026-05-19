## Plantilla de README

### 1) Objetivo
- Analizar y visualizar un dataset de demostración para entender el proceso de limpieza de datos, construcción de características y generación de visualizaciones.

### 2) Dataset
- Fuente: sephora_products.csv
- Nº filas/columnas: 12 columnas y 4.300 filas
- Variables clave: 'brand_name' (marca), 'product_name'(nombre del producto), 'price_usd' (precio original), 'sale_price_usd' (precio de venta), 'rating' (puntuación), 'reviews' (reseñas), 'love_count' (faoritos).

### 3) Preguntas
- Q1: ¿Cómo se distribuyen los precios de los productos en la plataforma de Sephora?
- Q2: ¿Cuales son las marcas de cométicos que ofrecen el mayor volumen de productos?
- Q3: ¿Existe una relación o correlación clara entre la puntuación en estrellas de un producto y su número total de reseñas?
- Q4: ¿Cuales son los productos específicos que se posicionan como los favoritos absolutos de los usuarios ("most lovers")?

### 4) Data issues & fixes
- Valores faltantes → Limpieza y imputación en src/cleaning.py
- Datos inconsistentes → Normalización y corrección
- Formatos incorrectos → Conversión de tipos de datos

### 5) Pipeline
- raw → clean → features → viz → (export opcional a `data/processed/`)

### 6) Hallazgos
- Insight 1: Distribución de precios. Al analizar el grafico de precios, la gran mayoría de los productos de sephora se concentran fuertemente en el rango de los $20 a $50 USD. Esto demuestra que el modelo de negocio de la plataforma se centra  principalmente en el segmento del "lujo accesible", dejando los precios más altos para líneas exclusivas de cuidado de piel y perfumes premium.
- Insight 2: Dominio de marcas. El gráfico de barras revela que el volumen del catálogo está claramente dominado por marcas como *Sephora Collection* y *Clinique*. Esto refleja una estrategia comercial enfocada en ofrecer un gran volumen de productos de marca propia asequibles junto con nombres clínicos de alta confianza para asegurar una alta rotación.
- Insight 3 y 4: El fenómeno de los productos de culto. El nivel de favoritos de los usuarios (`loves_count`) no crece de forma lineal con el precio o la puntuación, y el gráfico de dispersión muestra que no hay una correlación directa con el número de reseñas. Un grupo selecto de productos icónicos rompe completamente las métricas con millones de favoritos, lo que demuestra la existencia de productos "de culto" que generan una altísima fidelidad en la plataforma por encima de cualquier otra variable.

### 7) Estructura del proyecto
- `src/` contiene funciones reutilizables (`io`, `cleaning`, `features`, `viz`)
- `main.py` ejecuta el pipeline end-to-end

### 8) Cómo ejecutar
- `pip install -r requirements.txt`
- Ejecutar pipeline: `python main.py`
- (Opcional) Abrir y ejecutar: `notebooks/eda.ipynb`

## Estructura recomendada del proyecto

Regla: el notebook **explica** y **orquesta**. El código repetible va a `src/`.

Estructura sugerida:

```
project/
├── main.py
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── eda.ipynb
├── src/
│   ├── __init__.py
│   ├── io.py
│   ├── cleaning.py
│   ├── config.py
│   ├── features.py
│   ├── viz.py
│   └── utils.py
├── README.md
├── .gitignore
└── requirements.txt

```