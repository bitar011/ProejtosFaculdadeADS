#include <stdio.h>

#define taxaDeImposto 0.1
#define descontoPadrão 0.05

int main()
{
    float valor, valorDesconto, valorImposto, valor_final;
    printf("Digite o valor de venda do produto: ");
    scanf("%f", &valor);

    valorImposto = valor * taxaDeImposto;
    valorDesconto = valor * descontoPadrão;
    valor_final = valor + valorImposto - valorDesconto;

    printf("O valor final e: R$%2.f", valor_final);
    return 0;
}
