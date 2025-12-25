# Terraform Infrastructure (IaC)

## Zweck

Dieses Verzeichnis enthält ein **Terraform-Skeleton**, das die grundlegende Cloud-Infrastruktur
für die Flask-Anwendung **konzeptionell** beschreibt.

Der Fokus liegt auf Architekturverständnis und Infrastructure-as-Code (IaC),
nicht auf einem produktiven Deployment.

---

## Architektur (Konzeptuell)

Die Infrastruktur besteht aus drei Kernbausteinen:

* **Network**: Eine isolierte Virtual Private Cloud (VPC)
* **Security**: Eine Security Group zur Zugriffskontrolle
* **Compute**: Eine virtuelle Maschine als Laufzeitumgebung für die API

```
Client
  |
  v
[ Security Group ]
        |
        v
     [ EC2 ]
        |
        v
     [ VPC ]
```

---

## Trennung von Anwendung und Infrastruktur

Die Infrastruktur ist **vollständig vom Anwendungscode getrennt**:

* Der Flask-Code enthält keine Cloud-spezifischen Abhängigkeiten
* Keine Provider-spezifische Logik im Backend
* Infrastruktur wird ausschließlich über Terraform beschrieben

Diese Trennung ermöglicht:

* Austausch der Cloud-Plattform (AWS / Azure)
* Wiederverwendbarkeit der Anwendung
* saubere Verantwortlichkeiten

---

## Bewusste Vereinfachungen

Dieses Setup ist absichtlich **minimal gehalten**:

* Platzhalter (z. B. AMI-ID) statt echter Ressourcen
* Keine Credentials im Repository
* Kein `terraform apply`

Ziel ist es, das **Denken in Cloud-Architekturen** zu zeigen,
nicht reale Kosten zu verursachen.

---

## Lernziele

* Verständnis von Infrastructure as Code
* Grundkonzepte von Compute, Network und Security
* Cloud-Readiness einer Backend-Anwendung

Dieses Terraform-Skeleton dient als Basis für eine spätere
produktive Erweiterung.
