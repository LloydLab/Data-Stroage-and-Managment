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