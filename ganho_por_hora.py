ganho_por_hora = float(input("Quanto você ganha horas? "))
numero_de_horas_no_mes = float(input("Numero de horas trabalhadas no mes? "))
salario_bruto = ganho_por_hora * numero_de_horas_trabalhadas_no_mes
imposto_de_renda = salario_bruto * (11/100)
inss = salario_bruto * (8/100)
sindicato = salario_bruto * (5/100)
salario_liquido = salario_bruto - imposto_de_renda - inss - sindicato

print("Salario bruto: ",salario_bruto)
print("Inss: ",inss)
print("Sindicato: ", sindicato)
print("Salario liquido:", salario_liquido)