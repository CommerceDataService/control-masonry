---
permalink: /RA-5/
title: RA-5 - Vulnerability Scanning
---
## The organization GSA OCISO and Valiant Solutions&colon;
## a. Scans for vulnerabilities in the information system and hosted applications [Assignment&colon; organization-defined frequency and/or randomly in accordance with organization-defined process] and when new vulnerabilities potentially affecting the system/applications are identified and reported;  
* * *   
### AWS (VPC) Vulnerability Scanning  
* AlienVault USM for AWS runs monthly AWS friendly authenticated vulnerability scans within the 18F Virtual Private Cloud (VPC) infrastructure and does not require permission from AWS to conduct the vulnerability scan.  
* Nessus will be used conduct internal scanning of its VPC and private subnets within the 18F Virtual Private Cloud  
  
## b. Employs vulnerability scanning tools and techniques that facilitate interoperability among tools and automate parts of the vulnerability management process by using standards for&colon; (1) Enumerating platforms, software flaws, and improper configurations; (2) Formatting checklists and test procedures; and (3) Measuring vulnerability impact;  
* * *   
### AWS Vulnerability Scanning & interoperability  
* AlienVault USM for AWS runs AWS friendly authenticated vulnerability scans within the 18F Virtual Private Cloud (VPC) infrastructure and does not require permission from AWS to conduct the vulnerability scan. AlienVault USM identifies insecure configurations in 18Fs , identifies the current system inventory, provides  
  
### Operating System & Web Application (EC2) Vulnerabilit  y Scanning & interoperability  
* Nessus, and AlienVault USM for AWS utilize tools and techniques that promote interoperability such as Common Vulnerability Scoring System v2 (CVSS2), Common Platform Enumeration (CPE), and Common Vulnerability Enumeration (CVE). Tenable SecurityCenter is able to output reports in CyberScope format to meet NIST, DHS, and GSA reporting requirements.  
* OWASP Zap is used for web application scanning of hosted web sites and web based applications. It scans for the OWASP TOP 10 vulnerabilities and utilize tools and techniques that promote interoperability such as Common Vulnerability Scoring System v2 (CVSS2), Common Platform Enumeration (CPE), and Common Vulnerability Enumeration (CVE).  
  
## c. Analyzes vulnerability scan reports and results from security control assessments;  
* * *   
## d. Remediates legitimate vulnerabilities [Assignment&colon; organization-defined response times] in accordance with an organizational assessment of risk; and  
* * *   
## e. Shares information obtained from the vulnerability scanning process and security control assessments with [Assignment&colon; organization-defined personnel or roles] to help eliminate similar vulnerabilities in other information systems (i.e., systemic weaknesses or deficiencies).  
* * *   
### Operating System and Web Application (EC2) Vulnerabilit  y Reporting  
* Depending on the vulnerability identified the appropriate group will be tasked with resolution. If the vulnerability indicates a more systemic problem, then additional groups or points of contact are included to determine the best course of action for resolution of the systemic problem.  
* If indications of a breach are discovered the incident will be handled according to the GSA Security Incident Handling Guide: CIO IT Security 01-02 Revision 7 (August 18, 2009) requirements.  
  
