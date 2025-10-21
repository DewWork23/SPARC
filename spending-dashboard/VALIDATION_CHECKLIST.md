# Dashboard Validation Checklist

**Purpose:** Ensure data accuracy and prevent misleading visualizations before deployment
**When to Use:** Before every dashboard update, data refresh, or new feature deployment
**Version:** 1.0
**Last Updated:** 2025-10-21

---

## Pre-Deployment Validation

### ✅ DATA ACCURACY

#### Spending Data
- [ ] Excel file version verified (check file date)
- [ ] County spending totals match source Excel file
- [ ] Regional total is sum of all county totals
- [ ] Fiscal year labels are correct
- [ ] No negative or zero values displayed (unless intentional)
- [ ] All numbers formatted consistently with commas
- [ ] Decimal places appropriate for context ($X.XX for small amounts, $X for large)

**Verification Method:**
```bash
# Extract and verify spending totals from Excel
python3 verify_spending_totals.py
```

#### Narrative Data
- [ ] People served numbers match source PDFs (with page references)
- [ ] Naloxone distribution numbers verified
- [ ] Treatment days verified
- [ ] Success rates verified
- [ ] All percentages sum to 100% (where applicable)
- [ ] Regional totals are sums of county values (where applicable)

**Verification Method:**
- Cross-reference county-narrative-data.json with source PDFs
- Check `_metadata` section for source citations

---

### ✅ COMPARABILITY CHECKS

#### Before Creating ANY Comparison Visualization:
- [ ] Are these metrics measured the same way across counties?
- [ ] Do counties use the same definitions?
- [ ] Are service models comparable?
- [ ] Is there survivorship bias in any metric?
- [ ] Would a lay person misinterpret this comparison?

#### Red Flags (DO NOT COMPARE):
- ❌ Cost per person across different service types
- ❌ "People served" without context about different definitions
- ❌ Success rates that exclude dropouts vs. those that include them
- ❌ Program outcomes from different service intensities
- ❌ Efficiency rankings based on incomparable metrics

#### Green Lights (OKAY TO COMPARE):
- ✅ Total spending (dollars are dollars)
- ✅ Naloxone kits distributed (if using same counting method)
- ✅ Treatment days provided (if same definition)
- ✅ Number of strategies funded
- ✅ Fiscal year comparisons for same county

---

### ✅ CONTEXT & DISCLAIMERS

#### Required Disclaimers:
- [ ] "People Served" has asterisk + disclaimer about different methodologies
- [ ] Success rates note survivorship bias where applicable
- [ ] Richmond's metrics labeled "program completers only"
- [ ] Scotland labeled as "Capacity Building Phase"
- [ ] Exhibit A/B usage correctly explained

#### Context Requirements:
- [ ] Every metric has a clear definition visible to users
- [ ] Every comparison explains what's being compared
- [ ] Every percentage shows what it's a percentage OF
- [ ] Every average shows sample size (n=X)
- [ ] Every trend shows time period

---

### ✅ EXHIBIT A/B STATUS

#### Verify County Status:
- [ ] Cumberland: 100% Exhibit A ✓
- [ ] Robeson: 100% Exhibit A (Option A participant) ✓
- [ ] Columbus: Primarily Exhibit B (Option A+B) ✓
- [ ] Richmond: 100% Exhibit A ✓
- [ ] Bladen: 100% Exhibit A (Option B plan submitted) ✓
- [ ] Scotland: 100% Exhibit A ✓

#### Check All Locations Showing Exhibit Status:
- [ ] County Profiles tab badges
- [ ] Detailed Spending Breakdown labels
- [ ] Overview tab explanation text
- [ ] No conflicting information across tabs

---

### ✅ TAB-BY-TAB REVIEW

#### Tab 1: Overview
- [ ] Regional metrics accurate
- [ ] County summary table has NO Cost/Person column
- [ ] "People Served" has disclaimer
- [ ] Spending totals match Spending Analysis tab
- [ ] Option A/B explanation is accurate

#### Tab 2: Spending Analysis
- [ ] Spending by County chart matches Excel totals
- [ ] Strategy Category breakdown totals correctly
- [ ] Detailed Spending Breakdown shows correct Exhibit letters
- [ ] All amounts formatted with commas
- [ ] Fiscal year labels present

#### Tab 3: Outcomes & Impact
- [ ] People Served displayed as context cards (NOT bar chart)
- [ ] Each card explains what the number represents
- [ ] Disclaimer about different methodologies present
- [ ] Naloxone chart accurate
- [ ] Treatment Outcomes section has disclaimers

