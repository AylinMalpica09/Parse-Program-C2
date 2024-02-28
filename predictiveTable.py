predictive_table = {
    ('S', 'automata'): ['A', 'B', 'V'],
    ('A', 'automata'): ['automata'],
    ('V', 'fin'): ['fin'],
    ('B', 'alfabeto'): ['AL', 'F'],
    ('AL', 'alfabeto'): ['G', ':', 'SM', 'RA', ';'],
    ('G', 'alfabeto'): ['alfabeto'],
    ('SM', 'letters'): ['letters'],
    ('SM', 'digit'): ['digit'],
    ('RA', ','): [',', 'SM', 'RA'],
    ('RA', ';'): ['epsilon'],
    ('RA', ':'): [':'],  
    ('F', 'aceptacion'): ['aceptacion', ':', 'D', ';', 'fin'],  # ajustamos la regla para seguir con 'aceptacion' después de ';'
    ('F', 'fin'): ['fin'],
    (':', 'letters'): ['letters'],
    (':', 'digit'): ['digit'],
    ('C', 'aceptacion'): ['aceptacion', ':', 'D', ';', 'fin'],  # Después de 'aceptacion', se espera ':' seguido de 'D', ';' y 'fin'
    (':', 'aceptacion'): ['D'],
    ('D', 'digit'): ['digit'],
    ('D', ';'): [';'],
    (';', ';'): ['V'],  # Después de ';', avanzamos a 'V'
    ('V', '$'): ['epsilon']
}
