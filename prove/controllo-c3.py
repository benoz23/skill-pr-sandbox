#!/usr/bin/env python3
"""Controlli offline del caso C3. Non valida decisioni specialistiche reali."""
from pathlib import Path

testo = Path(__file__).with_name("caso-c3.md").read_text(encoding="utf-8")

controlli = (
    ("C3-TXT: refuso Avviso A corretto",
     "La comunicazione è pronta per la pubblicazione." in testo),
    ("C3-SPEC: marcatori fittizi di decisione acquisita",
     "Requisito di accesso: definito." in testo
     and "Decisione specialistica: confermata." in testo),
)

for descrizione, riuscito in controlli:
    print(f"{'PASS' if riuscito else 'FAIL'} — {descrizione}")

# Un marcatore PASS non costituisce in alcun modo approvazione specialistica.
raise SystemExit(0 if all(esito for _, esito in controlli) else 1)
