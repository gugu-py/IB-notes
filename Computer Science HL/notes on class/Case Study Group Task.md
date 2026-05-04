## **Phase 1: Pre-Engagement Interactions**

> Which systems should be in scope (EHRs, IoT medical devices, communications)?

### raw

https://www.gethealthie.com/glossary/it-infrastructure

electronic health record (EHR). EHRs are used by healthcare providers to store and exchange patient health information. EHRs can be used by providers to track patient health information over time, to share information with other providers, and to exchange information with patients.

health information exchange (HIE). HIEs are used to exchange patient health information between different healthcare providers. HIEs can be used to share information between providers in different locations, to share information between providers in different care settings, or to exchange information between providers and patients.

clinical decision support systems, patient portals, and telehealth systems. Clinical decision support systems are used to help healthcare providers make better decisions about patient care. Patient portals are used to give patients access to their own health information. Telehealth systems are used to provide healthcare services to patients at a distance.

https://kodjin.com/blog/it-infrastructure-in-healthcare/

- **Content Management Systems (CMS):** enable the creation, management, and exchange of digital content.
- **Enterprise Resource Planning (ERP):** software that integrates and manages essential business processes.
- **Web Servers:** facilitate seamless data exchange and quick resource access.

https://securithings.com/hospital-physical-security/iot-devices-in-healthcare/
IoTs

==from those, we select the following==

sort by seriousness

### ==Electronic Health Record (EHR)==

**Reason:** EHRs store and exchange patient health information. They are used to track patient information over time, share between providers, and with patients. Because they hold the most sensitive regulated data (PHI), compromise would cause maximum impact (privacy breach, compliance violation, patient safety).

### ==Health Information Exchange (HIE)==

**Reason:** HIEs exchange patient information between different providers, care settings, and locations. They act as aggregation and transmission centers, so an attack could affect multiple organizations and amplify risk.

### ==Patient Portals==

**Reason:** Patient portals provide patients direct access to their health information. They are externally accessible, making them high-value targets for credential theft, identity fraud, and unauthorized access to PHI.

### Telehealth Systems

**Reason:** Telehealth systems provide healthcare services at a distance. They involve real-time video/audio sessions with sensitive clinical discussions. Attacks could compromise confidentiality and integrity of consultations.

### Clinical Decision Support Systems (CDSS)

**Reason:** CDSS help providers make better decisions about patient care. Manipulation could mislead clinicians, creating patient safety risks even if data is intact. Integrity is more critical than confidentiality here.

### IoT Medical Devices

**Reason:** IoT medical devices (infusion pumps, monitors, etc.) are increasingly network-connected. Vulnerabilities could allow attackers to interfere with device operations or use them as pivot points. Impact is high but depends on device availability and test feasibility.

### Communications

**Reason:** Communications platforms (messaging, VoIP, clinician collaboration) carry sensitive operational and clinical metadata. While breaches may expose schedules or conversations, the direct impact is generally lower than EHR/HIE but still relevant for phishing or impersonation.

### Web Servers

**Reason:** Web servers facilitate seamless data exchange and quick resource access. They are common attack surfaces and need hardening, but they typically act as entry points rather than core PHI systems.

### Enterprise Resource Planning (ERP)

**Reason:** ERP integrates business processes like HR, finance, and supply chain. Attacks may cause financial fraud or operational disruption but don’t directly compromise clinical data.

### ==Content Management Systems (CMS)==

**Reason:** CMS enable creation and exchange of digital content. While they may expose credentials or be used as phishing platforms, they are less critical to clinical operations compared to EHR/HIE.

reference:
https://www.gethealthie.com/glossary/it-infrastructure
https://kodjin.com/blog/it-infrastructure-in-healthcare/
https://securithings.com/hospital-physical-security/iot-devices-in-healthcare/


## Phase 2 : Intelligence Gathering

Hospitals maintain high transparency about faculty through websites, LinkedIn, research publications, and social media. While this supports trust and collaboration, it also supplies attackers with intelligence that can be weaponized for **social engineering**.

### OSINT Sources and What Attackers Learn

- **LinkedIn & Job Boards** → Staff roles, reporting lines, email patterns, and technology in use.
    
- **Hospital Website & Publications** → Names, contact details, internal structure, metadata from documents.
    
- **Social Media** → Personal interests, schedules, casual mentions of system changes or vendors.
    

### Key Risk

