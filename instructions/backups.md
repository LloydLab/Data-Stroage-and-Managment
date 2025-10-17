## BACKUP & REDUNDANCY STRATEGY

All research data must be backed up regularly to prevent data loss. This document outlines the lab's backup strategy, including recommended practices, automated tools, and disaster recovery plans.

It is critical that large datasets, especially raw imaging data or omic datasets, are backed up in multiple locations to ensure data integrity and availability. The type of dataset will determine the exact backup method used. The location of backup should follow the guidance here, however the location (i.e path) of the data backup should be included in written or electronic lab notebook.

### The 3-2-1 Rule (Industry Standard)

For all precious data (link to page that says what is critical data), follow the 3-2-1 backup rule:

**3 copies of data:**

- 1 primary (RDS)
- 2 backups (external HDD + OneDrive)

**2 different media types:**

- RDS (RAID storage)
- External hard drive (geographically separated)
- OneDrive (different technology) 

**1 offsite copy:**

- External HDD at PI's office

### Backup Tiers

**What gets backed up where:**

**Tier 1 - Critical (3 copies):**

- Raw data from active projects
- Metadata files
- Unpublished analysis results

**Tier 2 - Important (2 copies):**

- Processed data
- Published data
→ RDS + External HDD

**Tier 3 - Reproducible (1 copy):**

- Analysis outputs
- Figures for presentations
- Exploratory notebooks
→ RDS only

### Disaster Recovery Plan

**Scenario 1: RDS System Failure**

1. Use external hard drive as temporary working storage
2. Continue critical experiments
3. Restore to new RDS when available

**Scenario 2: Ransomware Attack**

1. Disconnect RDS immediately
2. Do NOT connect external external hard drive (may be infected)
3. Restore from cloud backup to new clean system

**Scenario 3: Accidental Deletion**

1. Check RDS trash/snapshots (if available)
2. Restore from external hard drive backup
3. Restore from monthly OneDrive backup if needed

**Recovery Time:**

- Critical data: <4 hours
- Important data: <24 hours

# QUESTIONS FOR CLARE

- What data do you want backed up prior to personal leaving the lab?

  - Flow, imaging, IMC, RNAseq, ST, proteomic, metabolomic data?
  - Any shared datasets used by multiple people?
  - Is there any additional data that should be stored in back up locations following generation?

- Any PCR, ELISA, Viability data that should only be stored in the users OneDrive
- Upon leaving the Llyod lab, users should compress and archieve their experimental data and keep a copy on the RDS (need to decide which project? Might make most sense for Clare to get an RDS like Phil and use that as long term storage for all the lab data) and on the external hard drive.

