# GUIDELINES

### One-Page Quick Reference Cards

#### Starting a New Project

**☑ NEW PROJECT CHECKLIST** (15 minutes)

Each Llyod lab project must follow the standardized directory structure and include required documentation files.
Projects should be stored in the Llyod lab RDS in the relevant users folder name.

Example path:
`RDS/usrs/YourName/Project_YYYYMM_ShortName/001_EXPERIMENT_NAME/`

1. [ ] Create folder: `Project_YYYYMM_ShortName` when starting a new project
2. [ ] Copy template README.md from `/99_DOCUMENTATION/Templates/` (ADD LINK)
3. [ ] Fill in README.md (project title, PI, description, data types)
4. [ ] Copy template metadata.yaml (ADD LINK)
5. [ ] Fill in metadata.yaml (at minimum: project_id, pi, start_date)
6. [ ] Create subdirectories:
   - 01_raw_data/ (with data type folders)
   - 02_processed/
   - 03_analysis/
   - 04_figures/
7. [ ] Add project to lab inventory: `/99_DOCUMENTATION/project_inventory.xlsx`

**Time investment:** 15 minutes  
**Prevents:** Hours of future confusion and data loss

---

#### Saving New Data

**☑ NEW DATA CHECKLIST** (5 minutes per dataset)

1. [ ] Save to correct location:
   - Imaging → `raw_data/imaging/`
   - IMC → `raw_data/imc/`
   - scRNA-seq → `raw_data/scrnaseq/`
   - Spatial → `raw_data/spatial/`

2. [ ] Use naming convention:
   `YYYYMMDD_DataType_Sample_Condition.ext`

3. [ ] Update metadata.yaml:
   - Add new dataset entry
   - Record date, sample info, experimental conditions


**Time investment:** 5 minutes  
**Prevents:** Data corruption, lost samples, cannot reproduce results

---

#### Monthly Data Hygiene

**☑ MONTHLY CHECKLIST** (1 hour per month)

*BALAZS: Is this realistic to expect lab members to do this every month? How can we adapt to make it easier? Automate at all?*

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

## Data storage location
- OneDrive Link: [Insert link]
- RDS Path: `/RDS/usrs/YourName/Project_YYYYMM_ShortName/`
- External HDD ID: [Insert ID]

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