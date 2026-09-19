# Matematikopgaver - Regler for udvikling

## Generelle principper
- **Sprog:** Alt brugerfladetekst, opgavebeskrivelser, hints og feedback skal være på dansk.
- **Tone:** Hjælpsom, pædagogisk og opmuntrende.
- **Tilgængelighed:** Brug semantisk HTML og sørg for, at inputfelter har labels eller placeholder-tekst.
- **Hints:** Hints skal hjælpe frem mod svaret man skal ikke give selve svaret.

## Teknisk Standard
- **Matematik:** Brug MathJax til alle formler. 
    - Inline formler: `\( E = mc^2 \)`
    - Blok formler: `$$ \frac{-b \pm \sqrt{D}}{2a} $$`
- **Interaktivitet:** 
    - Brug `checkAnswer(id, correctVal)` til simple numeriske svar.
    - Brug `toggleBox(id)` til at vise/skjule hints og løsninger.
    - Feedback skal vises i et element med klassen `.feedback`.
- **Matematisk notation**
    - Den matematiske notation skal være den samme som `Formelsamling-STXB-2024.pdf`.      

## HTML Structure
- Top card med formlen/definitionen. I bunden af det et eller to eksempler som vises ved tryk på knapper.
- Regneopgaver, ikke "regneopgave" som overskrift
- Forståelsesopgaver, skal være tekst hvor eleverne skal vælge det rigtige udsagn.  Ikke "Forståelsesopgave" som overskrift
- En sidste mere krævende opgave til de hurtige, ikke "krævende opgave" som overskrift 
- js <script></script> skal udover det som har med style.css at gøre placeres til sidst i dokumentet.

## HTML Struktur for Teori og Eksempler (Formula Box)
Når en matematisk sætning eller teori skal præsenteres, bruges `.formula-box`. Den kan indeholde eksempler eller beviser, der kan foldes ud.

```html
<div class="formula-box">
    <h3>Sætningens Titel</h3>
    <p>Beskrivelse af sætningen med \( \text{matematik} \).</p>
    <div class="formula-group">
        <div><strong>Del 1:</strong> Forklaring...</div>
        <div><strong>Del 2:</strong> Forklaring...</div>
    </div>

    <div class="btn-group">
        <button class="btn-example" onclick="toggleBox('example-1')">Vis/Skjul Eksempel</button>
    </div>

    <div id="example-1" class="example-block">
        <h4>Eksempel på brug</h4>
        <p>Gennemgang af et eksempel...</p>
    </div>
</div>
```

## HTML header struktur
- den øverste del af html dokumentet skal indeholde, med xx udskiftet med titlen
```
<!DOCTYPE html>
<html lang="da">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> xx </title>
    <!-- Link til ekstern style.css jf. retningslinjerne -->
    <link rel="stylesheet" href="../style.css">
    <!-- MathJax til matematikvisning -->
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
```

## HTML Struktur for en opgave (Card)
Hver opgave skal følge dette mønster:
```html
<div class="card">
    <span class="task-title">Opgave X: Titel</span>
    <p>Opgavebeskrivelse med \( \text{matematik} \).</p>
    <div class="input-section">
        <input type="number" id="qX" step="0.01" placeholder="Svar...">
    </div>
    <div class="btn-group">
        <button class="btn-check" onclick="checkAnswer('qX', KORREKT_VÆRDI)">Tjek svar</button>
        <button class="btn-hint" onclick="toggleBox('hint-qX')">Hint</button>
        <button class="btn-sol" onclick="toggleBox('sol-qX')">Løsning</button>
    </div>
    <div id="feedback-qX" class="feedback"></div>
    <div id="hint-qX" class="hint-box"><strong>Hint:</strong> Hjælpende tekst her.</div>
    <div id="sol-qX" class="sol-box"><strong>Løsning:</strong> Gennemgang af beregningen.</div>
</div>
```

## CSS Retningslinjer
- Brug de eksisterende klasser i `style.css`:
    - `.card`: Standard opgavebeholder.
    - `.formula-box`: Til fremhævede formler i toppen af siden.
    - `.btn-check`, `.btn-hint`, `.btn-sol`: Knap-styling.
    - `.correct` / `.incorrect`: Farvning af feedback-tekst.
- `style.css` ligger en en overmappe.

## Workflow
- Nye emner bør have deres egen mappe, hvis de indeholder flere filer eller billeder.
- Opdater `README.md` med links til nye emner/sider.
