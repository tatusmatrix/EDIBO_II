// Kods dažādu datu tipu pētīšanai
// Informācijas vienības, ar kurām operē cilvēks - simboli un skaitļi
// simboli: burti, cipari, punktuācijas zīmes utt. - ASCII tabula - simbols VS binārs kods

// skaitļi: veseli skaitļi, reālie skaitļi, kompleksie skaitļi (divas daļas - Re un Im)

// Informācijas vienība, ar kuru operē dators - bits (0/1)
// Informācijas vienība ar adresi (datorā) - baits
// 1 byte == 8 bits
// ASCII table - one symbol == 1 byte
// unique binary combinations inside 1 byte - 256
// 1 bits: 0, 1 - 2 kombinācijas
// 2 biti: 00, 01, 10, 11 - 4 kombinācijas
// 3 biti: 000, 001, 010, 011, 100, 101, 110, 111 - 8 kombinācijas
// x biti: ... - (stāvokļu skaits)^biti - (2)^8 = 256
// ASCII tabulā - 256 unikāli simboli (ASCII tabula 1. daļa - 128 simboli)

#include<stdio.h>
#define A 11

void main()
 {
 char a = 10; // definēšana
 // 1. darbība - RAM atmiņā tiek atvelēta vieta viena char datu tipa mainīgā glabāšanai
 // šī vieta vieta ir viennozīmīgi saķēdēta ar identifikatoru "a" (bet, vietai ir arī adrese)
 // saskaņā ar char datu tipu, vietas izmērs - 1 baits
 // Kā šajā izskatījās tas atmiņas apgabals: 0000 0101 vai 1111 1110 vai 0000 1010
 // char a; // deklarēšana
 // 2. darbība - vērtības piešķiršana
 // a = 10; // vērtības piešķiršana
 // a -> 0000 1010
 printf("Mainīgā a vērtība (laika momentā t1) ir: %d\n",a);
 a = 125;
 printf("Mainīgā a vērtība (laika momentā t2) ir: %d\n",a);
 printf("Konstantes A vērtība (laika momentā t3) ir: %d\n",A);
 // A = 126; //konstanti mainīt nevar
 // printf("Konstantes A vērtība (laika momentā t4) ir: %d\n",A);
 char mans_mainiigais = 45;
 //centīsimies izmantot mnemoniskus nosaukumus - nosaukums atspoguļo maināgā jēgu vai nolūku
 a = 0x10;// ||||||||||   ||||||||||||||||
 printf("Mainīgā a vērtība (laika momentā t4) ir: %d\n",a);// prognoze - 16 - OK
 printf("Mainīgā a vērtība (laika momentā t5) ir: 0x%x\n",a);// prognoze - 10 - OK
 printf("Mainīgā a vērtība (laika momentā t6) ir: %o (oct)\n",a);// prognoze - 20 - OK
// printf("Mainīgā a vērtība (laika momentā t7) ir: %b (bin)\n",a);// prognoze - 20 - OK

 a = 65;
 printf("Mainīgā a vērtība ir: %d\n",a);
 printf("Mainīgā a vērtība ir: 0x%x\n",a);
 printf("Mainīgā a vērtība ir: %o (oct)\n",a);
 printf("Mainīgā a vērtība kā simbols: %c\n",a);

 a = 'k';
 printf("Mainīgā a vērtība ir: %d\n",a);
 printf("Mainīgā a vērtība ir: 0x%x\n",a);
 printf("Mainīgā a vērtība ir: %o (oct)\n",a);
 printf("Mainīgā a vērtība kā simbols: %c\n",a);

// http://cplusplus.com/reference/cstdio/printf/?kw=printf

 a = 125;
 printf("Mainīgā a vērtība ir: %d\n",a);
 a = 126;
 printf("Mainīgā a vērtība ir: %d\n",a);
 a = 127;
 printf("Mainīgā a vērtība ir: %d\n",a);
// 1 byte -> 256 numbers
// => without sign 0 ... 255
// => with sign -128 ... 0 ... 127

 a = 128;
 printf("Mainīgā a vērtība ir: %d\n",a);

 a = 258; // 258 = 256 + 2 -> 0000 0001 | 0000 0010 |
 printf("Mainīgā a vērtība ir: %d\n",a);

 unsigned char b = 128;
 printf("Mainīgā b vērtība ir: %d\n",b);

 // int
 int c;
 printf("int datu tipa izmērs baitos: %ld\n",sizeof(c)); 
 // šoreiz int atbilst 4 baiti (32 biti)
 // => without sign 0 ... (2^32-1)
 // => with sign -(2^31) ... 0 ... (2^31-1)

 //----------------------------------------------------------
 float d = 6.5; //double
 printf("float datu tipa skaitļa attēlošana: %f\n",d); 
 printf("float datu tipa skaitļa attēlošana: %.2f\n",d); 
 printf("float datu tipa skaitļa attēlošana: %.f\n",d); 
 }
