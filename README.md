# Data Management and Storage Plan for Llyod Lab

## 🎯 KEY CHALLENGES & SOLUTIONS

### Challenge 1: **Running Out of Space** ⚠️
**Current state:** 2TB RDS storage, generating large imaging data biweekly  

**Immediate Actions:**
1. ✅ Compress old imaging data (300-500GB recovery)
2. ✅ Archive completed projects externally (200-300GB recovery)
3. ✅ Remove redundant processed files (100-200GB recovery)
4. ✅ Set up automated storage monitoring

### Challenge 2: **Backup/Redundancy** 💾
**Current state:** No backup strategy  
**Target:** 3-2-1 backup rule (3 copies, 2 media, 1 offsite)  

**Immediate Actions:**
1. ✅ Identify key storage locations (OneDrive, RDS personal, RDS projects, external hardrives)
2. ✅ Create hierarchy of data storage for key datasets (confocal, flow cytometry, IMC, RNAseq, spatial transcriptomics) 
4. ✅ Create disaster recovery protocol

### Challenge 3: **Lack of Organization** 📁
**Current state:** Unclear where files should go  
**Target:** Standardized directory structure with enforcement  

**Immediate Actions:**
1. ✅ Deploy mandatory directory template
2. ✅ Create "Where does this go?" decision tree
3. ✅ Implement monthly organization compliance checks
4. ✅ Migrate existing data to new structure

### Challenge 4: **Clear Structure/Guidelines** 📋
**Current state:** No documented protocols  
**Target:** Simple, enforceable one-page guides  

**Immediate Actions:**
1. ✅ Create quick-reference cards (starting project, saving data, monthly hygiene)
2. ✅ Establish mandatory naming conventions
3. ✅ Set up automated validation tools
4. ✅ Train all lab members (1-hour session)

---

## 🚨 IMPLEMENTATION CHECKLIST

### Assessment & Quick Wins
- [ ] Run storage audit (identify space hogs)
- [ ] Audit external hard drive for backup space
- [ ] Identify 3-5 completed projects (or personel) to archive
- [ ] List all imaging data >1 year old

### Space Recovery
- [ ] Compress 5 largest old imaging datasets
- [ ] Move completed projects to archive staging
- [ ] Delete temporary analysis files from all projects

### Backup Setup
- [ ] Connect external HDD
- [ ] Install backup automation scripts
- [ ] Run first full backup
- [ ] Verify backup integrity

### Organization Rollout
- [ ] Create directory template on RDS
- [ ] Generate README and metadata templates
- [ ] Print and post quick-reference cards
- [ ] Schedule lab meeting for training

---

## 💾 SOLUTION 1: SPACE RECOVERY

#### Action 1: Compress Old Imaging Data (Expected: 300-500GB recovery)

**What to compress:**
- All microscopy images older than 1 year
- All folders from past personel
- IMC data from completed experiments
- Any TIFF files not currently being analyzed

**How to compress:**
```bash
# Quick compression of TIFF files
find /path/to/imaging -name "*.tif" -mtime +180 -exec python compress_image.py {} \;
```
`compress_image.py` located in ADD/PATH/TO/FILE

**Expected results:**
- 30-50% size reduction with lossless compression
- No quality loss, maintains all metadata

#### Action 2: Archive Completed Projects

**What to archive:**
- Published papers (raw data already deposited in public repos)
- Failed experiments (documented but not analyzed further)
- Superseded preliminary data

**Where to archive:**
- External hard drive
- Institutional archive service (check if available)

**Archive process:**
1. Copy to external storage (with checksum verification)
2. Compress before archiving (ZIP with medium compression)
3. Keep compressed copy on RDS for 30 days
4. Delete from active RDS after verification period

#### Action 3: Remove Redundant Files (Expected: 100-200GB recovery)

**Safe to delete:**
- ❌ Multiple versions of processed data (keep only: raw + final processed + analysis)
- ❌ Intermediate analysis files (Jupyter notebook outputs, cache files)
- ❌ QC plots and reports (keep summary only, regenerate if needed)
- ❌ Duplicate files from failed transfers (use fdupes to find)
- ❌ Temporary files in /tmp directories never cleaned

