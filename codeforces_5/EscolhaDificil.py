
Ca, Ba, Pa = map(int, input().split())  # Quantidade disponível
Cr, Br, Pr = map(int, input().split())  # Quantidade requisitada

# Cálculo de faltas
faltam_frango = max(0, Cr - Ca)
faltam_bife = max(0, Br - Ba)
faltam_massa = max(0, Pr - Pa)

total_faltando = faltam_frango + faltam_bife + faltam_massa

print(total_faltando)
