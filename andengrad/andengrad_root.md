---
title: "Udledning: Hvor kommer formlen for rødderne fra?"
author: "Matematik"
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

<div class="formula-box" style="background: #f8f9fa; border-left: 5px solid #3498db; padding: 15px; margin-bottom: 25px;">
  <h3 style="margin-top:0;">Målet for beviset</h3>
  <p>Løsningsformlen for 2.gradsligningen $ax^2 + bx + c = 0$ (hvor $a \neq 0$) er givet ved:</p>
  $$x = \frac{-b \pm \sqrt{d}}{2a} \quad \text{hvor} \quad d = b^2 - 4ac$$
  <p style="margin-bottom:0;"><strong>Diskriminantens betydning for antallet af rødder:</strong></p>
  <ul style="margin-top:5px; margin-bottom:0;">
    <li>$d > 0$: 2 løsninger</li>
    <li>$d = 0$: 1 løsning</li>
    <li>$d < 0$: ingen løsninger</li>
  </ul>
</div>

---

## Trin 1: Startligning til kvadratsætning

Vi ønsker at isolere $x$ i ligningen for et andengradspolynomium.

### Arbejdsspørgsmål til Trin 1:

1. **Skæringer og rødder:** 
   Forklar med dine egne ord, hvorfor man netop finder rødderne (skæringerne med $x$-aksen) der, hvor $f(x) = 0$, og hvorfor enhver andengradsligning kan omskrives til formen $ax^2 + bx + c = 0$.

2. **At gange igennem med $4a$:**
   Når vi ganger ligningen $ax^2 + bx + c = 0$ igennem med $4a$ på begge sider, får vi:
   $$4a^2 \cdot x^2 + 4ab \cdot x + 4ac = 0$$
   Forklar, hvorfor der stadig står $0$ på højre side efter multiplikationen.

3. **Flyt konstanten:**
   Ryk ledet $4ac$ over på højre side af lighedstegnet ved at trække det fra. Vis de mellemliggende trin så du ender med ligningen:
   $$4a^2 \cdot x^2 + 4ab \cdot x = -4ac$$

4. **Læg $b^2$ til:**
   Læg nu $b^2$ til på begge sider af lighedstegnet i din ligning fra spørgsmål 3, så du ender med udtrykket:
   $$4a^2 \cdot x^2 + 4ab \cdot x + b^2 = b^2 - 4ac$$

<details>
<summary style="background: #e8f8f0; border: 1px solid #2ecc71; padding: 10px; cursor: pointer; border-radius: 5px; font-weight: bold; color: #27ae60;">
🤖 Gemini Hint: Kopiér denne prompt til AI for hjælp til Trin 1
</summary>
<div style="background: #fdfefe; border: 1px solid #2ecc71; padding: 15px; border-radius: 5px; margin-top: 5px;">

Jeg arbejder med Trin 1 i udledningen af løsningsformlen for en 2.gradsligning. 
Du må IKKE give mig færdige svar. 
Stil mig i stedet 1-2 pædagogiske og guidende spørgsmål ad gangen, der hjælper mig med at forstå:
1. Hvorfor vi ganger igennem med 4a.
2. Hvordan leddet 4ac flyttes over på højre side.
3. Hvorfor det at lægge b^2 til på begge sider gør venstresiden klar til 1. kvadratsætning.

</div>
</details>

---

## Trin 2: Indføring af diskriminanten

Efter Trin 1 har vi opnået følgende ligning:

$$4a^2 \cdot x^2 + 4ab \cdot x + b^2 = b^2 - 4ac$$

### Arbejdsspørgsmål til Trin 2:

1. **Samling af parentesen:**
   Brug 1. kvadratsætning til at forklare, hvorfor venstresiden $4a^2 x^2 + 4ab x + b^2$ præcis kan omskrives til $(2ax + b)^2$.

2. **Diskriminanten $d$:**
   Kig på højresiden $b^2 - 4ac$. Hvorfor er dette udtryk en **konstant** (et tal, der ikke afhænger af variabelstørrelsen $x$)?
   *Vi vælger at kalde denne konstant for **diskriminanten** og giver den symbolet $d$.*

