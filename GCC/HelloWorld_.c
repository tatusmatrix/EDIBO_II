// http://cplusplus.com/ -> printf
#include<stdio.h>

int main()
 {
 //Hello World!//kļūda
 //"Hello World!"//kļūda
 //"Hello World!";//kļūdas nav, bet ir klusums
 //printf("Hello World!");
 printf("Hello World!\n");
 //lai printf strādātu ir jāpieslēdz stdio.h bibliotēka ar #include direktīvu
 return 0;
 }

/*
cmd:>./a.out
Hell World!cmd:>
           ^
           |
           |
šajā vietā prasās vēl viena darbība - kursora parcelšanas jaunas rindas sākumā
to var panākt ar speciāliem simboliem - darbības simboliem:
\n \t \r \b \v \a
*/
