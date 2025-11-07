#include <stdio.h>

int main(){
    int n;
    int primeiro = 0, segundo = 1, proximo;

    printf("Digite o numero de termos da sequencia de Fibonacci que voce deseja calcular: ");
    scanf("%d", &n);

    printf("Sequencia de Fibonacci ate o termo %d:\n", n);

    for (int i = 0; i < n; i++)
    {
        if(i<= 1){
            proximo = i;
        } else {
            proximo = primeiro + segundo;
            primeiro = segundo;
            segundo = proximo;
        }
        printf("%d", proximo);
    }

    return 0;
}