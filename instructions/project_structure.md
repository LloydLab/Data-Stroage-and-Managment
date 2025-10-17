# STANDARDIZED ORGANIZATION

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