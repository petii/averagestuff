# averagestuff
A simple python script to calculate the averages of the semester.

## Usage
Download the summary of the semester from Neptun, then convert the .xlsx file to .csv and add that file as a parameter to the script.
It should then print out your averages.

## Example
```
Input:
Tárgykód,"Tárgy címe, előadó neve",Kr.,Köv.,Óra heti (E/GY/L),Óra féléves (E/GY/L),Aláírás,Jegyek,Megjegyzés,Várólista,Teljesített,,,,,,,,,,,
IP-08JMIE,"Jogi-és menedzsment ismeretek EA. (BSc 08),  Balázs Krisztina Eszter dr.",2,Kollokvium (5),0/0/2,,,Jeles Balázs Krisztina Eszter dr. 2016.05.24. ,,,Igen,,,,,,,,,,,677377932
IP-08KGAE,"Közgazdasági alapismeretek EA. (BSc 08),  Lovics Gábor Tibor",3,Kollokvium (5),0/0/3,,,Jó Lovics Gábor Tibor 2016.05.20. ,,,Igen,,,,,,,,,,,677377896
IP-08cSCNYE,"Script nyelvek EA. (BSc,08,C),  Tejfel Máté",3,Kollokvium (5),0/0/2,,,Jeles Tejfel Máté 2016.06.17. ,,,Igen,,,,,,,,,,,678792876
IP-08aDM2E,"Diszkrét matematika 2. EA. (BSc,08,A),  Burcsi Péter",3,Kollokvium (5),0/0/3,,,Jó Burcsi Péter 2016.05.31. ,,,Igen,,,,,,,,,,,679062050
IP-08aPROGEG,"Programozás EA+GY. (BSc,08,A),  Veszprémi Anna, Gregorics Tibor Dr., Hudoba Péter",7,gyakorlati jegy (5),0/0/6,,,Jeles Veszprémi Anna 2016.06.20. ,,,Igen,,,,,,,,,,,679072657
IP-08aDM2G,"Diszkrét matematika 2. GY. (BSc,08,A),  Kőszegi Gábor, Burcsi Péter",3,gyakorlati jegy (5),0/3/0,,,Jeles Kőszegi Gábor 2016.05.31. ,,,Igen,,,,,,,,,,,684703558
IP-08aAN1G,"Analízis 1. GY. (BSc,08,A),  Németh Zsolt, Szili László",2,gyakorlati jegy (5),0/2/0,,,Jeles Németh Zsolt 2016.05.25. ,,,Igen,,,,,,,,,,,679071536
IP-08aFNYG,"Formális nyelvek és automaták GY (BSc,08,A),  Kolonits Gábor, Csuhaj Varjú Erzsébet",2,gyakorlati jegy (5),0/2/0,,,Jeles Kolonits Gábor 2016.05.19. ,,,Igen,,,,,,,,,,,679071062
IP-08aFNYE,"Formális nyelvek és automaták EA (BSc, 08,A),  Csuhaj Varjú Erzsébet",2,Kollokvium (5),0/0/2,,,Közepes Csuhaj Varjú Erzsébet 2016.05.25. ,,,Igen,,,,,,,,,,,679071424
IP-08aAN1E,"Analízis 1. EA. (BSc,08,A),  Szili László",3,Kollokvium (5),0/0/2,,,Jó Szili László 2016.06.06. ,,,Igen,,,,,,,,,,,679071719
IP-08aPNY1EG,"Programozási nyelvek I. C++ EA+GY. (BSc,08,A),  Parragi Zsolt, Pataki Norbert, Porkoláb Zoltán",5,gyakorlati jegy (5),0/0/4,,,Jó Pataki Norbert 2016.06.02. ,,,Igen,,,,,,,,,,,679072698
```
```
Output:
Kreditindex: 5.23333333333
```
