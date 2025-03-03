# OSINT Tool List  
This document lists the **open-source intelligence (OSINT) tools** used in the investigation of `lilyanavonel@gmail.com`.  

---

## **1. Data Breach & Credential Exposure**  
| Tool | Description | Link |
|------|------------|------|
| **Have I Been Pwned** | Checks if an email has been leaked in past data breaches | [https://haveibeenpwned.com/](https://haveibeenpwned.com/) |
| **IntelligenceX** | Searches dark web & paste sites for leaked credentials | [https://intelx.io/](https://intelx.io/) |

---

## **2. Email Reputation & Threat Analysis**  
| Tool | Description | Link |
|------|------------|------|
| **EmailRep.io** | Checks if an email is used for spam, fraud, or social media | [https://emailrep.io/](https://emailrep.io/) |
| **Hunter.io** | Finds company affiliations & email metadata | [https://hunter.io/](https://hunter.io/) |

---

## **3. Public Mentions & Search Engine OSINT**  
| Tool | Description | Link |
|------|------------|------|
| **Google Dorking** | Finds public mentions of the email in blogs, forums, PDFs | [https://www.google.com/advanced_search](https://www.google.com/advanced_search) |
| **IntelligenceX** | Searches for email mentions in government documents, files | [https://intelx.io/](https://intelx.io/) |

---

## **4. Website & Domain Investigation**  
| Tool | Description | Link |
|------|------------|------|
| **WHOIS Lookup** | Checks if the email is linked to any registered domains | [https://who.is/](https://who.is/) |
| **DNSDumpster** | Provides domain information and subdomain enumeration | [https://dnsdumpster.com/](https://dnsdumpster.com/) |


---

## **OSINT Automation Scripts**  
| Script | Description | File Location |
|--------|------------|--------------|
| **Email Reputation Checker** | Uses EmailRep API to analyze an email | `tools/email-reputation-checker.py` |
| **Google Dorking Automation** | Automates Google searches for public mentions | `tools/google-dorking-automation.py` |
| **WHOIS Lookup Script** | Checks if an email is linked to a domain | `tools/whois-lookup.sh` |


