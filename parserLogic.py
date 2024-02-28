from predictiveTable import predictive_table


terminales = set([clave[1] for clave in predictive_table.keys()])
palabras_reservadas = ['automata', 'alfabeto', 'aceptacion', 'fin']

def organizador(palabras):
    simbolos = []
    for palabra in palabras:
        if palabra in palabras_reservadas:
            simbolos.append(palabra)
        else:
            for letra in palabra:
                if letra.isalpha():
                    simbolos.append('letters')
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
            if (X, a) in predictive_table:
                producciones = predictive_table[(X, a)]
                if producciones != ['epsilon']:
                    for produccion in reversed(producciones):
                        if produccion != 'epsilon':
                            stack.append(produccion)
                text += str(stack) + '\n'
            else:
                return text + '\nError de sintaxis: no hay regla en la tabla para "{}", "{}"'.format(X, a)