**How to identify:**
```bash
# Find duplicate files
fdupes -r /path/to/RDS > duplicates.txt

# Find large files not accessed in 180 days
find /path/to/RDS -type f -size +100M -atime +180 -ls > large_old_files.txt

# Find jupyter checkpoint files
find /path/to/RDS -name ".ipynb_checkpoints" -type d -exec du -sh {} \;
```

#### Action 4: Set Up Storage Monitoring (Prevent future crises)

**Automated weekly monitoring:**
- Check total storage usage
- Alert when exceeds 80% capacity (warning)
- Alert when exceeds 90% capacity (critical)
- Email report to Data Steward and PI

**See storage_monitor.py script provided**

### Storage Optimization by Data Type

#### Imaging Data

**Problem:** Generates most data biweekly, quickly fills storage

**Solutions:**
1. **Immediate compression** (30-50% reduction)
   - Convert TIFF → OME-TIFF with LZW compression
   - No quality loss, maintains metadata
   
2. **Tiered storage** by age:
   - <3 months: Keep original on RDS (active work)
   - 3-12 months: Compressed OME-TIFF on RDS
   - >12 months: Archive to external HDD, keep only thumbnails on RDS

3. **Delete intermediate files:**
   - Keep: Raw images + final processed images
   - Delete: All intermediate processing steps (can regenerate)

**Expected space savings:** 40-60% of imaging storage

#### IMC Data

**Problem:** Large MCD files + extracted TIFF duplicates

**Solutions:**
1. Keep only MCD files (raw data)
2. Delete extracted TIFFs after analysis complete
3. Compress MCD files in HDF5 format (30% reduction)

#### scRNA-seq

**Solutions:**
1. Archive raw FASTQ files to external storage
2. Keep only processed count matrices on RDS
3. Use Parquet format for count matrices (50-70% reduction)
   

#### Spatial Transcriptomics

**Solutions:**
1. Keep original files off Xenium machine
2. Keep compressed back up 

---

## 🔒 SOLUTION 2: BACKUP & REDUNDANCY STRATEGY

### The 3-2-1 Rule (Industry Standard)

**3 copies of data:**
- 1 primary (RDS)
- 2 backups (external HDD + OneDrive)

**2 different media types:**
- RDS (RAID storage)
- External hard drive (geographically separated)
- OneDrive (different technology) 

**1 offsite copy:**
- External HDD at PI's office

### Recommended Setup for Your Lab

**What gets backed up where:**

**Tier 1 - Critical (3 copies):**
- Raw data from active projects
- Metadata files
- Unpublished analysis results
→ RDS + External HDD + Cloud

**Tier 2 - Important (2 copies):**
- Processed data
- Analysis code
- Published data
→ RDS + External HDD

**Tier 3 - Reproducible (1 copy):**
- Analysis outputs
- Figures for presentations
- Exploratory notebooks
→ RDS only

### Automated Backup Schedule

**Daily (5 minutes, automated):**
- Metadata files (metadata.yaml, README.md)
- Lab notebooks
- Code repositories (git push)

**Weekly (2 hours, automated):**
- New raw data from past 7 days
- Updated processed datasets

**Monthly (manual, 30 minutes):**
- Full backup verification
- Rotate external HDD offsite
- Cloud sync critical data

### Backup Scripts (Automated)

**Script 1: Daily Metadata Backup**
```bash
#!/bin/bash
# Backs up all metadata files daily
rsync -av --include='metadata.yaml' --include='README.md' --exclude='*'   /RDS/00_ACTIVE_PROJECTS/ /backup/daily_metadata/
```

**Script 2: Weekly Raw Data Backup**
```bash
#!/bin/bash
# Backs up new raw data weekly
find /RDS/00_ACTIVE_PROJECTS -name "01_raw_data" -type d -mtime -7 |   xargs -I {} rsync -av {} /backup/weekly_rawdata/
```

**Script 3: Monthly Cloud Sync**
```bash
#!/bin/bash
# Syncs critical data to cloud monthly
rclone sync /RDS/00_ACTIVE_PROJECTS/*/01_raw_data/   backblaze:lab-backup/raw_data/   --progress
```

**See detailed scripts in automation section**

### Disaster Recovery Plan

**Scenario 1: RDS System Failure**
1. Use external HDD as temporary working storage
2. Continue critical experiments
3. Restore to new RDS when available

**Scenario 2: Ransomware Attack**
1. Disconnect RDS immediately
2. Do NOT connect external HDD (may be infected)
3. Restore from cloud backup to new clean system

