# Data Management and Storage Plan for Llyod Lab

### Training Materials

#### 1-Hour Lab Meeting Training Agenda

**Agenda:**
1. **Why we need this** (10 min)
   - Current problems: running out of space, lost data, cannot find files
   - Benefits: save time, prevent data loss, meet funder requirements

2. **Directory structure tour** (15 min)
   - Walk through folder hierarchy
   - Show example project
   - Explain where each file type goes

3. **File naming demo** (10 min)
   - Show good vs. bad names
   - Practice with examples
   - Common mistakes to avoid

4. **Hands-on practice** (20 min)
   - Each person creates a test project
   - Save a test file with correct naming
   - Generate checksum
   - Update metadata.yaml

5. **Q&A and resources** (5 min)
   - Where to find templates
   - Who to ask for help (Data Steward)
   - Printed quick-reference cards

**Materials needed:**
- Printed quick-reference cards (one per person)
- Access to RDS for hands-on practice
- Example "good" project to show

#### Training Checklist (For each lab member)

**New Lab Member Onboarding:**
- [ ] Attend 1-hour training session
- [ ] Read complete data management plan
- [ ] Create a test project (supervised)
- [ ] Save test data with correct naming
- [ ] Update metadata file
- [ ] Generate checksums
- [ ] Demonstrate understanding to Data Steward

**Sign-off:**
- Lab member: _________________ Date: _______
- Data Steward: _______________ Date: _______

---

---
## 📞 GETTING HELP

### Data Steward Responsibilities
- Answer "where does this go?" questions
- Weekly compliance checks
- Monthly storage audits
- Backup verification
- Training new members

### When to Ask Data Steward
- ❓ Unsure where to save a file
- ❓ Need to create unusual project structure
- ❓ Storage getting full
- ❓ Backup questions or issues
- ❓ Need help finding old data

### Escalate to PI When
- 🚨 Storage >90% full despite cleanup
- 🚨 Backup failure
- 🚨 Data loss incident
- 🚨 Repeated compliance violations
- 🚨 Need additional budget for storage

---

## 📚 APPENDIX: QUICK REFERENCE

### Directory Structure (1-page poster)
[Print and post in lab]

### File Naming Examples (1-page card)
[Keep at each computer]

### Monthly Checklist (1-page card)
[Post on Data Steward's desk]

### Emergency Contacts
- Data Steward: [email]
- PI: [email]
- IT Support: [phone/email]
- Backup Service: [support contact]

---

**Document Version:** 3.0  
**Last Updated:** 2025-11-12  
**Next Review:** 2026-01-12

**Document Owner:** Data Steward  
**Approved By:** PI

---

*This plan is a living document. Please provide feedback and suggestions for improvement to the Data Steward.*

---

## Publishing the instructions website

This repository is configured to publish the Markdown files under `instructions/` as a website using MkDocs.

How to enable GitHub Pages the first time:

1. Push your changes to the `main` branch on GitHub.
2. In your GitHub repository, go to Settings → Pages.
3. Under "Build and deployment", set Source to "GitHub Actions". Save.
4. A workflow named "Deploy MkDocs site to GitHub Pages" will run on each push to `main`.
5. When it finishes, your site will be available at `https://<your-org-or-user>.github.io/<repo-name>/`.

Local preview (optional):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Then open the local link shown (usually `http://127.0.0.1:8000`).