3. **Skriv den forenklede ligning:**
   Skriv den forenklede ligning op, hvor venstresiden er pakket sammen til en parentes i anden, og højresiden er erstattet af $d$:
   $$(2ax + b)^2 = d$$

<details>
<summary style="background: #e8f8f0; border: 1px solid #2ecc71; padding: 10px; cursor: pointer; border-radius: 5px; font-weight: bold; color: #27ae60;">
🤖 Gemini Hint: Kopiér denne prompt til AI for hjælp til Trin 2
</summary>
<div style="background: #fdfefe; border: 1px solid #2ecc71; padding: 15px; border-radius: 5px; margin-top: 5px;">

Jeg arbejder med Trin 2 i udledningen af løsningsformlen for en 2.gradsligning. 
Hjælp mig med at forstå omskrivningen fra:
4a^2 * x^2 + 4ab * x + b^2 = b^2 - 4ac 
til
(2ax + b)^2 = d

Du må IKKE give mig løsningen direkte. Stil mig guidende spørgsmål om, hvordan 1. kvadratsætning bruges her, og hvorfor vi kalder udtrykket (b^2 - 4ac) for diskriminanten d.

</div>
</details>

---

## Trin 3: Isolering af $x$ og den færdige formel

Vi står nu med den forenklede ligning:

$$(2ax + b)^2 = d$$

### Arbejdsspørgsmål til Trin 3:

1. **Fjern potensen:**
   Hvordan fjerner man "i anden" på venstresiden? 
   Forklar, hvorfor der skal tilføjes et $\pm$ (plus-minus) foran udtrykket på højresiden, når man tager kvadratroden:
   $$2ax + b = \pm\sqrt{d}$$

2. **Isolér $x$ i to skridt:**
   * **Skridt A:** Hvad får du, hvis du trækker $b$ fra på begge sider af lighedstegnet?
   * **Skridt B:** Hvad skal du til sidst dividere med på begge sider for helt at isolere $x$?

3. **Samling:**
   Opskriv den endelige løsningsformel for $x$:
   $$x = \frac{-b \pm \sqrt{d}}{2a}$$

<details>
<summary style="background: #e8f8f0; border: 1px solid #2ecc71; padding: 10px; cursor: pointer; border-radius: 5px; font-weight: bold; color: #27ae60;">
🤖 Gemini Hint: Kopiér denne prompt til AI for hjælp til Trin 3
</summary>
<div style="background: #fdfefe; border: 1px solid #2ecc71; padding: 15px; border-radius: 5px; margin-top: 5px;">

Jeg arbejder med Trin 3 i udledningen af løsningsformlen for en 2.gradsligning, hvor vi har ligningen (2ax + b)^2 = d.
Guide mig igennem de sidste algebraiske trin med isoleringen af x uden at give mig svarene direkte. Stil spørgsmål til, hvorfor vi bruger plus/minus ved kvadratroden, og hvordan b og 2a flyttes korrekt over.

</div>
</details>

---

# Tjek din forståelse

## Hvorfor kræver formlen, at diskriminanten $d \geq 0$?

Kig på det øjeblik i beviset, hvor vi tager kvadratroden:

$$2ax+b=\pm\sqrt{d}$$

Hvorfor giver det ingen mening at lede efter reelle rødder, hvis $d$ er et negativt tal (f.eks. $d = -4$)?

Sæt kryds ved det svar, du mener er rigtigt:

- [ ] **A:** Fordi hvis $d$ er negativ, vil hele brøken give et negativt resultat, og rødder må aldrig være negative tal.
- [ ] **B:** Fordi man ikke kan tage kvadratroden af et negativt tal inden for de reelle tal, da intet tal ganget med sig selv kan give et negativt resultat.
- [ ] **C:** Hvis $d$ er negativ, forsvinder koefficienten $b$ ud af ligningen, og så kan man ikke gøre beviset færdigt.

**Din forklaring med egne ord:**

\vspace{35mm}

---

**Opsamling:**

$$d = b^2 - 4ac \qquad \text{og} \qquad x = \frac{-b \pm \sqrt{d}}{2a}$$