**Scenario 3: Accidental Deletion**
1. Check RDS trash/snapshots (if available)
2. Restore from last weekly external HDD backup
3. If >1 week old, restore from monthly cloud backup

**Recovery Time:**
- Critical data: <4 hours (from external HDD)
- Important data: <24 hours
- Reproducible data: <1 week (regenerate)

---

## 📂 SOLUTION 3: STANDARDIZED ORGANIZATION

### Mandatory Directory Structure

```
/RDS_Lab_Storage/
│
├── 00_ACTIVE_PROJECTS/          # Current work (<6 months)
│   └── Project_YYYYMM_Name/
│       ├── README.md            # REQUIRED
│       ├── metadata.yaml        # REQUIRED
│       ├── 01_raw_data/
│       │   ├── imaging/
│       │   ├── imc/
│       │   ├── scrnaseq/
│       │   └── spatial/
│       ├── 02_processed/
│       ├── 03_analysis/
│       ├── 04_figures/
│       └── 05_manuscript/
│
├── 01_ARCHIVED_PROJECTS/        # Completed (>6 months)
│   └── [Same structure]
│
├── 02_SHARED_DATASETS/          # Reference data
│   ├── Public_scRNAseq/
│   └── Reference_Genomes/
│
├── 03_ANALYSIS_PIPELINES/       # Reusable code
│   ├── imaging_pipeline/
│   ├── imc_pipeline/
│   └── scrna_pipeline/
│
├── 04_ARCHIVE_READY/            # Staging for external archival
│
└── 99_DOCUMENTATION/            # Templates & guides
    ├── Templates/
    └── Protocols/
```

### File Naming Convention (Mandatory)

**Format:**
```
YYYYMMDD_DataType_Sample_Condition.extension
```

**Examples:**

**Imaging:**
```
20240115_Confocal_MouseBrain_Section1_DAPI.tif
20240115_Confocal_MouseBrain_Section1_GFP.tif
```

**IMC:**
```
20240115_IMC_Tumor_Patient01_Core1.mcd
20240115_IMC_Panel_37markers.csv
```

**scRNA-seq:**
```
20240115_scRNAseq_PBMC_Donor01_counts.h5ad
20240115_scRNAseq_PBMC_Donor01_filtered.h5ad
```

**Analysis outputs:**
```
20240115_DiffExp_TumorVsNormal_DESeq2.csv
20240115_Clustering_Res08_UMAP.pdf
```

### Decision Tree: "Where Does This File Go?"

**START: I have a new file**

❓ Is it RAW data from instrument?  
   → YES: `01_raw_data/[data_type]/`  
   → NO: Continue

❓ Is it PROCESSED/QC'd data?  
   → YES: `02_processed/`  
   → NO: Continue

❓ Is it ANALYSIS code or results?  
   → YES: `03_analysis/`  
   → NO: Continue

❓ Is it a FIGURE for publication?  
   → YES: `04_figures/`  
   → NO: Continue

❓ Is it SHARED reference data?  
   → YES: `02_SHARED_DATASETS/`  
   → NO: Ask Data Steward

### Enforcement Mechanisms

**Automated weekly check (Mondays):**
```bash
# Check all projects have required files
find /RDS/00_ACTIVE_PROJECTS -type d -maxdepth 1 | while read project; do
  if [ ! -f "$project/README.md" ]; then
    echo "MISSING README: $project" >> /var/log/compliance_issues.txt
    mv "$project" /RDS/NEEDS_ORGANIZATION/
  fi
  if [ ! -f "$project/metadata.yaml" ]; then
    echo "MISSING METADATA: $project" >> /var/log/compliance_issues.txt
    mv "$project" /RDS/NEEDS_ORGANIZATION/
  fi
done

# Email compliance report to Data Steward
mail -s "Weekly Organization Compliance Report" data-steward@uni.edu < /var/log/compliance_issues.txt
```

**Manual enforcement:**
- Projects in `/NEEDS_ORGANIZATION/` cannot be worked on
- Must add missing files to restore access
- Data Steward reviews and approves restoration

---

## 📋 SOLUTION 4: CLEAR GUIDELINES

### One-Page Quick Reference Cards

#### CARD 1: Starting a New Project

**☑ NEW PROJECT CHECKLIST** (15 minutes)

