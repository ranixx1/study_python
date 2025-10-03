def dia(dia_int, mes_int, ano_int):
    meses_extenso = {
        1: "janeiro",
        2: "fevereiro",
        3: "marco",
        4: "abril",
        5: "maio",
        6: "junho",
        7: "julho",
        8: "agosto",
        9: "setembro",
        10: "outubro",
        11: "novembro",
        12: "dezembro"
    }

    dias_no_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if not (1 <= mes_int <= 12):
        return "Data Invalida"

    if not (1 <= dia_int <= dias_no_mes[mes_int]):
        return "Data Invalida"

    nome_do_mes = meses_extenso[mes_int]
    dia_formatado = f"{dia_int:02d}"

    return f"{dia_formatado} de {nome_do_mes} de {ano_int}"