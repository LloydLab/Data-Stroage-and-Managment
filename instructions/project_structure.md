# STANDARDIZED ORGANIZATION

### Mandatory Directory Structure

The Llyod lab needs a space on the RDS the can be continously expanded as needed for memory. This will cost to 

```
/RDS_Lab_Storage/ # General lab RDS storage
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

### File Naming Convention (Mandatory)

Naming files consistently is crucial for easy identification, retrieval, and organization. Do not use spaces, special characters or change capalization strategy in the file names.

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

*BALAZS: Is this realistic to expect lab members to do this every month? How can we adapt to make it easier? Automate at all?*

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