1. [ ] Create folder: `Project_YYYYMM_ShortName`
2. [ ] Copy template README.md from `/99_DOCUMENTATION/Templates/`
3. [ ] Fill in README.md (project title, PI, description, data types)
4. [ ] Copy template metadata.yaml
5. [ ] Fill in metadata.yaml (at minimum: project_id, pi, start_date)
6. [ ] Create subdirectories:
   - 01_raw_data/ (with data type folders)
   - 02_processed/
   - 03_analysis/
   - 04_figures/
7. [ ] Add project to lab inventory: `/99_DOCUMENTATION/project_inventory.xlsx`
8. [ ] Notify Data Steward via email

**Time investment:** 15 minutes  
**Prevents:** Hours of future confusion and data loss

---

#### CARD 2: Saving New Data

**☑ NEW DATA CHECKLIST** (5 minutes per dataset)

1. [ ] Save to correct location:
   - Imaging → `01_raw_data/imaging/`
   - IMC → `01_raw_data/imc/`
   - scRNA-seq → `01_raw_data/scrnaseq/`
   - Spatial → `01_raw_data/spatial/`

2. [ ] Use naming convention:
   `YYYYMMDD_DataType_Sample_Condition.ext`

3. [ ] Generate checksum:
   ```bash
   sha256sum myfile.tif > myfile.tif.sha256
   ```

4. [ ] Update metadata.yaml:
   - Add new dataset entry
   - Record date, sample info, experimental conditions

5. [ ] Backup will run automatically (weekly)

**Time investment:** 5 minutes  
**Prevents:** Data corruption, lost samples, cannot reproduce results

---

#### CARD 3: Monthly Data Hygiene

**☑ MONTHLY CHECKLIST** (1 hour per month)

**Week 1:**
- [ ] Run storage monitor: `python storage_monitor.py /RDS`
- [ ] Review storage report
- [ ] If >80% full, proceed to emergency cleanup

**Week 2:**
- [ ] Compress imaging data >3 months old
- [ ] Expected recovery: 100-200GB
- [ ] Run: `python compress_old_imaging.py --days 90`

**Week 3:**
- [ ] Move projects >6 months inactive to `01_ARCHIVED_PROJECTS/`
- [ ] Delete temporary analysis files (cache/, *.tmp)
- [ ] Find: `find /RDS -name "cache" -type d -exec rm -rf {} \;`

**Week 4:**
- [ ] Verify backup integrity (spot check 5 random files)
- [ ] Rotate external HDD (swap onsite/offsite)
- [ ] Update lab data inventory

**Time investment:** 1 hour per month  
**Prevents:** Storage crises, data loss, backup failures

---

### Mandatory Templates

#### README.md Template (Required for all projects)

```markdown
# Project: [Title]

## Project Info
- **ID:** Project_YYYYMM_Name
- **PI:** [Name]
- **Lead:** [Name]
- **Start:** YYYY-MM-DD
- **Status:** Active/Archived/Published

## Description
[2-3 sentences describing research question]

## Data Types
- [ ] Imaging
- [ ] IMC
- [ ] scRNA-seq
- [ ] Spatial transcriptomics

## Key Files
- Raw data: `01_raw_data/`
- Processed: `02_processed/`
- Analysis: `03_analysis/`
- Figures: `04_figures/`

## Notes
[Any important notes about this project]

## Publications
[List any papers from this project]
```

#### metadata.yaml Template (Required for all projects)

```yaml
# Project Metadata
project_id: "Project_YYYYMM_Name"
pi_name: "Dr. Name"
pi_email: "pi@university.edu"
lead_researcher: "Researcher Name"
start_date: "YYYY-MM-DD"
status: "active"  # active, archived, published
funding_source: "Grant XYZ"

# Data Summary
data_types:
  - imaging
  - imc
  - scrnaseq
  - spatial

total_size_gb: 0  # Update periodically

# Raw Data Inventory
raw_data:
  - dataset_id: "20240115_Imaging_Experiment1"
    date_acquired: "2024-01-15"
    data_type: "imaging"
    modality: "confocal"
    sample_type: "mouse_brain"
    size_gb: 50
    location: "01_raw_data/imaging/20240115_Experiment1/"
    notes: "Initial pilot experiment"

# Processing History
processing_log:
  - date: "2024-01-20"
    action: "Segmentation and quantification"
    software: "CellProfiler 4.2"
    output: "02_processed/imaging/20240120_segmented/"

# Publications
publications: []

# Last Updated
last_updated: "YYYY-MM-DD"
updated_by: "Name"
```

