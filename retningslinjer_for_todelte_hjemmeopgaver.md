# Retningslinjer for todelte hjemmeopgaver (Afleveringsformat)

Dette dokument er en **overbygning** til `continuerules.md` og gælder, når der udvikles større, todelte hjemmeopgaver med tidsregistrering, metodebeskrivelse og PDF-afleveringsrapport.

* **Grundprincip:** Alt i `continuerules.md` (sprog, tone, MathJax, matematisk notation jf. `Formelsamling-STXB-2024.pdf`, placering af `<script>` til sidst i `<body>` samt brug af `.card` og `.formula-box`) gælder uændret, **medmindre det eksplicit overstyres nedenfor**.

---

## 1. Overstyringer i forhold til `continuerules.md`

1. **Ekstra stylesheet i `<head>`:**
   Ud over `../style.css` skal filen **altid** linke til `../style_aflevering.css` (som ligeledes ligger i overmappen). Der må ikke skrives inline `<style>`-blokke i HTML-dokumentet.
2. **Ingen fuld løsning (`.sol-box` / `.btn-sol`) i Del 2:**
   Hvor `continuerules.md` har både hint- og løsningsknap på alle opgaver, gælder dette **kun for Del 1 (øvedelen)**. I **Del 2 (afleveringsdelen)** må der **ikke** være en løsningsknap eller `.sol-box` – kun `Hint 1` og `Hint 2`, som logges i rapporten.
3. **Interaktivitetsfunktioner i Del 2:**
   I Del 2 erstattes standardfunktionen `checkAnswer()` med afleveringsspecifikke funktioner (`checkPart2Single`, `checkPart2Tangent` og `useHint`), som tæller antal forsøg og brugte hints til PDF-rapporten.

---

## 2. HTML Header Struktur (Overstyring)
Udskift standard-headeren fra `continuerules.md` med denne, hvor `xx` erstattes af opgavens titel:

```html
<!DOCTYPE html>
<html lang="da">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hjemmeopgave – xx</title>
    <!-- Link til eksterne stylesheets i overmappen -->
    <link rel="stylesheet" href="../style.css">
    <link rel="stylesheet" href="../style_aflevering.css">
    <!-- MathJax til matematikvisning -->
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
```

---

## 3. Sidens overordnede opbygning

1. **Top-kort (`.formula-box`):**
   - Følger strukturen i `continuerules.md` med relevant formelsamling og 2–3 udfoldelige eksempler (`.example-block`), herunder et eksempel på, hvordan en god metodebeskrivelse formuleres, samt et eksempel med Maple-kommandoer.
2. **Del 1: Opvarmning og færdighedstræning (`.part-banner` + `.card`):**
   - Indledes med en `.part-banner`-boks, der forklarer, at uret ikke kører her, og at både hints og fulde løsninger er tilgængelige.
   - Opgaverne følger standardmønstret fra `continuerules.md` (med både `.btn-hint` og `.btn-sol`).
3. **Del 2: Afleveringsopgaver med tidsregistrering:**
   - Indledes med en `.part-banner`-boks, der forklarer formålet og fremhæver, at output afleveres som PDF.
   - Opgaverne er skjult bag `#part2-lock-screen` (`.locked-overlay`), indtil eleven trykker på `startPart2()`.
   - Øverst i `#part2-content` placeres `.timer-bar` (aktiv arbejdstid + nulstil-knap `resetAllData()`).
   - **Fordeling af opgavetyper i Del 2:**
     - Flest opgaver på grundlæggende/middel niveau (uden hjælpemidler).
     - Enkelte lette opgaver med udvidede regler (fx produkt- og kædereglen).
     - Mindst én afsluttende opgave med Maple (med hjælpemidler).
4. **Afleveringsboks (`.report-generator-box`) & Print-container (`#print-report`):**
   - Nederst i `#part2-content` placeres `.report-generator-box` med navnefelt (`#student-name`) og knappen `generatePDFReport()`.
   - Helt nederst i `<body>` (før `<script>`) placeres `<div id="print-report"></div>`, som er skjult på skærmen, men overtager hele udskriften via `@media print` i `style_aflevering.css`.

---

## 4. HTML Struktur for en opgave i Del 2 (Card)
Hver opgave i Del 2 skal have et unikt `taskId` (`t1`, `t2`, `t3`, ...) og følge dette mønster:

