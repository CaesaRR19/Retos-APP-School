# Ordenado Por ASCII

ASCII es el acrónimo de American Standard Code for Information Interchange. Es el formato de codificación de caracteres más común para datos de texto en computadoras e Internet. Los caracteres en la codificación ASCII incluyen letras mayúsculas y minúsculas (A..Z, a..z), números (0..9) y símbolos de puntuación básicos. En este problema, solo nos interesan los códigos ASCII de las letras mayúsculas y minúsculas del alfabeto inglés. ASCII define un código para cada letra. Las letras mayúsculas ('A'..'Z') tienen asignados códigos que comienzan desde 65 para la letra 'A', 66 para la letra 'B' y así sucesivamente hasta que 90 se asigna a la letra 'Z'. Por otro lado, las letras minúsculas ('a'..'z') tienen asignados códigos que comienzan desde 97 para la letra 'a', 98 para la letra 'b' y así sucesivamente hasta que 122 se asigna a la letra 'z'. Conociendo los códigos ASCII, es posible definir la suma ASCII para una cadena dada como la suma de los códigos ASCII de sus letras. Por ejemplo, la suma ASCII para la cadena 'ABC' es igual a 198 (65+66+67), mientras que la suma ASCII para la cadena 'abD' es igual a 263 (97+98+68). Dada una lista de N cadenas, ordena la lista en orden no descendente según la suma ASCII de las cadenas.

## Entrada

La primera línea contiene un entero 1≤N≤100, que representa el tamaño de la lista. Las siguientes N líneas contienen las cadenas de la lista. Cada cadena tiene como máximo 100 letras minúsculas y mayúsculas del alfabeto inglés.

## Salida

La salida contiene N líneas con la lista ordenada de cadenas. Si hay un empate con la suma de los códigos ASCII de dos cadenas, considera que la cadena con el índice más pequeño (en la lista original) es más pequeña que la cadena con el índice más grande.
