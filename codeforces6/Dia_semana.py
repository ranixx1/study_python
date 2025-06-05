#Escreva uma função que receba que dia da semana é hoje e em quantos dias ocorre um determinado evento e retorne que dia da semana é o evento.
def dia_da_semana(h, d):
    # 1. Mapea dias da semana para números
    dias_para_numero = {
        "Domingo": 0,
        "Segunda-feira": 1,
        "Terca-feira": 2,
        "Quarta-feira": 3,
        "Quinta-feira": 4,
        "Sexta-feira": 5,
        "Sabado": 6
    }

    # 2. Mapea números para dias da semana 
    numero_para_dias = [
        "Domingo",
        "Segunda-feira",
        "Terca-feira",
        "Quarta-feira",
        "Quinta-feira",
        "Sexta-feira",
        "Sabado"
    ]

    numero_dia_hoje = dias_para_numero[h]

    numero_dia_evento = (numero_dia_hoje + d) % 7

    return numero_para_dias[numero_dia_evento]
