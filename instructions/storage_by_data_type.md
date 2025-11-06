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

1. Archive raw FASTQ files to external storage
2. Keep only processed count matrices on RDS
3. Use Parquet format for count matrices (50-70% reduction)

#### bulk RNA-seq

#### Proteomics

#### Spatial Transcriptomics

**Solutions:**

1. Keep original files off Xenium machine on external HDD
2. Keep compressed back up on RDS project folder
3. Delete intermediate analysis files after project completion