---

### Training Materials

#### 1-Hour Lab Meeting Training Agenda

**Agenda:**
1. **Why we need this** (10 min)
   - Current problems: running out of space, lost data, cannot find files
   - Benefits: save time, prevent data loss, meet funder requirements

2. **Directory structure tour** (15 min)
   - Walk through folder hierarchy
   - Show example project
   - Explain where each file type goes

3. **File naming demo** (10 min)
   - Show good vs. bad names
   - Practice with examples
   - Common mistakes to avoid

4. **Hands-on practice** (20 min)
   - Each person creates a test project
   - Save a test file with correct naming
   - Generate checksum
   - Update metadata.yaml

5. **Q&A and resources** (5 min)
   - Where to find templates
   - Who to ask for help (Data Steward)
   - Printed quick-reference cards

**Materials needed:**
- Printed quick-reference cards (one per person)
- Access to RDS for hands-on practice
- Example "good" project to show

#### Training Checklist (For each lab member)

**New Lab Member Onboarding:**
- [ ] Attend 1-hour training session
- [ ] Read complete data management plan
- [ ] Create a test project (supervised)
- [ ] Save test data with correct naming
- [ ] Update metadata file
- [ ] Generate checksums
- [ ] Demonstrate understanding to Data Steward

**Sign-off:**
- Lab member: _________________ Date: _______
- Data Steward: _______________ Date: _______

---

## 🔧 AUTOMATION TOOLS

### Tool 1: Storage Monitor (Prevent crises)

**Purpose:** Alert before running out of space

**Usage:**
```bash
# Run weekly (automated via cron)
python storage_monitor.py /RDS_Lab_Storage --threshold-warning 80 --threshold-critical 90
```

**Output:**
- Email alert when >80% full (warning)
- Email alert when >90% full (critical)
- Weekly report of storage trends

**See storage_monitor.py script (provided earlier)**

---

### Tool 2: Imaging Compressor (Free up space)

**Purpose:** Compress old imaging data automatically

**Usage:**
```bash
# Compress all TIFF images older than 90 days
python compress_imaging.py --input /RDS/00_ACTIVE_PROJECTS --days-old 90 --format ome-tiff
```

**Expected results:**
- 30-50% size reduction
- No quality loss
- Maintains all metadata
- Automatically verifies integrity

---

### Tool 3: Organization Validator (Enforce structure)

**Purpose:** Check projects follow required structure

**Usage:**
```bash
# Check all active projects weekly
python validate_organization.py /RDS/00_ACTIVE_PROJECTS
```

**Checks:**
- README.md exists
- metadata.yaml exists and valid
- File naming conventions followed
- Required subdirectories present

**Output:**
- List of non-compliant projects
- Specific issues for each project
- Email report to Data Steward

---

### Tool 4: Backup Verifier (Ensure backups work)

**Purpose:** Verify backup integrity automatically

**Usage:**
```bash
# Verify all checksums in backup directory
python verify_backup.py /backup/external_hdd
```

**Checks:**
- All files have checksums
- Checksums match actual file hashes
- No corrupted files in backup

**Output:**
- Number of files verified
- List of any errors found
- Email report if errors detected

---

## 📊 SUCCESS METRICS

### Month 1 Goals

**Space Management:**
- [ ] 500GB+ storage recovered
- [ ] Storage usage <70%
- [ ] All imaging data >6 months compressed

**Backup:**
- [ ] External HDD purchased and connected
- [ ] Weekly automated backup running
- [ ] Cloud backup account set up

**Organization:**
- [ ] All active projects follow directory structure
- [ ] All projects have README.md and metadata.yaml
- [ ] 0 projects in /NEEDS_ORGANIZATION/

**Guidelines:**
- [ ] All lab members trained (100%)
- [ ] Quick-reference cards posted
- [ ] Templates available in /99_DOCUMENTATION/

### Month 3 Goals

**Space Management:**
- [ ] Storage usage stable at <75%
- [ ] No emergency cleanup needed
- [ ] Automated compression running monthly

**Backup:**
- [ ] 3 successful backup verifications
- [ ] Disaster recovery plan tested
- [ ] Offsite rotation established

**Organization:**
- [ ] 100% compliance with naming conventions
- [ ] All new projects use templates
- [ ] Automated validation running weekly