#### Tab 4: Success Stories
- [ ] Stories match source PDFs
- [ ] No misleading claims
- [ ] County attribution correct

#### Tab 5: County Profiles
- [ ] Option A/B badges correct
- [ ] Planning status accurate (Robeson, Bladen)
- [ ] Top strategies match spending data
- [ ] County narratives accurate

---

### ✅ TECHNICAL VALIDATION

#### File Loading
- [ ] Excel file loads without errors
- [ ] county-narrative-data.json loads without errors
- [ ] No console errors in browser developer tools
- [ ] All charts render correctly
- [ ] Mobile responsive design works

#### Data Integrity
- [ ] No null/undefined values displayed as "NaN"
- [ ] No division by zero errors
- [ ] All tooltips show correct data
- [ ] All filters work correctly
- [ ] Tab navigation works

#### Performance
- [ ] Dashboard loads in < 3 seconds
- [ ] No lag when switching tabs
- [ ] Charts animate smoothly

---

### ✅ METADATA & DOCUMENTATION

#### county-narrative-data.json
- [ ] `_metadata` section present
- [ ] Source PDFs listed with dates
- [ ] Last updated date is current
- [ ] Data dictionary explains all metrics
- [ ] Comparability warnings present
- [ ] Source page numbers documented

#### Code Comments
- [ ] Complex calculations explained
- [ ] Data sources cited in code
- [ ] Any assumptions documented

---

### ✅ STAKEHOLDER REVIEW

#### Before Going Live:
- [ ] County representatives have reviewed their data
- [ ] SPARC leadership has approved
- [ ] No sensitive/confidential information exposed
- [ ] All claims can be backed up with source documents
- [ ] Legal/compliance review if required

---

## Post-Deployment Monitoring

### First 24 Hours:
- [ ] Check for user-reported issues
- [ ] Monitor for console errors
- [ ] Verify all links work
- [ ] Test on multiple browsers (Chrome, Firefox, Safari, Edge)
- [ ] Test on mobile devices

### First Week:
- [ ] Collect user feedback
- [ ] Address any confusion about metrics
- [ ] Document any questions asked repeatedly

---

## Issue Response Protocol

### If a Data Accuracy Issue is Reported:

1. **Immediate Actions:**
   - Do NOT dismiss the concern
   - Document the specific issue
   - Check the source data immediately
   - Verify with original PDFs/Excel files

2. **Investigation:**
   - Use this checklist to trace the data flow
   - Check if issue exists in multiple places
   - Determine if it's display issue or data issue

3. **Fix and Verify:**
   - Make the correction
   - Run full validation checklist again
   - Document what was wrong and how it was fixed
   - Update COMPREHENSIVE_AUDIT_REPORT.md

4. **Communication:**
   - Notify stakeholders of the issue and fix
   - Be transparent about what was wrong
   - Explain steps taken to prevent recurrence

---

## Common Pitfalls to Avoid

### Data Issues:
- ❌ Using old Excel file version
- ❌ Forgetting to update fiscal year labels
- ❌ Copy-pasting data between counties without updating
- ❌ Rounding errors that make percentages sum to 99% or 101%

### Presentation Issues:
- ❌ Comparing incomparable metrics
- ❌ Creating rankings without context
- ❌ Showing averages without sample sizes
- ❌ Displaying "100% success" without explaining methodology

### Technical Issues:
- ❌ Hard-coding values instead of calculating from data
- ❌ Not testing on all tabs
- ❌ Assuming fixes in one place fixed all places
- ❌ Skipping validation because "it's just a small change"

---

## Sign-Off

Before marking this checklist complete, the following people should review:

- [ ] **Data Analyst:** All numbers verified against sources
- [ ] **Dashboard Developer:** All technical validations pass
- [ ] **Project Lead:** Content and context appropriate
- [ ] **County Representative (optional):** County-specific data reviewed

**Validated By:** _______________
**Date:** _______________
**Dashboard Version:** _______________

---

## Update History

| Date | Validator | Issues Found | Status |
|------|-----------|--------------|--------|
| 2025-10-21 | Claude Code | 6 critical issues | ✅ All fixed |
|  |  |  |  |

---

**Remember:** It's better to delay deployment to fix an issue than to publish misleading information.
Trust is hard to earn and easy to lose.
