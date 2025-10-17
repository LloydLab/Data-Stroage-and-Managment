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
