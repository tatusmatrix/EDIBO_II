#include<stdio.h>

void main()
 {
 char a;
 printf("Cienījamais, lietotāj, lūdzu ievadi vienu burtu: ");
 scanf("%c",&a);
 printf("Cienījamais, lietotāj, tu esi ievadījis simbolu: %c\n",a);
 printf("Cienījamais, lietotāj, tu esi ievadījis simbolu, kura dec kods ir: %d\n",a);
 printf("Cienījamais, lietotāj, tu esi ievadījis simbolu, kura hex kods ir: 0x%x\n",a);
 printf("Cienījamais, lietotāj, tu esi ievadījis simbolu, kura oct kods ir: %o\n",a);
 printf("P.s. kā reāls skaitlis: %f\n",a);

 int b;
 printf("Cienījamais, lietotāj, lūdzu ievadi vienu burtu: ");
 scanf("%d",&b);
 printf("Cienījamais, lietotāj, tu esi ievadījis simbolu: %c\n",b);
 printf("Cienījamais, lietotāj, tu esi ievadījis simbolu, kura dec kods ir: %d\n",b);
 printf("Cienījamais, lietotāj, tu esi ievadījis simbolu, kura hex kods ir: 0x%x\n",b);
 printf("Cienījamais, lietotāj, tu esi ievadījis simbolu, kura oct kods ir: %o\n",b);
 printf("P.s. kā reāls skaitlis: %f\n",b);

 double c;
 printf("Cienījamais, lietotāj, lūdzu ievadi vienu burtu: ");
 scanf("%lf",&c);
 printf("Cienījamais, lietotāj, tu esi ievadījis simbolu: %c\n",c);
 printf("Cienījamais, lietotāj, tu esi ievadījis simbolu, kura dec kods ir: %d\n",c);
 printf("Cienījamais, lietotāj, tu esi ievadījis simbolu, kura hex kods ir: 0x%x\n",c);
 printf("Cienījamais, lietotāj, tu esi ievadījis simbolu, kura oct kods ir: %o\n",c);
 printf("P.s. kā reāls skaitlis: %f\n",c); 
}
