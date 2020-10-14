#Calculo de imposto

salario = int(input("Digite aqui quanto voce ganha:"))
imposto = 0
if salario < 3000:
  imposto = salario * 0.15
  print("Este e o valor do seu imposto:{}".format(imposto))
else:
  imposto = salario * 0.5
  print("Este e o valor do seu imposto:{}".format(imposto))
