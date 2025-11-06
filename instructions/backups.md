## BACKUP & REDUNDANCY STRATEGY

All research data must be backed up regularly to prevent data loss. This document outlines the lab's backup strategy, including recommended practices, and disaster recovery plans.

It is critical that large datasets, especially raw imaging data or omic datasets, are backed up in multiple locations to ensure data integrity and availability. The type of dataset will determine the exact backup method used. The location of backup should follow the guidance here, however the location (i.e path) of the data backup should be included in written or electronic lab notebook the work can be easily located.

**All lab members should save their data in the lab's shared RDS storage system as the primary location. This ensures that data is centrally stored and accessible to all authorized lab members**. This includes IMC, Imaging, Flow Cytometry, scRNA-seq, bulk RNA-seq, Proteomics, Spatial Transcriptomics data etc. These files should be stored on the lab RDS at the following path: `/RDS/LLYOD` (I would suggest Clares's RDS file). Large datasets should be stored in the relative project folder e.g `/RDS/LLYOD/RAW_DATA/scRNAseq/`.

*Note to Clare: This is going to require you to have an RDS account with sufficient storage space for all lab members data. You might need to purchase more eventually. All the data will be compressed to maximize the available space.*


### The 3-2-1 Rule (Industry Standard)

For all precious data (link to page that says what is critical data), follow the 3-2-1 backup rule:

**3 copies of data:**

- Working copy (project or personal RDS or OneDrive)
- 1 primary back up (general RDS, compressed)
- 1 secondary backup (external hard drive at PI's office)

### Backup Tiers

**What gets backed up where:**

What data is critical and needs multiple backups?

**Tier 1 - Critical (3 copies):**

- Raw imaging data (confocal, etc)
- Imaging Mass Cytometry (MCD files, raw data)
- Raw sequencing data (FASTQ files)
- Spatial transcriptomics raw data files
- Proteomics raw data files
- Metabolomics raw data files

*All relevant metadata associated with the raw data need to be easily accessible! This includes lab notebook entries, analysis code, README files, metadata.yaml files etc*

For more information on what needs to be included in a metadata file, see the [Project Structure](project_structure.md) page.

**Tier 2 - Important (2 copies):**

- Flow cytometry raw data files (FCS)

**Tier 3 - Low priority (1 copy):**

- All other data (ELISA, PCR, viability assays, etc)

### Disaster Recovery Plan

**Scenario 1: RDS System Failure**

If the RDS system fails or data is corrupted, there are multiple backup locations to restore maintained by ICL RDS team. Reach out to them in case of failure.

**Scenario 2: Accidental Deletion**

1. Check RDS trash/snapshots (if available)
2. Restore from external hard drive backup
3. Restore from OneDrive backup if needed

# QUESTIONS FOR CLARE

- What will be the location for general lab RDS back up? 
- What data do you want backed up prior to personal leaving the lab?

  - Flow, imaging, IMC, RNAseq, ST, proteomic, metabolomic data?
  - Any shared datasets used by multiple people?
  - Is there any additional data that should be stored in back up locations following generation?

- Any PCR, ELISA, Viability data that should only be stored in the users OneDrive
- Upon leaving the Llyod lab, users should compress and archieve their experimental data and keep a copy on the RDS (need to decide which project? Might make most sense for Clare to get an RDS like Phil and use that as long term storage for all the lab data) and on the external hard drive.