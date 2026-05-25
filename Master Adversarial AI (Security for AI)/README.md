\# Adversarial AI Testing \& LLM Guardrail Engineering Lab



\## Executive Summary

As organizations rapidly adopt AI, securing Large Language Models (LLMs) against adversarial attacks is critical. This project evaluates LLM application vulnerabilities based on the \*\*OWASP Top 10 for LLM Applications\*\*. Using a fully localized and air-gapped environment, I simulated direct prompt injection and sensitive information disclosure attacks against an enterprise application mockup, followed by engineering defensive input/output filters to mitigate the risks.



\## Core Competencies Demonstrated

\* \*\*AI Security Auditing \& Red Teaming\*\*

\* \*\*Prompt Injection Mitigations (LLM01)\*\*

\* \*\*Data Loss Prevention / Information Disclosure Defenses (LLM02)\*\*

\* \*\*Python Defensive Programming\*\*



\## Environment \& Architecture

\* \*\*LLM Engine:\*\* Ollama (Running Phi-3 locally)

\* \*\*Language:\*\* Python 3.x

\* \*\*Framework:\*\* OWASP Top 10 for LLM Applications

\* \*\*Workflow:\*\*

&#x20; 1. \*\*Adversarial Phase (`app.py`):\*\* Deployed a simulated corporate support chatbot containing sensitive internal variables. Conducted jailbreak scripts to extract restricted data.

&#x20; 2. \*\*Defensive Remediation (`secure\_app.py`):\*\* Developed an application-layer security proxy featuring keyword-based semantic filtering (input validation) and string-based data redaction (output filtering).



\## Attack Evidence (Before Patching)

\*The system was successfully bypassed using a Roleplay Escape prompt, forcing the LLM to reveal the legacy database key.\*

!\[Successful Attack](successful\_attack.png)



\## Defensive Verification (After Patching)

\*After implementing input sanitization and DLP output filters, the exact same attack vector was successfully intercepted and blocked.\*

!\[Blocked Attack](blocked\_attack.png)