OSINT transforms public transparency into actionable intelligence, lowering the barrier for attackers to convincingly **impersonate trusted individuals** and manipulate staff into divulging credentials, opening attachments, or granting access.


## **Phase 3: Threat Modelling**

> How could attackers use social engineering here? (phishing, vishing, pretexting).
> What are their capabilities and intentions?

==source and citation==

### 1. **Phishing (email-based attacks)**

**Capabilities**

- Crafting lookalike emails (spoofed domains, typosquatting, stolen logos/branding).
    
- Embedding malicious links that mimic patient portals, telehealth logins, or EHR vendor pages.
    
- Using malware-laced attachments (malicious PDFs or invoices tied to ERP).
    
- Credential-harvesting landing pages for portals or VPNs.
    

**Intentions**

- **Credential theft**: Steal provider or patient logins for EHRs, HIE portals, or telehealth systems.
    
- **Initial foothold**: Deliver malware (keyloggers, ransomware) into hospital networks.
    
- **Lateral movement**: From one compromised account (say, a nurse’s) pivot into systems with higher privileges.
    
- **Data exfiltration**: PHI, billing, or scheduling data for resale or extortion.
    

**Examples**

- Fake “urgent lab results” email with a link to a malicious EHR login page.
    
- “Password expiry” notice redirecting staff to an attacker’s patient portal clone.
    
- Invoices disguised as ERP purchase orders containing malware.
    

### 2. **Vishing (voice-based attacks)**

**Capabilities**

- Caller ID spoofing to impersonate IT helpdesk, vendors, or clinical supervisors.
    
- Using social pressure and urgency (“we need to fix your EHR login now or your account will be suspended”).
    
- Exploiting confusion during emergencies or shift changes.
    

**Intentions**

- **Harvest MFA tokens**: Trick clinicians into reading back SMS/voice codes to complete logins.
    
- **Install remote software**: Convince staff to run remote desktop clients (“support tools”) for fake troubleshooting.
    
- **Bypass policies**: Persuade helpdesk staff to reset credentials or disable security controls.
    

**Examples**

- Attacker poses as the hospital IT team: “We noticed unusual activity on your patient portal account; please verify your MFA code.”
    
- Calls to a receptionist: “This is Dr. Smith from another clinic — I urgently need access to patient records, can you provide the login?”
    


### 3. **Pretexting (fabricated scenarios for trust)**

**Capabilities**

- Building convincing backstories with publicly available info (LinkedIn, hospital staff directories, press releases).
    
- Leveraging stolen PHI from previous breaches to sound legitimate.
    
- Tailoring communication to roles (billing clerk, clinician, biomedical engineer).
    

**Intentions**

- **Privilege escalation**: Trick staff into granting extra access rights (“I’m from the compliance audit team, need admin rights to export logs”).
    
- **Physical access**: Impersonate vendor/maintenance staff to access IoT devices or servers.
    
- **Supply chain infiltration**: Pose as external partners (labs, insurers) to request secure data transfers.
    

**Examples**

- Attacker emails IT ops claiming to be from an EHR vendor needing urgent access for a “security patch.”
    
- Fake biomedical engineer pretext to access IoT medical devices in restricted areas.
    
- Impersonating a regulator requesting PHI samples for an “audit.”
    


### 4. **Attacker profile: capabilities & intentions**

- **Capabilities**:
    
    - Access to phishing kits (ready-made EHR/portal clones).
        
    - Caller ID spoofing tools and AI voice cloning.
        
    - Data mining skills (scraping staff lists, press releases, social media).
        
    - Familiarity with healthcare terminology and workflows to sound authentic.
        
- **Intentions**:
    
    - **Financial gain**: Sell PHI on dark markets, conduct insurance fraud, ransomware campaigns.
        
    - **Espionage / competitive intelligence**: State-backed actors stealing research/clinical trial data.
        
    - **Disruption**: Criminals (or hacktivists) targeting hospitals for maximum visibility.
        
    - **Patient harm**: Rare, but altering CDSS or IoT devices to cause safety events.
        
reference:
https://www.hhs.gov/hipaa/for-professionals/security/guidance/cybersecurity-newsletter-october-2024/index.html
https://www.paubox.com/blog/phishing-scams-used-to-attack-healthcare-organizations
https://405d.hhs.gov/Documents/Five-Threat-Series-Email-Phishing-405d-R.pdf
