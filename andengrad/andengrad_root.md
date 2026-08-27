---
title: "Eksperimentel matematik"
author: ""
date: ""
lang: da
papersize: a4
geometry: margin=18mm
fontsize: 12pt
header-includes:
  - |
    \usepackage{amsmath}
    \usepackage{amssymb}
    \usepackage{enumitem}
    \setlist[enumerate]{itemsep=0.5em}
---

# Udledning: Hvor kommer formlen for rødderne fra?

## Målet: At løse $a \cdot x^2 + b \cdot x + c = 0$

Når vi leder efter rødderne i et andengradspolynomium, leder vi efter de steder, hvor grafen skærer x-aksen. Det svarer til at løse ligningen, hvor $y=0$.

Udfordringen er, at $x$ optræder i både første og anden potens på samme tid, så vi kan ikke bare isolere det, som vi plejer. Vi er nødt til at lave et matematisk trick, der samler alle $x$'erne ét sted ved hjælp af 1. kvadratsætning.

## Trin 1: Tricket: Vi ganger med $4a$

Vi starter med vores grundligning:

$$
a \cdot x^2 + b \cdot x + c = 0
$$

For at gøre tallene nemmere at omdanne til en parentes senere, starter vi med at gange med $4a$ i alle led på begge sider af lighedstegnet:

$$
4a^2 \cdot x^2 + 4ab \cdot x + 4ac = 0
$$

Nu rykker vi det løse led $4ac$ over på højre side ved at trække det fra:

$$
4a^2 \cdot x^2 + 4ab \cdot x = -4ac
$$

**Overvej:** Hvorfor kan $4a^2 \cdot x^2$ også skrives som $(2ax)^2$?

## Trin 2: Læg $b^2$ til og dan kvadratet

Nu lægger vi $b^2$ til på begge sider af lighedstegnet. Det gør vi, fordi venstresiden derved kommer til at matche 1. kvadratsætning:

$$
4a^2 \cdot x^2 + 4ab \cdot x + b^2 = b^2 - 4ac
$$

Venstresiden kan nu omskrives og pakkes sammen til en enkelt parentes i anden:

$$
(2ax+b)^2 = b^2 - 4ac
$$

Her spotter vi noget velkendt! Højresiden $b^2-4ac$ kalder vi for **diskriminanten, $d$** (formel 65). Vi kan derfor skrive ligningen som:

$$
(2ax+b)^2=d
$$

**Overvej:** Vis ved hjælp af 1. kvadratsætning, hvordan udtrykket

$$
4a^2 \cdot x^2 + 4ab \cdot x + b^2
$$

bliver pakket sammen til $(2ax+b)^2$.

## Trin 3: Fjern "i anden" ved at tage kvadratroden

Vi står nu med den simplere ligning:

$$
(2ax+b)^2=d
$$

For at fjerne potensen i anden tager vi kvadratroden på begge sider. Da et tal i anden altid bliver positivt, skal vi huske, at der både kan gemme sig en positiv og en negativ løsning under kvadratroden ($\pm$):

$$
2ax+b=\pm\sqrt{d}
$$

Nu kan vi isolere $x$ i to skridt:

1. Træk $b$ fra på begge sider:

   $$
   2ax=-b\pm\sqrt{d}
   $$

2. Divider med $2a$ på begge sider:

   $$
   \boxed{x=\frac{-b\pm\sqrt{d}}{2a}}
   $$

Dette er den berømte løsningsformel for rødderne i et andengradspolynomium.

# Tjek din forståelse

## Hvorfor kræver formlen, at diskriminanten $d \geq 0$?

Kig på det øjeblik i beviset, hvor vi tager kvadratroden:

$$
2ax+b=\pm\sqrt{d}
$$

Hvorfor giver det ingen mening at lede efter rødder, hvis $d$ er et negativt tal, for eksempel $d=-4$?

Sæt kryds ved det svar, du mener er rigtigt.

- [ ] **A:** Fordi hvis $d$ er negativ, vil hele brøken give et negativt resultat, og rødder må aldrig være negative tal.

- [ ] **B:** Fordi man ikke kan tage kvadratroden af et negativt tal inden for de reelle tal. Intet tal ganget med sig selv kan give noget negativt.

- [ ] **C:** Hvis $d$ er negativ, forsvinder koefficienten $b$ ud af ligningen, og så kan man ikke gøre beviset færdigt.

**Din forklaring:**

\vspace{35mm}

---

**Husk:**

$$
 d=b^2-4ac
 \qquad\text{og}\qquad
 x=\frac{-b\pm\sqrt{d}}{2a}
$$
