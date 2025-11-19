#include <stdio.h>

//Definição de constantes
#define taxaDeImposto 0.1
#define descontoPadrão 0.05

int main()
{
    //Definição de variáveis
    float valor, valorDesconto, valorImposto, valor_final;
    //Saída com comando do que deve ser feito e entrada do usuário
    printf("Digite o valor de venda do produto: ");
    scanf("%f", &valor);

    //Processamento que resultará no valor final
    valorImposto = valor * taxaDeImposto;
    valorDesconto = valor * descontoPadrão;
    valor_final = valor + valorImposto - valorDesconto;

    //Saída com valor final resultado do processamento
    printf("O valor final e: R$%2.f", valor_final);
    return 0;
}
