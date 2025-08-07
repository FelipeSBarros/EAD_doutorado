
> Parte de la info aquí redactada proviene de la [Documentación del portal de acceso da los datos](https://www.ambiente.gub.uy/iSIA_OAN/guia.html#formateado).

# Estaciones  
Las `estaciones` de monitoreo son puntos en donde se toman las muestras de manera rutinaria (con frecuencias específicas para cada programa). Son las mismas disponibilizadas en [el geoportal OAN](https://www.ambiente.gub.uy/metadatos/pdf.php?idref=c254). Pueden ser se superfície (394, en todo Uruguay, 11 en Río Negro) o sedimentos (108 en todo Uruguay, 67 en Río Negro), totalizando 502 estaciones en todo Uruguay. En dichas estaciones de monitoreo **no se consideran las estaciones de monitoreo de Aire**. Por otro lado están las [estaciones automáticas](https://www.ambiente.gub.uy/metadatos/pdf.php?idref=c825).
 
Los estaciones o puntos de monitoreo se distinguen según la altura en la columna de agua en que se toman las muestras. Las muestras **superficiales** y de **fondo** se toman en el primer y último metro de profundiad respectivamente. A eso se refiere `Tipo de punto de monitoreo`.

**¿Debemos trabajar con ambos datos, tanto de superfície como de fondo?**

#  Mediciones  
Cada valor reportado, dependiendo de las técnicas e instrumentos utilizados, típicamente tiene límites asociados, conocidos como Límite de Detección (LD) y Límite de Cuantificación (LC).   
* El LD indica el valor mínimo necesario para distinguir lo medido del cero.  
* El LC indica el valor mínimo necesario para lograr una precisión aceptable. 

Los métodos utilizados para cada parámetro ambiental son variables, lo que puede afectar los valores reportados, además de LD y LC. Para el caso de los datos colectados por DINACEA, los métodos utilizados se pueden encontrar en los [compendios de metodologías analíticas](https://www.ambiente.gub.uy/oan/documentos/Compendio_version_VIII_consolidado.pdf), publicados en el OAN.

Cuando se analizan numéricamente datos que incluyen esta información, es necesario establecer criterios para lidiar con los valores del tipo *LD*, *LC*, etc. Se ofrecen dos métodos para tratar con estos elementos.

## Formateo
Los datos descargados con `formateado`, tendrán limpieza básica de los elementos:   
- elimina espacios en blanco y corrige errores de puntuación, cuando los encuentra.

### Formateado `simples`.

* LD cuando el valor que figura es <LD
* LC cuando el valor que figura es <LC
* LC cuando el valor que figura es LD<X<LC
* X cuando el valor que figura es <X (en donde X es un valor numérico)
* X cuando el valor que figura es >X (en donde X es un valor numérico)

Por defecto, en la descarga se incluyen los valores originales, en la columna `valor_original`, al tiempo que la columna `valor_transformado` es creada luego de aplicar el método de limpieza seleccionado. También se incluyen las columnas con LD y LC: `limite_deteccion` y `limite_cuantificacion`.

> Los valores originales son descartados cuando se selecciona la opción Usar formato ancho.

