# GUIDELINES

## Starting a New Project

**☑ NEW PROJECT CHECKLIST** (15 minutes)

Each Llyod lab project must follow the standardized directory structure and include required documentation files.
Projects should be stored in the Llyod lab RDS in the relevant users folder name.

Example path:
`RDS/USERS/YourName/Project_YYYYMM_ShortName/001_EXPERIMENT_NAME/`

0. [ ] Give project a short, descriptive name (no spaces) - every project must have a unique name
1. [ ] Create folder: `Project_YYYYMM_ShortName` when starting a new project
2. [ ] Create project_overview.md  from the [templates]() folder
3. [ ] Create subfolder: `001_EXPERIMENT_NAME` for each experiment within the project
4. [ ] Copy template README.md from the [templates](https://github.com/LloydLab/Data-Stroage-and-Managment/blob/main/templates/README.md) folder
5. [ ] Fill in README.md (project title, PI, description, data types)
6. [ ] Copy template metadata.yaml from the [templates](https://github.com/LloydLab/Data-Stroage-and-Managment/tree/main/templates) folder

There are several versions of metadata.yaml depending on data types used in the experiment. We have templates for the following formats:
   - [General](https://github.com/LloydLab/Data-Stroage-and-Managment/blob/main/templates/metadata_general.yaml)
   - [Mouse](https://github.com/LloydLab/Data-Stroage-and-Managment/blob/main/templates/metadata_mouse.yaml)
   - [Dry lab] (https://github.com/LloydLab/Data-Stroage-and-Managment/blob/main/templates/metadata_dry.yaml)

7. [ ] Fill in metadata.yaml (at minimum: project_id, pi, start_date)
8. [ ] Create subdirectories in experimen subfolder:
   - 01_raw_data/ (with data type folders)
   - 02_processed/
   - 03_analysis/
   - 04_figures/
   - 05_docs/

**Time investment:** 15 minutes
**Prevents:** Hours of future confusion and data loss!

---

## Saving New Data

**☑ NEW DATA CHECKLIST** (5 minutes per dataset)

1. [ ] Save to correct location:
   - Imaging → `raw_data/imaging/`
   - IMC → `raw_data/imc/`
   - scRNA-seq → `raw_data/scrnaseq/`
   - Spatial → `raw_data/spatial/`

2. [ ] Use naming convention:
   `YYYYMMDD_DataType_Sample_Condition.ext`
   *Where data is exported from instrument/software with a particular nomenclature, keep original filenames instead of renaming files.*

3. [ ] Update metadata.yaml:
   - Add new dataset entry
   - Record date, sample info, experimental conditions

**Time investment:** 5 minutes
**Prevents:** Data corruption, lost samples, cannot reproduce results

---

## Monthly Data Hygiene

**☑ MONTHLY CHECKLIST** (1 hour per month)

For this section, automatic bash scripts are running on the RDS continously.

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

Balazs Bohar has created several scripts to help with monthly data hygiene. You can find more details on the [automation_tools](automation_tools.md) page. For any questions, please reach out to him directly.


---
