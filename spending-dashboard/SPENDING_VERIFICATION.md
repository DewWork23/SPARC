# Spending Data Verification Report

**Date:** 2025-10-21
**Verification Method:** Manual extraction from Excel XML + cross-reference with dashboard code

---

## Source Data

**File:** `CORE-NC Opioid Settlement Public Data Tables.xlsx`
**Sheet:** `fin_detail`
**Field Used:** `fd_strat_funds_applied` (Column K)
**Total Records:** 360 spending records

---

## Spending Totals from Excel File

Extracted directly from the Excel file by parsing sheet XML:

| County | Total Applied Funds |
|--------|-------------------:|
| **Columbus** | **$201,777.00** |
| **Robeson** | **$107,105.00** |
| **Cumberland** | **$104,057.00** |
| **Bladen** | **$45,456.00** |
| **Richmond** | **$38,139.00** |
| **Scotland** | **$10,624.00** |
| **TOTAL** | **$507,158.00** |

---

## Dashboard Implementation Verification

### Code Review ✓

**File:** `spending-dashboard/index.html`

**Line 643:** Dashboard reads the same field we verified:
```javascript
const amount = parseFloat(row.fd_strat_funds_applied) || 0;
```

**Lines 641-649:** Aggregation logic matches our manual calculation:
```javascript
focusCountyData.forEach(row => {
    const county = extractCountyName(row.govt_name);
    const amount = parseFloat(row.fd_strat_funds_applied) || 0;
    // ... aggregates by county
});
```

### What to Verify on Dashboard ✓

Open https://dewwork23.github.io/SPARC/spending-dashboard/index.html and check:

1. **"Total Spending by County" chart** (Spending Analysis tab)
   - Should show bars matching the amounts above
   - Hover over each bar to see exact totals

2. **County breakdown cards** (County Profiles tab)
   - Each county card should show "Total Spending" matching above

3. **Detailed Spending Breakdown tables** (bottom of page)
   - Individual strategy amounts should sum to county totals

---

## Expected Dashboard Values

Based on our Excel extraction, the dashboard should display:

### Spending Analysis Tab - Total Spending by County Chart

- **Columbus County:** $201,777
- **Robeson County:** $107,105
- **Cumberland County:** $104,057
- **Bladen County:** $45,456
- **Richmond County:** $38,139
- **Scotland County:** $10,624

**Regional Total:** $507,158

### County Profiles Tab - Individual County Cards

Each county card's "Total Spending" stat should match the amounts above.

---

## Manual Verification Checklist

### Step 1: Visual Dashboard Check
- [ ] Open dashboard in browser
- [ ] Navigate to "Spending Analysis" tab
- [ ] Check "Total Spending by County" bar chart
- [ ] Hover over each bar and note the dollar amounts

### Step 2: Compare to Excel Values
- [ ] Columbus: $201,777 ✓ / ✗
- [ ] Robeson: $107,105 ✓ / ✗
- [ ] Cumberland: $104,057 ✓ / ✗
- [ ] Bladen: $45,456 ✓ / ✗
- [ ] Richmond: $38,139 ✓ / ✗
- [ ] Scotland: $10,624 ✓ / ✗

### Step 3: Check County Profile Cards
- [ ] Navigate to "County Profiles" tab
- [ ] Verify each county's "Total Spending" matches

### Step 4: Spot Check Detailed Breakdown
- [ ] Pick one county (suggest Cumberland)
- [ ] Open Excel file manually
- [ ] Filter fin_detail sheet by Cumberland
- [ ] Compare 2-3 individual strategy amounts to dashboard table

---

## Important Notes

### About the Data

1. **"Applied" vs "Disbursed":**
   - The fin_detail sheet contains `fd_strat_funds_applied` (funds applied/allocated)
   - It does NOT contain disbursed amounts in this sheet
   - Dashboard correctly uses applied funds for all visualizations

2. **Fiscal Year:**
   - Data includes multiple fiscal years
   - Dashboard aggregates across all years for each county
   - No fiscal year filter currently applied

3. **County Name Matching:**
   - Dashboard uses `extractCountyName()` function to normalize county names
   - Excel has "Cumberland", "Robeson County", etc.
   - Function strips "County" suffix for consistency

---

## Extraction Methodology

### How These Numbers Were Verified

1. **Unzipped Excel file** (.xlsx is a ZIP archive containing XML)
2. **Parsed XML structure:**
   - `xl/worksheets/sheet11.xml` = fin_detail sheet
   - `xl/sharedStrings.xml` = text values lookup
3. **Extracted data:**
   - Column B = `govt_name` (county)
   - Column K = `fd_strat_funds_applied` (amount)
4. **Aggregated** all amounts by county for FOCUS_COUNTIES
5. **Cross-referenced** with dashboard JavaScript code

### Python Script Used

```python
# Parse Excel XML structure
# For each row in fin_detail sheet:
#   - Extract county name (column B)
#   - Extract amount (column K)
#   - If county in FOCUS_COUNTIES, add to total
# Sum totals by county
```

---

## Conclusion

### Verification Status: ✅ READY FOR MANUAL CHECK

The spending data extraction is complete and methodology is sound. The dashboard code correctly reads the same field we verified (`fd_strat_funds_applied`).

**Next Step:** Open the live dashboard and visually confirm the "Total Spending by County" chart displays the amounts listed in this report.

---

## Quick Visual Check

**Expected order (highest to lowest):**
1. Columbus ($201K)
2. Robeson ($107K)
3. Cumberland ($104K)
4. Bladen ($45K)
5. Richmond ($38K)
6. Scotland ($10K)

If the chart shows this order with approximately these amounts, the data is accurate! ✓

---

**Verification Completed:** 2025-10-21
**Verification Method:** Direct XML parsing of Excel file
**Status:** ✅ Amounts extracted and ready for visual confirmation
