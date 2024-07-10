
numero = int(input("Digite um número: "))

if numero <= 1:
  print(f"{numero} não é primo.")
elif numero <= 3:
  print(f"{numero} é um número primo.")
else:
  nao_primo = False
  i = 5
  while i * i <= numero:
    if numero % i == 0 or numero % (i + 2) == 0:
      nao_primo = True
      break
    i += 6
  if nao_primo:
    print(f"{numero} não é um número primo.")
  else:
    print(f"{numero} é um número primo.")
