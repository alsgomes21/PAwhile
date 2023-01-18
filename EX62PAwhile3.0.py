print('10 TERMOS DE UMA P.A')
print('='*20)

primeiro= int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
contagem = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while contagem <= total:
        print('{} - '.format(termo), end=' ')
        termo += razao
        contagem += 1
    print('Pausa')
    mais = int(input('Quantos termos a mais você quer mostrar?'))

print('Programa finalizado com total de {} termos'.format(total))