# STANDARDIZED ORGANIZATION

### Mandatory Directory Structure

The Llyod lab needs a space on the RDS the can be continously expanded as needed for memory.
[Here](https://www.imperial.ac.uk/admin-services/ict/self-service/research-support/rcs/service-offering/rds/) are a detailed description about RDS project allocated spaces.

```
/RDS_Lab_Storage/ # General lab RDS storage!
│
├── USERS/
│   └── YourName/
│       └── Project_YYYYMM_ShortName/    # Active projects, use when relevant
│           ├── project_overview.md      # REQUIRED – summary of project goals, collaborators, dates
│           ├── 001_EXPERIMENT_NAME/
│           │   ├── README.md            # REQUIRED – overview of this specific experiment
│           │   ├── metadata.yaml        # REQUIRED – structured metadata for reproducibility
│           │   ├── 01_raw_data/
│           │   │   ├── ELISA/
│           │   │   ├── PCR/
│           │   │   └── Viability/
│           │   ├── 02_processed/
│           │   ├── 03_analysis/
│           │   ├── 04_figures/
│           │   └── 05_other/
│           │
│           └── 002_EXPERIMENT_NAME2/    # Additional experiments follow same structure
│
│
├── 01_SHARED_DATASETS/                  # Shared or large datasets
│   ├── flow_cytometry/
│   ├── scRNAseq/
│   ├── spatial_transcriptomics/
│   └── IMC/
│
├── 02_ANALYSIS_PIPELINES/               # Cloned Github repo and validated analysis code for finalized pipelines
│   ├── imaging_pipeline/
│   ├── imc_pipeline/
│   └── scrna_pipeline/
│
│
└── 03_DOCUMENTATION/                    # Templates, SOPs, and guides
    ├── Templates/
    └── SOP_Protocols/
```
> **IMPORTANT NOTE:** Every raw data needs to be stored in the corresponding subdirectory in the *01_SHARED_DATASETS* folder!!! Everybody will have access to this shared datasets folder, so in this case we can avoid to keep copies of the large, complex raw datafiles in personal directories.

### File Naming Convention (Mandatory)

Naming files consistently is crucial for easy identification, retrieval, and organization. Do not use spaces, special characters or change capalization strategy in the file names.

This is only applicable for data generated in-house using low throughput methods (e.g., microscopy images, flow cytometry files, qPCR data, etc.) where file names can be controlled. Do **NOT** change file names for data exported from high-throughput instruments or software (e.g., sequencing data, mass spectrometry data, etc.); keep original filenames in these cases as analysis tools expect specific file names and formats.

Follow this convention for all files:

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

**Automated weekly check (Monday morning):**

A Bash script on the RDS automatically runs every Monday at 8:00 AM.
It generates a log file that can be reviewed for fixes.

> **Note:** The script checks only the **Lloyd Lab general space**.
> It does **not** scan personal home folders.

You can find more details on the [automation_tools](automation_tools.md) page.

**Manual enforcement:**

- Projects in `/NEEDS_ORGANIZATION/` cannot be worked on
- Must add missing files to restore access
- Data Steward reviews and approves restoration

---