**Guidelines:**
- [ ] <5 organization questions per month
- [ ] All new data saved correctly first time
- [ ] Lab members confident with system

### Month 6 Goals

**Space Management:**
- [ ] Storage usage <70% consistently
- [ ] Predictable storage growth
- [ ] No manual intervention needed

**Backup:**
- [ ] 6+ successful monthly verifications
- [ ] Zero data loss incidents
- [ ] Backup costs within budget

**Organization:**
- [ ] Organization is now "default behavior"
- [ ] Old projects migrated to new structure
- [ ] Publication-ready data organization

**Guidelines:**
- [ ] System integrated into lab culture
- [ ] New members onboard smoothly
- [ ] Minimal Data Steward time required

---

## 💰 BUDGET SUMMARY

### One-Time Costs

| Item | Purpose | Cost |
|------|---------|------|
| 4TB External HDD | Primary backup | $100 |
| 2TB External HDD | Offsite rotation | $80 |
| Label maker | Label drives/projects | $25 |
| **Total One-Time** | | **$205** |

### Recurring Costs

| Item | Purpose | Cost/Month | Cost/Year |
|------|---------|------------|-----------|
| Cloud storage (1TB) | Offsite backup | $50 | $600 |
| **Total Recurring** | | **$50/month** | **$600/year** |

### Time Investment

| Role | Activity | Time/Week | Time/Year |
|------|----------|-----------|-----------|
| Data Steward | Ongoing management | 2-4 hours | 100-200 hours |
| PI | Oversight | 0.5 hours | 25 hours |
| Lab members | Compliance | 0.5 hours | 25 hours each |

### Return on Investment

**Costs:**
- Financial: $205 + $600/year = $805 first year
- Time: 150-250 hours first year (front-loaded)

**Benefits:**
- Prevent data loss (priceless for years of research)
- Save 5-10 hours/person/month in finding files
- Meet funder requirements (enable grant submissions)
- Enable collaboration and data sharing
- Reduce stress and last-minute crises

**ROI:** 10-20x in time savings alone

---

## 🎯 IMPLEMENTATION ROADMAP

### Week 1: Assessment & Planning
- [ ] Read complete plan
- [ ] Run storage audit
- [ ] Purchase backup hardware
- [ ] Designate Data Steward
- [ ] Schedule lab training

### Week 2: Quick Wins
- [ ] Compress 5 largest old datasets
- [ ] Archive 3 completed projects
- [ ] Set up directory structure
- [ ] Install automation scripts
- [ ] Train lab members

### Week 3-4: Full Deployment
- [ ] Migrate all projects to new structure
- [ ] Set up automated backups
- [ ] Test disaster recovery
- [ ] Verify all compliance

### Month 2-3: Optimization
- [ ] Fine-tune automation
- [ ] Address compliance issues
- [ ] Optimize storage allocation
- [ ] Refine protocols

### Month 4-6: Sustainability
- [ ] Monitor metrics
- [ ] Reduce Data Steward time
- [ ] System becomes automatic
- [ ] Focus on continuous improvement

---

## 📞 GETTING HELP

### Data Steward Responsibilities
- Answer "where does this go?" questions
- Weekly compliance checks
- Monthly storage audits
- Backup verification
- Training new members

### When to Ask Data Steward
- ❓ Unsure where to save a file
- ❓ Need to create unusual project structure
- ❓ Storage getting full
- ❓ Backup questions or issues
- ❓ Need help finding old data

### Escalate to PI When
- 🚨 Storage >90% full despite cleanup
- 🚨 Backup failure
- 🚨 Data loss incident
- 🚨 Repeated compliance violations
- 🚨 Need additional budget for storage

---

## 📚 APPENDIX: QUICK REFERENCE

### Directory Structure (1-page poster)
[Print and post in lab]

### File Naming Examples (1-page card)
[Keep at each computer]

### Monthly Checklist (1-page card)
[Post on Data Steward's desk]

### Emergency Contacts
- Data Steward: [email]
- PI: [email]
- IT Support: [phone/email]
- Backup Service: [support contact]

---

**Document Version:** 2.0  
**Last Updated:** 2025-10-17  
**Next Review:** 2026-01-17

**Document Owner:** Data Steward  
**Approved By:** PI

---

*This plan is a living document. Please provide feedback and suggestions for improvement to the Data Steward.*
