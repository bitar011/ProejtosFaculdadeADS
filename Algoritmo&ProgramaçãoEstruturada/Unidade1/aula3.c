#include <stdio.h>

int main() {
    
    //Declaração das Variáveis
    
    //Variáveis para guardar os dados de entrada
    int tv_2020, note_2020, smart_2020;
    int tv_2021, note_2021, smart_2021;
    int tv_2022, note_2022, smart_2022;
    
    //Variáveis para os cálculos
    int total_2020, total_2021, total_2022;
    float media_2020, media_2021, media_2022;

    //Coleta de Dados
    printf("Insira os dados de 2020\n");
    printf("Vendas de TV: ");
    scanf("%d", &tv_2020);
    printf("Vendas de Notebook: ");
    scanf("%d", &note_2020);
    printf("Vendas de Smartphone: ");
    scanf("%d", &smart_2020);

    printf("\nInsira os dados de 2021\n");
    printf("Vendas de TV: ");
    scanf("%d", &tv_2021);
    printf("Vendas de Notebook: ");
    scanf("%d", &note_2021);
    printf("Vendas de Smartphone: ");
    scanf("%d", &smart_2021);

    printf("\nInsira os dados de 2022\n");
    printf("Vendas de TV: ");
    scanf("%d", &tv_2022);
    printf("Vendas de Notebook: ");
    scanf("%d", &note_2022);
    printf("Vendas de Smartphone: ");
    scanf("%d", &smart_2022);


    //Cálculos

    //Calcula os totais de cada ano
    total_2020 = tv_2020 + note_2020 + smart_2020;
    total_2021 = tv_2021 + note_2021 + smart_2021;
    total_2022 = tv_2022 + note_2022 + smart_2022;

    //Calcula as médias (dividindo por 3.0 para garantir resultado float)
    media_2020 = (float)total_2020 / 3.0;
    media_2021 = (float)total_2021 / 3.0;
    media_2022 = (float)total_2022 / 3.0;


    //Apresentação dos Resultados
    
    printf("\n\nAnalise de Vendas Anuais (2020-2022)\n\n");

    printf("Resultados para 2020:\n");
    printf("Total de produtos vendidos: %d\n", total_2020);
    printf("Media de vendas por tipo de produto: %.2f\n\n", media_2020);

    printf("Resultados para 2021:\n");
    printf("Total de produtos vendidos: %d\n", total_2021);
    printf("Media de vendas por tipo de produto: %.2f\n\n", media_2021);

    printf("Resultados para 2022:\n");
    printf("Total de produtos vendidos: %d\n", total_2022);
    printf("Media de vendas por tipo de produto: %.2f\n\n", media_2022);

    return 0;
}