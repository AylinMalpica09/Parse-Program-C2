parser_table = {
    ('S', 'automata'): ['A', 'B', 'V'],
    ('A', 'automata'): ['automata'],
    ('V', 'fin'): ['fin'],
    ('B', 'alfabeto'): ['AL', 'F'],
    ('AL', 'alfabeto'): ['G', ':', 'SM', 'RA', ';'],
    ('G', 'alfabeto'): ['alfabeto'],
    ('SM', 'alpha'): ['alpha'],
    ('SM', 'digit'): ['digit'],
    ('RA', ','): [',', 'SM', 'RA'],
    ('RA', ';'): ['epsilon'],
    ('RA', ':'): [':'],  
    ('F', 'aceptacion'): ['aceptacion', ':', 'D', ';', 'fin'],  # ajustamos la regla para seguir con 'aceptacion' después de ';'
    ('F', 'fin'): ['fin'],
    (':', 'alpha'): ['alpha'],
    (':', 'digit'): ['digit'],
    ('C', 'aceptacion'): ['aceptacion', ':', 'D', ';', 'fin'],  # Después de 'aceptacion', se espera ':' seguido de 'D', ';' y 'fin'
    (':', 'aceptacion'): ['D'],
    ('D', 'digit'): ['digit'],
    ('D', ';'): [';'],
    (';', ';'): ['V'],  # Después de ';', avanzamos a 'V'
    ('V', '$'): ['epsilon']
}


terminales = set([clave[1] for clave in parser_table.keys()])
palabras_reservadas = ['automata', 'alfabeto', 'aceptacion', 'fin']

def organizador(palabras):
    simbolos = []
    for palabra in palabras:
        if palabra in palabras_reservadas:
            simbolos.append(palabra)
        else:
            for letra in palabra:
                if letra.isalpha():
                    simbolos.append('alpha')
                elif letra.isdigit():
                    simbolos.append('digit')
                else:
                    simbolos.append(letra)
    return simbolos

def analizador_sintactico(entrada):
    stack = ['$', 'S']
    text = str(stack) + '\n'
    entrada = entrada.strip() + ' $'
    palabras = entrada.split(' ')
    simbolos = organizador(palabras)
    index = 0
    while True:
        X = stack.pop()
        a = simbolos[index]
        if X in terminales:
            if X == a:
                index += 1
                if X == '$':
                    return text + "Lectura completada: entrada válida"
            else:
                return text + '\nError de sintaxis: se esperaba "{}" pero se encontró "{}"'.format(X, a)
        else:
            if (X, a) in parser_table:
                producciones = parser_table[(X, a)]
                if producciones != ['epsilon']:
                    for produccion in reversed(producciones):
                        if produccion != 'epsilon':
                            stack.append(produccion)
                text += str(stack) + '\n'
            else:
                return text + '\nError de sintaxis: no hay regla en la tabla para "{}", "{}"'.format(X, a)