```html
<div class="card" id="card-t1">
    <span class="task-title">Opgave 2.1: Titel (uden hjælpemidler / med hjælpemidler)</span>
    <p>Opgavebeskrivelse med \( \text{matematik} \).</p>

    <label for="method-t1"><strong>Metodebeskrivelse og vigtigste mellemregninger:</strong></label>
    <textarea id="method-t1" class="method-textarea" oninput="saveText('t1')" placeholder="Forklar din fremgangsmåde og vigtigste mellemregninger..."></textarea>

    <p><strong>Tjek dit resultat:</strong></p>
    <div class="input-section">
        <label for="ans-t1">\( x_0 = \)</label>
        <input type="number" id="ans-t1" step="0.01" placeholder="Svar...">
    </div>
    <div class="btn-group">
        <button class="btn-check" onclick="checkPart2Single('t1', KORREKT_VÆRDI, TOLERANCE)">Tjek resultat</button>
        <button class="btn-hint" onclick="useHint('t1', 1)">Hint 1</button>
        <button class="btn-hint" onclick="useHint('t1', 2)">Hint 2</button>
    </div>
    <div id="feedback-t1" class="feedback"></div>
    <div id="hint-t1-1" class="hint-box" style="display:none;"><strong>Hint 1:</strong> Første hjælpende skridt...</div>
    <div id="hint-t1-2" class="hint-box" style="display:none;"><strong>Hint 2:</strong> Næste hjælpende skridt...</div>

    <div class="rating-box">
        <strong>Vurdering af opgave 2.1:</strong> Hvor svær synes du, opgaven var?
        <div class="rating-options">
            <label><input type="radio" name="rate-t1" value="1 (Meget let)" onchange="saveRating('t1', this.value)"> 1 (Meget let)</label>
            <label><input type="radio" name="rate-t1" value="2 (Let)" onchange="saveRating('t1', this.value)"> 2 (Let)</label>
            <label><input type="radio" name="rate-t1" value="3 (Tilpas)" onchange="saveRating('t1', this.value)"> 3 (Tilpas)</label>
            <label><input type="radio" name="rate-t1" value="4 (Svær)" onchange="saveRating('t1', this.value)"> 4 (Svær)</label>
            <label><input type="radio" name="rate-t1" value="5 (Meget svær)" onchange="saveRating('t1', this.value)"> 5 (Meget svær)</label>
        </div>
        <input type="text" id="comment-t1" class="comment-input" oninput="saveComment('t1')" placeholder="Valgfri kommentar til opgaven...">
    </div>
</div>
```

---

## 5. CAS-syntaks (Maple) og JavaScript-konfiguration
- **Maple-konventioner:**
  - I Maple-eksempler og -hints bruges decimaltal i funktionskald (fx `f'(2.0) * (x - 2.0) + f(2.0);`), så Maple returnerer decimaltal frem for eksakte udtryk.
  - Eksponentialfunktionen \( \mathrm{e}^x \) skrives altid som `exp(x)` i Maple-hints.
- **Konfiguration i `<script>` (nederst i `<body>`):**
  - **`STORAGE_KEY`:** Skal altid ændres til et unikt navn for den konkrete hjemmeopgave (fx `'math_hw_integral_v1'`), så elevens gemte svar og tid i `localStorage` ikke kolliderer med andre opgaver.
  - **`PART2_TASKS`:** Skal opdateres, så arrayet matcher alle opgaver i Del 2 (`id` og `title`), da det styrer både automatisk lagring og tabellen i PDF-rapporten.
  - **Tidtagning:** Tæller kun aktiv tid, mens fanen er synlig (`document.visibilityState === 'visible'`) og der har været brugeraktivitet inden for de seneste 3 minutter (`INACTIVITY_LIMIT_MS = 3 * 60 * 1000`).
  - **PDF-rapport (`generatePDFReport()`):** Skal generere en rapport i `#print-report` med elevens navn, dato, aktiv tid på Del 2, antal rigtige opgaver, oversigtstabel (resultat, forsøg, brugte hints, elevens vurdering), alle metodebeskrivelser og kommentarer samt et kontrol-ID (`MAT-XXXXXX`).