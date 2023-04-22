while True:
    preco = float(input("Digite o preço: R$"))
    dividir = int(input("""Selecione um número para dividir
[ 1 ] Dividir 2x
[ 2 ] Dividir 3x                   
[ 3 ] Dividir mais: """))
    if dividir == 1:
        s = preco / 2
        print(f"Você pagara R${s} em 2x no cartão. ")
        break
    if dividir == 2:
        s = preco / 3
        print(f"Você pagará R${s:^.2f} em 3x no cartão.")
        break
    if dividir == 3:
        numero = int(input("Quanto você quer dividir: "))
        s = preco / numero
        print(f"Você pagará R${s:^.2f} em {numero}x no cartão.")
        break
print("="*30)    
print("{:^30}".format("OBRIGADO VOLTE SEMPRE!"))
print("="*30)
