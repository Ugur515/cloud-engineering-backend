# Flask Backend – Cloud-Ready Beispielprojekt

## Überblick

Dieses Repository enthält eine **Flask-basierte Backend-Anwendung**, die schrittweise von einer einfachen API zu einer **cloud‑fähigen, professionell strukturierten Backend‑Architektur** weiterentwickelt wurde.

Der Fokus liegt nicht auf Feature‑Menge, sondern auf:

* sauberer Architektur
* Wartbarkeit
* Cloud‑Readiness
* nachvollziehbarer Lernkurve

Das Projekt ist bewusst **junior‑gerecht**, aber **beruflich realistisch** aufgebaut.

---

## Architektur – Gesamtübersicht

```
Client (Browser / Postman)
        |
        v
   Flask API (Routes)
        |
        v
   Service Layer (Business-Logik)
        |
        v
   Repository / DB-Zugriff
        |
        v
      SQLite (lokal)

-------------------------------

   Infrastructure as Code
        |
        v
   Terraform (Compute / Network / Security)
```

Die Anwendung ist vollständig **von der Infrastruktur entkoppelt**.

---

## Projektstruktur (vereinfacht)

```
app/
  routes/        # HTTP-Endpunkte
  services/      # Business-Logik
  repositories/  # Datenzugriff
  models/        # Datenmodelle
  main.py        # App-Startpunkt

infra/
  terraform/     # Infrastructure as Code (IaC)

README.md
```

---

## Technologiestack

* **Python / Flask** – REST API
* **SQLite** – lokale Datenhaltung (austauschbar)
* **Terraform** – Infrastructure as Code (konzeptionell)
* **Logging** – strukturierte Logs statt print

---

## Cloud-Readiness

Das Projekt ist so aufgebaut, dass:

* keine Cloud‑spezifische Logik im Anwendungscode enthalten ist
* Konfiguration über Variablen erfolgt
* Datenhaltung austauschbar ist (z. B. RDS, Cloud SQL)
* Infrastruktur separat und versioniert beschrieben wird

Details zur Infrastruktur befinden sich in:

➡️ `infra/terraform/README.md`

---

## Bewusste Vereinfachungen

* Keine produktive Cloud‑Provisionierung
* Platzhalter für Infrastruktur‑Ressourcen
* Fokus auf Architektur statt Betrieb

Diese Entscheidungen sind **absichtlich**, um das Grundverständnis sauber zu zeigen.

---

## Was ich in diesem Projekt gelernt habe

* Aufbau einer mehrschichtigen Backend‑Architektur
* Trennung von HTTP‑Schicht, Logik und Datenzugriff
* Saubere Fehlerbehandlung und Logging
* Vorbereitung einer Anwendung auf Cloud‑Umgebungen
* Modellierung von Infrastruktur mit Terraform (IaC‑Grundlagen)

---

## Zielgruppe

Dieses Projekt richtet sich an Bewerbungen für:

* Cloud Engineer Trainee
* Junior Cloud Engineer
* Junior Backend Engineer
* Junior Platform / Infrastructure Engineer

---

## Hinweis

Dieses Repository dient als **Lern‑ und Demonstrationsprojekt**.
Es erhebt keinen Anspruch auf produktiven Einsatz, sondern auf saubere technische Grundlagen.
