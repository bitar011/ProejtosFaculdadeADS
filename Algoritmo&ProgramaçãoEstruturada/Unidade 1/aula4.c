#include<stdio.h>

int main(){

    //Definindo variáveis utilizadas
    float valor_bruto=0;
    float valor_liquido=0;
    float desconto=0;
    int qtd_pessoas=0;

    //Pede ao usuário o valor totda da conta
    printf("\n Digite o valor total da conta: ");
    scanf("%f",&valor_bruto);

    //Pede a quantidade de pessoas
    printf("\n Digite a quantidade de pessoas: ");
    scanf("%d",&qtd_pessoas);

    //Pede o desconto que será aplicado
    printf("\n Digite o desconto (em porcentagem): ");
    scanf("%f",&desconto);

    //Calcula valor final, aplicando desconto;
    valor_liquido = valor_bruto - (valor_bruto * desconto/100);

    //Exibe valores, final e a ser pago por pessoa
    printf("\n Valor da conta com desconto = %f",valor_liquido);
    printf("\n Valor a ser pago por pessoa = ");

    printf("\%f", valor_liquido/qtd_pessoas);

}