# GUIDELINES

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