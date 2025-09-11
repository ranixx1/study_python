salario  = float(input())

if(salario <= 2000.00):
    print("Isento")
elif(salario > 2000.00 and salario <=3000.00):
    print(f"R$ {salario*0.08:.2f}")
elif(salario > 3000.00 and salario <=4500.00):
    print(f"R$ {salario*0.18:.2f}")
elif(salario > 4500.00):
    print(f"R$ {salario*0.18:.2f}")