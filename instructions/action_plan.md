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

## GOALS

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
