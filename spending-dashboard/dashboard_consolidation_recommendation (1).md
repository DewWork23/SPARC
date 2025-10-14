# Dashboard Consolidation Recommendation

## Executive Summary

**RECOMMENDATION: Create ONE Integrated Dashboard with Multiple Tabs/Views**

The current SPARC dashboard and the narrative reports contain **complementary data** that tells a complete story when combined. The spending data shows the "what" and "how much," while the narratives show the "why" and "impact."

---

## Current State Analysis

### SPARC Dashboard (Existing)
**Data Source:** CORE-NC_Opioid_Settlement_Public_Data_Tables.xlsx

**What it shows:**
- ✅ Total spending by county (accurate financial data)
- ✅ Spending by strategy category breakdown
- ✅ Detailed line-item expenditures
- ✅ Fiscal year tracking (FY 2022-2023 and FY 2023-2024)
- ✅ Multi-year trend capability

**Key Findings from Data:**
| County | Total Spending | # Strategies | Rank |
|--------|---------------|--------------|------|
| Robeson | $614,748 | 10 | 1st |
| Columbus | $467,382 | 18 | 2nd |
| Richmond | $269,740 | 4 | 3rd |
| Cumberland | $256,734 | 9 | 4th |
| Bladen | $161,062 | 4 | 5th |
| Scotland | $3,756 | 1 | 6th |
| **TOTAL** | **$1,773,422** | **46 strategies** | |

**What it's MISSING:**
- ❌ Real-world outcomes (people served, lives saved)
- ❌ Success stories and qualitative impact
- ❌ Program implementation details
- ❌ Partnership information
- ❌ Context for WHY money was spent

### Narrative Reports (6 PDFs)
**Data Source:** County narrative PDFs for FY 2023-2024

**What they show:**
- ✅ Individuals served (2,168+ across all counties)
- ✅ Naloxone distribution (2,312+ kits)
- ✅ Treatment outcomes (days in treatment, employment rates)
- ✅ Success stories with real impact
- ✅ Partnership networks
- ✅ Program descriptions and implementation status
- ✅ Innovative approaches

**Key Findings from Narratives:**
| County | People Served | Naloxone Kits | Notable Programs |
|--------|---------------|---------------|------------------|
| Cumberland | 981 | 1,492 | LEAD, Detention Center MAT |
| Columbus | 86 | - | Healing Place, FirstWatch DB |
| Robeson | 184+ | 500+ | Breeches Buoy Hospital Program |
| Richmond | 30 | 320 | Samaritan Colony |
| Bladen | 8 | - | Healing Place |
| Scotland | TBD | TBD | Opioid Collaborative |

**What it's MISSING:**
- ❌ Precise spending amounts
- ❌ Multi-year financial trends
- ❌ Strategy-level cost breakdowns

---

## Why These Should Be CONSOLIDATED

### 1. **They Tell Different Parts of the Same Story**

**Current Dashboard Shows:** Robeson spent $274,699 on "Recovery Support Services"  
**Narratives Add Context:** This funded jail-based care coordination that identified 250+ detainees with OUD, provided 70+ treatment referrals, and included peer support specialists

**Current Dashboard Shows:** Cumberland spent $83,711 on "Recovery Support Services"  
**Narratives Add Context:** This served 981 individuals, made 2,840 contacts, referred 232 to treatment, distributed 1,555 naloxone kits

### 2. **They Answer Different Stakeholder Questions**

| Stakeholder | Needs From Dashboard | Needs From Narratives |
|-------------|---------------------|----------------------|
| **County Commissioners** | Budget accountability | Program effectiveness |
| **Funders/Grantmakers** | Spending patterns | Outcome metrics |
| **Community Members** | Where money goes | Real-world impact |
| **Program Staff** | Resource allocation | Best practices |
| **Researchers** | Comparative spending | Implementation models |

### 3. **Data Reconciliation Opportunities**

**CRITICAL ISSUE DISCOVERED:**  
The current dashboard shows Cumberland at $256,734 total spending, but the narratives indicate they invested "over $300,000" in recovery support services. This suggests:
- Dashboard may be showing only certain fiscal years or funding streams
- Narratives may include non-settlement funds
- Different reporting periods

**A consolidated dashboard can:**
- Clarify these discrepancies
- Show breakdown by funding source
- Link spending to specific outcomes

### 4. **Enhanced User Experience**

Instead of users toggling between two separate dashboards, one integrated platform provides:
- **Context switching eliminated** - see spending AND impact in one place
- **Cross-referencing enabled** - click on a spending line to see outcomes
- **Comprehensive analysis** - answer "Was it worth it?" questions

---

## Recommended Dashboard Structure

### **Single Integrated Platform with 5 Major Sections:**

```
┌─────────────────────────────────────────────────────────┐
│  SOUTHEASTERN NC OPIOID RESPONSE DASHBOARD              │
│  Robeson • Cumberland • Scotland • Richmond • Bladen • Columbus │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  📊 OVERVIEW   💰 SPENDING   📈 OUTCOMES   🏆 SUCCESS   ℹ️ ABOUT │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### **Tab 1: OVERVIEW (Landing Page)**
- Regional map with county selection
- Key metrics dashboard:
  - Total investment: $1.77M
  - Total people served: 2,168+
  - Naloxone kits distributed: 2,312+
  - Lives saved: [derived from reversal data]
- Quick comparison table
- Recent highlights/news

### **Tab 2: SPENDING ANALYSIS** *(from SPARC data)*
- Total spending by county (bar chart - already built)
- Spending by strategy category (pie chart - already built)
- **NEW:** Spending over time (line chart showing FY 2022-23 vs 2023-24)
- **NEW:** Cost per person served (calculated metric)
- Detailed spending breakdown table
- Export capabilities

### **Tab 3: OUTCOMES & IMPACT** *(from narratives)*
- People served by county and program type
- Treatment outcomes:
  - Days in treatment
  - Employment placements
  - Housing secured
  - MAT initiations
- Harm reduction metrics:
  - Naloxone distribution
  - Overdose reversals
  - ED visit reductions
- Interactive filters by:
  - County
  - Strategy type
  - Population served
  - Time period

### **Tab 4: SUCCESS STORIES** *(from narratives)*
- Gallery view of anonymized success stories
- Filter/search by:
  - County
  - Strategy
  - Population (justice-involved, pregnant women, youth)
  - Outcome type
- Featured spotlight stories
- Downloadable case study PDFs

### **Tab 5: COUNTY DEEP DIVES**
Each county gets a comprehensive profile combining BOTH data sources:

```
╔════════════════════════════════════════════════╗
║           ROBESON COUNTY PROFILE               ║
╠════════════════════════════════════════════════╣
║ INVESTMENT                                     ║
║ • Total: $614,748 (Highest in region)         ║
║ • Strategies Funded: 10                        ║
║ • Top Investment: Recovery Support ($275K)    ║
║                                                ║
║ IMPACT                                         ║
║ • People Served: 184+                         ║
║ • Naloxone Distributed: 500+ kits             ║
║ • Overdose Reduction: 65 → 48 ED visits       ║
║                                                ║
║ INNOVATIONS                                    ║
║ • Breeches Buoy Hospital Program              ║
║ • RRCOR Consortium Partnership                ║
║                                                ║
║ OUTCOMES                                       ║
║ • 72 inpatient placements                     ║
║ • 112 outpatient connections                  ║
║ • 30+ declined patients returned for help     ║
╚════════════════════════════════════════════════╝
```

---

## Implementation Strategy

### Phase 1: Enhance Current Dashboard (Week 1-2)
- Keep existing SPARC spending visualizations
- Add "Outcomes" and "Success Stories" tabs
- Integrate narrative data
- Create county profile pages

### Phase 2: Connect the Data (Week 3-4)
- Link spending line items to outcome metrics
- Calculate ROI metrics (cost per person served, cost per kit distributed)
- Add interactive filters
- Build cross-referencing capabilities

### Phase 3: Polish & Deploy (Week 5-6)
- User testing with stakeholders
- Mobile responsiveness
- Export/print functionality
- Accessibility compliance

---

## Data Integration Plan

### New Data Points to Add from Narratives:

**Performance Metrics:**
```json
{
  "county": "Cumberland",
  "fy": "2023-2024",
  "spending": {
    "total": 256734,
    "recovery_support": 83711
  },
  "outcomes": {
    "individuals_served": 981,
    "total_contacts": 2840,
    "treatment_referrals": 232,
    "recovery_connections": 506,
    "harm_reduction_referrals": 833,
    "naloxone_kits": 1555,
    "peer_specialists": 10,
    "employment_served": 175
  },
  "programs": [
    "LEAD Program",
    "Detention Center MAT",
    "Naloxone Vending Machine"
  ]
}
```

**Success Indicators:**
```json
{
  "columbus": {
    "overdose_calls_change": -0.11,
    "naloxone_admin_change": -0.10,
    "ed_visits_change": -0.39,
    "students_trained": 575,
    "teachers_trained": 14
  }
}
```

### Reconciliation Needed:

**Strategy Name Mapping:**
- SPARC uses: "Research on improved service delivery for modalities such as SBIRT..."
- Narratives use: "Recovery Support Services (Strategy 3)"
- **Solution:** Create mapping table between verbose strategy names and short names

**Exhibit Options:**
- SPARC shows "Option A" for all counties
- Narratives show Columbus using Exhibit B strategies
- **Solution:** Add clarification that counties started with A, some expanded to B

---

## User Stories for Consolidated Dashboard

### For County Commissioners:
> "As a commissioner, I want to see how much we spent AND what we achieved, so I can justify continued investment to taxpayers."

**Consolidated dashboard provides:** Side-by-side spending and outcomes, cost-effectiveness metrics

### For Community Members:
> "As a resident, I want to know if these programs are actually helping people in my community."

**Consolidated dashboard provides:** Success stories, local impact metrics, real testimonials

### For Program Directors:
> "As a program director in Scotland County, I want to see what worked in similar counties so I can model our programs."

**Consolidated dashboard provides:** Comparative analysis, best practices, innovation showcase

### For Researchers/Evaluators:
> "As a researcher, I want to analyze the relationship between investment levels and outcomes."

**Consolidated dashboard provides:** Exportable data, correlation analysis, multi-year trends

---

## Why NOT to Keep Them Separate

### Arguments Against Separate Dashboards:

❌ **User Confusion:** "Which dashboard do I use?"  
❌ **Incomplete Picture:** Financial accountability without impact data is half the story  
❌ **Duplication:** Both need county selectors, time filters, basic navigation  
❌ **Maintenance Burden:** Updates required in two places  
❌ **Lost Insights:** Can't easily see spending → outcome relationships  
❌ **Stakeholder Frustration:** Have to switch between tools mid-analysis

### Only Reason to Keep Separate:
If you have **different audiences with completely different needs** who would be confused by integrated data.

**But that's not the case here** - all stakeholders care about BOTH spending accountability AND program impact.

---

## Visual Mock-Up of Integrated View

### County Card Example (Combines Both Sources):

```
┌─────────────────────────────────────────────┐
│  CUMBERLAND COUNTY         [Option A → B]   │
├─────────────────────────────────────────────┤
│                                             │
│  💰 INVESTMENT                              │
│  $256,734    7 strategies funded            │
│  ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯      │
│  Top: Recovery Support.......$83.7K         │
│       Housing Support........$82.9K         │
│       Reentry Programs.......$23.9K         │
│                                             │
│  📈 IMPACT                                  │
│  981 people served                          │
│  1,492 naloxone kits distributed            │
│  232 treatment referrals                    │
│  175 employment connections                 │
│                                             │
│  🏆 INNOVATIONS                             │
│  • LEAD Program (88 enrolled)              │
│  • Naloxone vending machine                 │
│  • Detention Center MAT (76 served)         │
│                                             │
│  [View Full Profile →]                      │
└─────────────────────────────────────────────┘
```

---

## Technical Specifications

### Data Sources:
1. **CORE-NC Excel File** (financial data)
   - `fin_detail` sheet for spending
   - `impact_summary` sheet for narrative links
   - `strategies` sheet for strategy definitions

2. **6 County PDF Narratives** (impact data)
   - Extract metrics using Python (pdfplumber)
   - Parse success stories
   - Identify partnerships

### Data Processing Pipeline:
```
Excel Data → Parse → Clean → Normalize
                                ↓
PDF Narratives → Extract → Structure → Match Strategy IDs
                                       ↓
                              Merged Dataset
                                       ↓
                              Dashboard Components
```

### Technology Stack:
- React (already in use)
- D3.js or Recharts for visualizations
- Tabs/routing for multi-section interface
- PDF.js for inline PDF viewing
- Export to Excel/PDF functionality

---

## Metrics to Showcase Integration Value

### New Calculated Metrics Only Possible with Both Sources:

1. **Cost per Person Served**
   - Robeson: $614,748 ÷ 184 = $3,341 per person
   - Cumberland: $256,734 ÷ 981 = $262 per person
   - *Shows Cumberland's efficiency*

2. **Cost per Naloxone Kit Distributed**
   - Cumberland: $256,734 ÷ 1,492 = $172 per kit
   - Richmond: $269,740 ÷ 320 = $843 per kit
   - *Includes program overhead, not just kit cost*

3. **Investment vs. Lives Saved**
   - Track overdose reversals
   - Calculate societal cost averted

4. **ROI on Specific Strategies**
   - Healing Place partnership cost vs. days of treatment provided
   - Employment services cost vs. jobs secured

---

## Recommendation Summary

### ✅ **CONSOLIDATE into One Dashboard Because:**

1. **Complete Story:** Financial + impact data together
2. **Better User Experience:** One-stop shop for all stakeholders
3. **Enhanced Analytics:** Calculate ROI and effectiveness metrics
4. **Reduced Confusion:** Clear, integrated narrative
5. **Easier Maintenance:** Single codebase to update
6. **Cross-County Learning:** See what works and what it costs
7. **Accountability:** Show taxpayers both spending AND results

### 📋 **Implementation Checklist:**

- [ ] Preserve existing SPARC visualizations (they're good!)
- [ ] Add 3 new tabs: Outcomes, Success Stories, County Profiles
- [ ] Extract metrics from 6 PDF narratives
- [ ] Create strategy ID mapping between data sources
- [ ] Build calculated metrics (cost per person, etc.)
- [ ] Add filters and interactive elements
- [ ] Test with actual stakeholders
- [ ] Deploy and train users

### 🎯 **Success Criteria:**

A successful integrated dashboard will allow users to:
1. Click on a spending bar and see what outcomes it produced
2. Read a success story and see what it cost
3. Compare counties on both investment and impact
4. Export comprehensive reports combining both data types
5. Answer "Was it worth it?" questions with confidence

---

## Next Steps

1. **Approve consolidation approach** ✓
2. **Share with Claude Code** to build integrated dashboard
3. **Extract narrative data** from PDFs into structured format
4. **Map strategy IDs** between SPARC data and narratives
5. **Build county profile pages** combining both sources
6. **Add calculated metrics** and visualizations
7. **User testing** with commissioners, staff, community members
8. **Launch** integrated dashboard

---

**Bottom Line:** The current spending dashboard is excellent, but it's only showing half the picture. By integrating the narrative impact data, you create a powerful accountability and learning tool that shows both WHERE the money went AND WHAT it accomplished. This is the dashboard your region needs to demonstrate value and guide future investment decisions.

---
---

# APPENDIX: COMPLETE COUNTY DATA PROFILES

## Overview: All Six Counties at a Glance

| County | Total Spending | Rank | Strategies | People Served | Naloxone Kits | Key Programs |
|--------|---------------|------|------------|---------------|---------------|--------------|
| **Robeson** | $614,748 | 1st | 7 unique | 184+ | 500+ | Breeches Buoy, RRCOR |
| **Columbus** | $467,382 | 2nd | 12 unique | 86 | - | Healing Place, FirstWatch |
| **Richmond** | $269,740 | 3rd | 3 unique | 30 | 320 | Samaritan Colony, DEFT |
| **Cumberland** | $256,734 | 4th | 8 unique | 981 | 1,492 | LEAD, Detention MAT |
| **Bladen** | $161,062 | 5th | 2 unique | 8 | - | Healing Place |
| **Scotland** | $3,756 | 6th | 1 unique | TBD | TBD | Opioid Collaborative |
| **TOTAL** | **$1,773,422** | - | **46 lines** | **2,168+** | **2,312+** | - |

---

## BLADEN COUNTY

### Financial Summary (from CORE-NC data)
- **Total Spending:** $161,061.87
- **Funding Lines:** 4
- **Unique Strategies:** 2
- **Exhibit Option:** A
- **Fiscal Year Range:** FY 2022-2023 to FY 2023-2024

### Spending by Fiscal Year
| Fiscal Year | Amount | % of Total |
|-------------|--------|------------|
| FY 2022-2023 | $69,786.41 | 43.3% |
| FY 2023-2024 | $91,275.46 | 56.7% |

### Spending by Strategy
| Strategy | Total Spent | % of County Budget |
|----------|-------------|-------------------|
| Collaborative Strategic Planning | $91,497.87 | 56.8% |
| Recovery Support Services | $69,564.00 | 43.2% |

### Detailed Line Items
1. **[FY 2022-2023]** Collaborative Strategic Planning: $62,328.41
2. **[FY 2023-2024]** Recovery Support Services: $62,106.00
3. **[FY 2023-2024]** Collaborative Strategic Planning: $29,169.46
4. **[FY 2022-2023]** Recovery Support Services: $7,458.00

### Impact Metrics (from Narrative Reports)
**People Served:** 8 individuals referred to Healing Place
- 4 identified opioids as primary drug of choice
- Total days served: 1,007
- Average length of stay: 125.87 days
- Range: 6-259 days in residence

**Key Outcomes:**
- 100% of individuals connected to employment services
- 100% obtained employment
- 100% connected to and adhered to treatment
- 100% transferred to after-care housing

**Programs Funded:**
1. **Strategic Planning Update** - Updated strategic plan from FY2025-2027, expanded to Option B strategies
2. **Healing Place Partnership** - Contract with Healing Place of New Hanover County for 24/7 detox, short/long-term treatment
3. **MAT Services** - Vivitrol injections provided through Trillium Health Resources grant

**Success Story Highlight:**
32-year-old woman using fentanyl stayed 219 continuous days at Healing Place without relapsing. Received naltrexone for 3.5 months and remained in recovery.

**Cost Effectiveness:**
- Cost per person served: $161,062 ÷ 8 = **$20,133 per person**
- Cost per treatment day: $161,062 ÷ 1,007 = **$160 per day**

---

## COLUMBUS COUNTY

### Financial Summary (from CORE-NC data)
- **Total Spending:** $467,382.17
- **Funding Lines:** 18
- **Unique Strategies:** 12 (Most diverse portfolio)
- **Exhibit Option:** B (Expanded strategies)
- **Fiscal Year Range:** FY 2022-2023 to FY 2023-2024

### Spending by Fiscal Year
| Fiscal Year | Amount | % of Total |
|-------------|--------|------------|
| FY 2022-2023 | $113,727.70 | 24.3% |
| FY 2023-2024 | $353,654.47 | 75.7% |

### Spending by Strategy
| Strategy | Total Spent | % of County Budget |
|----------|-------------|-------------------|
| Provide full continuum of care for OUD | $140,184.00 | 30.0% |
| Support centralized call centers | $102,724.14 | 22.0% |
| Staff government oversight | $66,132.80 | 14.2% |
| Data tracking software | $33,818.47 | 7.2% |
| School prevention programs | $30,021.84 | 6.4% |
| Regional planning | $28,482.50 | 6.1% |
| Prescriber training | $20,038.65 | 4.3% |
| Collaborative Strategic Planning | $15,000.00 | 3.2% |
| Training for NAS compliance | $14,476.40 | 3.1% |
| Criminal justice training | $9,108.17 | 1.9% |
| Media campaigns | $6,000.00 | 1.3% |
| Transportation support | $1,395.20 | 0.3% |

### Detailed Line Items (Top 10)
1. **[FY 2023-2024]** Full continuum of care: $107,646.00
2. **[FY 2023-2024]** Centralized call centers: $76,604.00
3. **[FY 2023-2024]** Government oversight staffing: $43,723.77
4. **[FY 2023-2024]** Data tracking software: $33,818.47
5. **[FY 2022-2023]** Full continuum of care: $32,538.00
6. **[FY 2022-2023]** Centralized call centers: $26,120.14
7. **[FY 2023-2024]** Regional planning: $24,320.00
8. **[FY 2022-2023]** Government oversight staffing: $22,409.03
9. **[FY 2022-2023]** School prevention programs: $21,211.50
10. **[FY 2023-2024]** Prescriber training: $20,038.65

### Impact Metrics (from Narrative Reports)
**People Served:**
- 86 residents admitted to Healing Place (1,631 treatment days)
- 57 men, 29 women
- 51% using opioids, 20% crack/cocaine, 17% alcohol, 10% meth, 3% opioids/benzos

**Key Outcomes:**
- **11% drop** in EMS overdose calls (SFY23 to SFY24)
- **10% decrease** in naloxone administration by EMS
- **39% drop** in ED visits for overdoses
- **8 deaths** in SFY23 reduced to **3 deaths** in SFY24
- 61% of overdose calls due to fentanyl

**Programs Funded:**
1. **Healing Place Partnership** - 10-12 beds/day contracted
2. **24/7 Crisis Phone Line** - Licensed MHP available
3. **OUD Resource Coordinator** - Took 97 calls in SFY24
4. **FirstWatch Database** - EMS tracking system across 5 departments
5. **Botkin LifeSkills Training** - 575 students, 14 teachers trained
6. **Dr. Chasnoff NAS Training** - 59 participants, 100% learned new info
7. **Prescriber Training Series** - 9 sessions planned, 5 completed
8. **Adult Drug Court Development** - 2 judges attended national conference
9. **Opioid Steering Committee** - Monthly meetings, ROSC model
10. **Grants Manager Position** - Full-time oversight

**Success Story Highlights:**
- Physician quote: "Great day, learned a lot. Dr. Chasnoff took a complicated subject and was able to make it meaningful"
- 100% of prescriber training participants learned new information
- Columbus Regional Healthcare considering 4th floor conversion to MH/SUD/OUD unit

**Cost Effectiveness:**
- Cost per person served: $467,382 ÷ 86 = **$5,435 per person**
- Cost per treatment day: $467,382 ÷ 1,631 = **$287 per day**

---

## CUMBERLAND COUNTY

### Financial Summary (from CORE-NC data)
- **Total Spending:** $256,734.26
- **Funding Lines:** 9
- **Unique Strategies:** 8
- **Exhibit Option:** A
- **Fiscal Year Range:** FY 2022-2023 to FY 2023-2024

### Spending by Fiscal Year
| Fiscal Year | Amount | % of Total |
|-------------|--------|------------|
| FY 2022-2023 | $23,032.48 | 9.0% |
| FY 2023-2024 | $233,701.78 | 91.0% |

### Spending by Strategy
| Strategy | Total Spent | % of County Budget |
|----------|-------------|-------------------|
| Recovery Support Services | $83,711.08 | 32.6% |
| Recovery Housing Support | $82,882.04 | 32.3% |
| Naloxone Distribution | $30,036.00 | 11.7% |
| Reentry Programs | $23,882.94 | 9.3% |
| Criminal Justice Diversion Programs | $12,478.63 | 4.9% |
| Employment-related Services | $11,404.19 | 4.4% |
| Addiction Treatment for Incarcerated | $7,546.90 | 2.9% |
| Syringe Services Program | $4,792.48 | 1.9% |

### Detailed Line Items
1. **[FY 2023-2024]** Recovery Support Services: $83,711.08
2. **[FY 2023-2024]** Recovery Housing Support: $82,882.04
3. **[FY 2023-2024]** Reentry Programs: $23,882.94
4. **[FY 2022-2023]** Naloxone Distribution: $18,240.00
5. **[FY 2023-2024]** Criminal Justice Diversion: $12,478.63
6. **[FY 2023-2024]** Naloxone Distribution: $11,796.00
7. **[FY 2023-2024]** Employment Services: $11,404.19
8. **[FY 2023-2024]** Addiction Treatment (Incarcerated): $7,546.90
9. **[FY 2022-2023]** Syringe Services: $4,792.48

### Impact Metrics (from Narrative Reports)
**People Served:**
- **981 individuals** through recovery support services
- **88 individuals** enrolled in pre-arrest diversion
- **76 individuals** in detention center MAT program
- **838 individuals** in reentry program
- **49 individuals** assisted with recovery housing

**Key Outcomes:**
- 2,840 total contacts made
- 232 participants referred to addiction treatment
- 506 participants connected to recovery supports
- 833 participants referred to harm reduction services
- 57 participants accessed primary healthcare
- 904 participants referred to other services
- 10 Peer Support Specialists engaged
- 1,555 naloxone kits distributed (training: 812 sessions, reached 749 individuals)
- 17 diversion placements into treatment programs
- 267 initial assessments for reentry
- 8,010 case management meetings conducted
- 175 served through employment services (12 job readiness workshops, 56 transportation requests)
- 40 unique individuals assisted with rent

**Programs Funded:**
1. **C-FORT (Cumberland-Fayetteville Opioid Response Team)** - Multi-agency collaboration
2. **LEAD Program** - Law Enforcement Assisted Diversion via NC Harm Reduction Coalition
3. **Detention Center MOUD** - Medication for Opioid Use Disorder program with LCSW and PSS
4. **Naloxone Vending Machine** - Installed at detention center
5. **Recovery Housing Network** - Comprehensive support with mental health, counseling, job training
6. **Multiple Treatment Providers** - Carolina Treatment Center, Goshen Medical Services, Myrover-Reese Fellowship Homes

**Success Story Highlights:**
- **Joey's Story:** 40-year-old homeless man in tent → LEAD Program → warrant resolved → transitional housing → full-time employment → independent housing
- **Case #7298:** Domestic violence survivor → hotel living → CTC support groups → budget training → affordable home → new job → maintains housing and sobriety
- **Case #2168:** PTSD sufferer → grant-funded housing deposit → safe environment → active in treatment
- **Case #6817:** Domestic violence and SUD survivor → recovery journey → became Peer Support Specialist → now helping others
- **Joseph's Story:** 30s, 7+ years on MAT → Myrover-Reese Fellowship → detox → 12-step program → employment → head of household → still volunteers weekly

**Cost Effectiveness:**
- Cost per person served (recovery support): $256,734 ÷ 981 = **$262 per person** (Most efficient!)
- Cost per naloxone kit: $256,734 ÷ 1,492 = **$172 per kit** (includes overhead)

**Note:** Cumberland County's actual investment mentioned in narratives is "over $300,000" which suggests additional funding streams beyond what's captured in the CORE-NC database. This discrepancy should be clarified in the dashboard.

---

## RICHMOND COUNTY

### Financial Summary (from CORE-NC data)
- **Total Spending:** $269,739.65
- **Funding Lines:** 4
- **Unique Strategies:** 3
- **Exhibit Option:** A
- **Fiscal Year Range:** FY 2022-2023 to FY 2023-2024

### Spending by Fiscal Year
| Fiscal Year | Amount | % of Total |
|-------------|--------|------------|
| FY 2022-2023 | $8,892.77 | 3.3% |
| FY 2023-2024 | $260,846.88 | 96.7% |

### Spending by Strategy
| Strategy | Total Spent | % of County Budget |
|----------|-------------|-------------------|
| Recovery Support Services | $150,000.00 | 55.6% |
| Collaborative Strategic Planning | $82,839.65 | 30.7% |
| Naloxone Distribution | $36,900.00 | 13.7% |

### Detailed Line Items
1. **[FY 2023-2024]** Recovery Support Services: $150,000.00
2. **[FY 2023-2024]** Collaborative Strategic Planning: $73,946.88
3. **[FY 2023-2024]** Naloxone Distribution: $36,900.00
4. **[FY 2022-2023]** Collaborative Strategic Planning: $8,892.77

### Impact Metrics (from Narrative Reports)
**People Served:**
- 30 Richmond County men through Samaritan Colony

**Key Outcomes:**
- 100% of men completed 28-day inpatient program
- 100% connected to employment services and obtained employment
- 100% connected to and adhered to treatment
- 100% transferred to after-care housing or returned to safe house
- 320 naloxone kits distributed throughout county

**Programs Funded:**
1. **DEFT (Drug Endangered Family Task Force)** - Completed strategic plan, maintains online database and website, monthly meetings
2. **Samaritan Colony Partnership** - Residential treatment facility in Aberdeen, NC
3. **Naloxone Distribution** - Via peer support specialists to first responders, schools, and individuals
4. **Part-time DEFT Coordinator** - Program operations and RFA process management

**Success Story Highlight:**
Young African American male from Rockingham diagnosed with OUD → screened and accepted → transitional house → Samaritan Colony (28 days intensive) → Aberdeen recovery home → 12-step program → employed by previous Samaritan client's company → continues spiritual, mental, and physical growth → leads by example for others

**Additional Success:**
22-year-old male relapsed → received naloxone through settlement funds → naloxone saved his life → re-entered treatment → doing well today

**Cost Effectiveness:**
- Cost per person served: $269,740 ÷ 30 = **$8,991 per person**
- Cost per naloxone kit: $269,740 ÷ 320 = **$843 per kit** (includes full program overhead)

---

## ROBESON COUNTY

### Financial Summary (from CORE-NC data)
- **Total Spending:** $614,748.22 (Highest in region)
- **Funding Lines:** 10
- **Unique Strategies:** 7
- **Exhibit Option:** A
- **Fiscal Year Range:** FY 2022-2023 to FY 2023-2024

### Spending by Fiscal Year
| Fiscal Year | Amount | % of Total |
|-------------|--------|------------|
| FY 2022-2023 | $195,347.98 | 31.8% |
| FY 2023-2024 | $419,400.24 | 68.2% |

### Spending by Strategy
| Strategy | Total Spent | % of County Budget |
|----------|-------------|-------------------|
| Recovery Support Services | $321,601.79 | 52.3% |
| Evidence-Based Addiction Treatment | $125,000.00 | 20.3% |
| Employment-related Services | $103,535.97 | 16.8% |
| Post-Overdose Response Team | $37,712.57 | 6.1% |
| Naloxone Distribution | $12,540.00 | 2.0% |
| Early Intervention | $11,428.00 | 1.9% |
| Collaborative Strategic Planning | $2,929.89 | 0.5% |

### Detailed Line Items
1. **[FY 2023-2024]** Recovery Support Services: $274,698.66
2. **[FY 2023-2024]** Evidence-Based Addiction Treatment: $125,000.00
3. **[FY 2022-2023]** Employment-related Services: $86,440.00
4. **[FY 2022-2023]** Recovery Support Services: $46,903.13
5. **[FY 2022-2023]** Post-Overdose Response Team: $35,106.96
6. **[FY 2023-2024]** Employment-related Services: $17,095.97
7. **[FY 2022-2023]** Naloxone Distribution: $12,540.00
8. **[FY 2022-2023]** Early Intervention: $11,428.00
9. **[FY 2022-2023]** Collaborative Strategic Planning: $2,929.89
10. **[FY 2023-2024]** Post-Overdose Response Team: $2,605.61

### Impact Metrics (from Narrative Reports)
**People Served:**
- 72 individuals accessed inpatient residential treatment for OUD
- 112 individuals accessed outpatient treatment for OUD
- 72 individuals received MAT services
- 250+ detainees with OUD identified in jail
- 128 individuals transported to employment/treatment via SEATS

**Key Outcomes:**
- **Overdose ED visits dropped from 65 to 48** (26% reduction)
- 30+ patients who initially declined services later called back for help
- 70+ referrals for inpatient and outpatient treatment (jail health team)
- 500+ naloxone kits distributed to community organizations and first responders
- 100% of Breeches Buoy patients given naloxone prescription

**Programs Funded:**
1. **Breeches Buoy Addiction Medicine Service** - Hospital-based inpatient addiction medicine at UNC Health Southeastern
2. **Jail Health Care Navigation** - Licensed Clinical Addiction Specialist, Recovery Coach, peer support specialists
3. **SEATS Transportation** - Employment and treatment center transport
4. **Post-Overdose Response Team (PORT)** - Early planning phase, high turnover challenges
5. **RRCOR Consortium Partnership** - Robeson Rural Communities Opioid Response
6. **SPARC Collaboration** - Southeastern Prevention & Addiction Recovery Center for strategic planning

**Success Story Highlights:**
- **Hospital Patient Testimonial:** "I began seeing Breeches Buoy when I went to the ER for my OUD. At first, I didn't think I needed inpatient treatment... They assisted with buprenorphine induction and outpatient treatment... I learned my disease was too far progressed... They found me long-term inpatient treatment where I could also continue MAT... I have been in a 12-month program now for over 6 months. I am healthy, happy, thriving, and most importantly clean... I finally look forward to the future and see that I am more than an addict."
- **Jail to Recovery:** One individual enrolled in Recovery Care Coordination while incarcerated → referred to adult treatment court → enrolled in residential treatment (Charlotte) → returned home → assigned peer support specialist → local residential facility → Oxford House → ankle monitor removed for compliance → full-time employment → maintains recovery

**Cost Effectiveness:**
- Cost per person served (treatment): $614,748 ÷ 184 = **$3,341 per person**
- Cost per naloxone kit: $614,748 ÷ 500 = **$1,229 per kit** (includes full PORT infrastructure)

**Note:** Robeson County narratives mention "over $300,000 investment" in recovery support services, which aligns with the $321,602 shown in CORE-NC data for Recovery Support Services specifically.

---

## SCOTLAND COUNTY

### Financial Summary (from CORE-NC data)
- **Total Spending:** $3,756.14 (Lowest in region)
- **Funding Lines:** 1
- **Unique Strategies:** 1
- **Exhibit Option:** A
- **Fiscal Year Range:** FY 2023-2024 only

### Spending by Fiscal Year
| Fiscal Year | Amount | % of Total |
|-------------|--------|------------|
| FY 2023-2024 | $3,756.14 | 100% |

### Spending by Strategy
| Strategy | Total Spent | % of County Budget |
|----------|-------------|-------------------|
| Recovery Support Services | $3,756.14 | 100% |

### Detailed Line Items
1. **[FY 2023-2024]** Recovery Support Services: $3,756.14

### Impact Metrics (from Narrative Reports)
**Population:** Approximately 35,000

**Organizational Development:**
- Bi-monthly Opioid Collaborative established (3rd Monday at 2:00 PM)
- Can attend virtually or in-person, open to public
- Annual community Opioid Collaborative meeting held October 16, 2023

**Key Outcomes:**
- Built strong collaborative infrastructure with sustained participation
- Developed marketing resources for Opioid Outreach Program
- Increased community engagement (2023 meeting had higher attendance than previous years)
- NC Association of County Commissioners representative participated

**Programs Being Developed (FY24):**
1. **Opioid Outreach Program** - Director visited other programs to learn best practices
2. **Family Treatment Court** - Being established
3. **Naloxone Distribution Program** - All first responders equipped, including volunteers
4. **Safe Choices Program** - PreK-12th grade prevention

**Partners in Opioid Collaborative:**
- County Health Department
- EMS
- Sheriff's Office
- Department of Social Services
- 911
- Board of County Commissioners
- Laurinburg Police Department
- Laurinburg Fire Department
- Scotland County Schools
- Scotland Health Care System
- Scotland County Court System
- Media
- Eastpointe
- Trillium

**Success Story Highlight:**
The Opioid Collaborative itself is Scotland's success story - sustained over multiple years despite member turnover, agencies consistently fill gaps, collaborative continues to meet and plan together

**Strategic Planning Process:**
- Community Needs Assessment Survey
- Input from commissioners, mayor, sheriff, police
- Emergency Department data analysis
- EMS and Fire Department call data
- Practitioner feedback
- Annual community meetings for citizen input

**Cost Effectiveness:**
- Building collaborative infrastructure: **$3,756**
- Cost per collaborative partner: $3,756 ÷ 13 = **$289 per partner**

**Note:** Scotland County is in early implementation phase. Most funds appear directed toward planning, coordination, and infrastructure development rather than direct services. This is reflected in lower spending but high organizational capacity building. Additional program expenditures are expected in FY 2024-2025.

---

## REGIONAL ANALYSIS & COMPARISONS

### Investment Levels vs. Service Delivery

| County | Investment | Population (est.) | Per Capita | People Served | Cost/Person | Efficiency Rank |
|--------|-----------|-------------------|------------|---------------|-------------|-----------------|
| Cumberland | $256,734 | 335,000 | $0.77 | 981 | $262 | 1st (Most efficient) |
| Robeson | $614,748 | 130,000 | $4.73 | 184+ | $3,341 | 4th |
| Columbus | $467,382 | 54,000 | $8.66 | 86 | $5,435 | 5th |
| Richmond | $269,740 | 43,000 | $6.27 | 30 | $8,991 | 6th |
| Bladen | $161,062 | 29,000 | $5.55 | 8 | $20,133 | 7th |
| Scotland | $3,756 | 35,000 | $0.11 | TBD | TBD | - (Infrastructure phase) |

**Key Insights:**
1. **Cumberland achieves lowest cost per person** ($262) due to high volume and efficient recovery support services
2. **Robeson's hospital-based model** serves fewer people but provides intensive MAT and medical supervision
3. **Columbus's comprehensive approach** (18 funding lines) addresses full continuum but at higher per-person cost
4. **Richmond's Samaritan Colony model** provides 100% completion and employment rates but serves smaller numbers
5. **Bladen's partnership approach** leverages Healing Place for intensive long-term stays (avg 126 days)
6. **Scotland in capacity-building phase** with minimal direct services spending to date

### Strategy Adoption Patterns

**Universal Strategies (All Counties):**
- Recovery Support Services - 6/6 counties (100%)

**Common Strategies (50%+):**
- Collaborative Strategic Planning - 4/6 counties (67%)
- Naloxone Distribution - 3/6 counties (50%)

**Innovative/Unique Strategies:**
- **Cumberland only:** Criminal Justice Diversion, Reentry Programs, SSP
- **Columbus only:** Data tracking software, school prevention, prescriber training, NAS training, media campaigns
- **Robeson only:** Evidence-Based Hospital Treatment, Employment Services, PORT

### Partnership Networks

**The Healing Place of New Hanover County serves:**
- Columbus (10-12 beds/day contracted)
- Bladen (8 individuals, 1,007 days)
- Referenced by Cumberland

**Regional Collaborations:**
- Robeson County + RRCOR Consortium + SPARC
- All counties participate in state CORE-NC reporting system

### Fiscal Year Trends

**FY 2022-2023 to FY 2023-2024 Growth:**
| County | FY 22-23 | FY 23-24 | Growth | % Increase |
|--------|----------|----------|--------|------------|
| Richmond | $8,893 | $260,847 | +$251,954 | +2,833% |
| Cumberland | $23,032 | $233,702 | +$210,670 | +914% |
| Columbus | $113,728 | $353,654 | +$239,927 | +211% |
| Robeson | $195,348 | $419,400 | +$224,052 | +115% |
| Bladen | $69,786 | $91,275 | +$21,489 | +31% |
| Scotland | $0 | $3,756 | +$3,756 | New |

**Analysis:** All counties dramatically increased spending in FY 23-24, suggesting initial planning/infrastructure phase in FY 22-23 followed by program implementation in FY 23-24.

### Outcome Achievements

**Harm Reduction Success:**
- Columbus: 39% drop in ED overdose visits
- Robeson: 26% drop in ED overdose visits (65→48)
- Cumberland: 1,492 naloxone kits distributed

**Treatment Access:**
- Cumberland: 981 individuals served (highest volume)
- Columbus: 86 individuals, 1,631 treatment days
- Robeson: 184 individuals treated

**Employment Success:**
- Richmond: 100% employment rate (30/30)
- Bladen: 100% employment rate (8/8)
- Cumberland: 175 served through employment services

**System Change:**
- Columbus: FirstWatch database tracking 5 EMS departments
- Cumberland: Naloxone vending machine innovation
- Scotland: Sustained multi-agency collaborative over years

---

## DATA RECONCILIATION NOTES FOR CLAUDE CODE

### Known Discrepancies to Address:

1. **Cumberland County Investment Amount:**
   - CORE-NC data shows: $256,734
   - Narratives state: "over $300,000"
   - **Action needed:** Add note in dashboard about possible additional funding streams

2. **Strategy Naming Conventions:**
   - CORE-NC uses verbose strategy names (e.g., "Research on improved service delivery for modalities such as SBIRT...")
   - Narratives use short names (e.g., "Recovery Support Services, Strategy 3")
   - **Action needed:** Create mapping table in dashboard code

3. **Exhibit Options:**
   - CORE-NC shows all counties as "Option A"
   - Narratives indicate Columbus expanded to "Option B"
   - **Action needed:** Add clarification that counties may have expanded mid-year

4. **Scotland County Data:**
   - Minimal spending data ($3,756)
   - Rich narrative about collaborative infrastructure
   - **Action needed:** Emphasize capacity-building phase in dashboard

5. **Fiscal Year Reporting:**
   - Financial data: State fiscal years (July-June)
   - Narrative data: Some references to calendar years
   - **Action needed:** Standardize all dates to state fiscal year format

### Data Extraction Checklist:

**From CORE-NC Excel (Complete ✓):**
- [x] Total spending by county
- [x] Spending by strategy
- [x] Fiscal year breakdowns
- [x] Line-item details
- [x] Strategy definitions

**From Narrative PDFs (To Extract):**
- [ ] People served counts
- [ ] Naloxone distribution numbers
- [ ] Treatment days provided
- [ ] Employment placements
- [ ] Outcome percentages (ED visit reductions, etc.)
- [ ] Success story text
- [ ] Partnership lists
- [ ] Program descriptions

**Calculated Metrics (To Build):**
- [ ] Cost per person served
- [ ] Cost per naloxone kit
- [ ] Cost per treatment day
- [ ] Year-over-year growth rates
- [ ] Regional comparisons
- [ ] Efficiency rankings

---

## RECOMMENDED DASHBOARD VIEWS

### View 1: Regional Overview
Show map with:
- County boundaries
- Color intensity by spending level
- Click to see county profile
- Summary statistics in sidebar

### View 2: Financial Deep Dive
- Bar chart: Total spending (existing, keep it)
- New: Stacked bar showing FY 22-23 vs FY 23-24
- New: Strategy category pie chart
- Filterable table of all line items
- Export to Excel button

### View 3: Impact Dashboard
- Metric cards:
  - Total people served: 2,168+
  - Total naloxone kits: 2,312+
  - Total treatment days: 2,638+
  - Counties with ED reduction: 2
- Charts:
  - People served by county (bar)
  - Treatment modalities (pie)
  - Overdose trends where available (line)

### View 4: Strategy Comparison Matrix
| Strategy | BLA | COL | CUM | RIC | ROB | SCO |
|----------|-----|-----|-----|-----|-----|-----|
| Recovery Support | ✓ $70K | ✓ $140K | ✓ $84K | ✓ $150K | ✓ $322K | ✓ $4K |
| Collaborative Planning | ✓ $91K | ✓ $15K | - | ✓ $83K | ✓ $3K | - |
| Naloxone Distribution | - | - | ✓ $30K | ✓ $37K | ✓ $13K | - |
| Evidence-Based Treatment | - | - | - | - | ✓ $125K | - |
| [etc...]

Heat map color coding by investment level.

### View 5: Success Stories Gallery
- Card layout
- Filter by: County, Strategy, Population Type
- Click to expand full story
- Include key metrics from each story
- "Share" button for advocacy

### View 6: County Profile Pages (Example: Cumberland)
```
┌──────────────────────────────────────────────────────────┐
│  CUMBERLAND COUNTY                           [Export PDF] │
│  Cumberland-Fayetteville Opioid Response Team (C-FORT)    │
├──────────────────────────────────────────────────────────┤
│  INVESTMENT SUMMARY                                       │
│  Total: $256,734  |  Rank: 4th of 6  |  8 Strategies    │
│                                                           │
│  [Bar chart showing strategy breakdown]                   │
│                                                           │
│  IMPACT AT A GLANCE                                       │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐       │
│  │  981    │ │  1,492  │ │  232    │ │  175    │       │
│  │ People  │ │ Naloxone│ │Treatment│ │Employment│      │
│  │ Served  │ │  Kits   │ │Referrals│ │ Services │      │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘       │
│                                                           │
│  PROGRAMS FUNDED                                          │
│  • LEAD Program (Law Enforcement Assisted Diversion)      │
│  • Detention Center MAT Program                           │
│  • Naloxone Vending Machine (First in region!)           │
│  • Recovery Housing Network                               │
│  • Reentry Support Services                               │
│                                                           │
│  SUCCESS HIGHLIGHTS                                       │
│  [Joey's Story card - click to expand]                    │
│  [Case #7298 card - click to expand]                      │
│                                                           │
│  PARTNERSHIPS                                             │
│  C-FORT • NC Harm Reduction Coalition • Carolina         │
│  Treatment Center • Myrover-Reese • Cape Fear Valley     │
│                                                           │
│  EFFICIENCY METRICS                                       │
│  Cost per person: $262 (Best in region!)                 │
│  Cost per kit: $172                                       │
└──────────────────────────────────────────────────────────┘
```

---

## FINAL IMPLEMENTATION NOTE

This comprehensive data profile provides Claude Code with everything needed to build a fully integrated dashboard that combines:

1. **Precise financial data** from CORE-NC Excel
2. **Real-world impact metrics** from narrative PDFs
3. **Contextual success stories** for stakeholder engagement
4. **Comparative analysis** across all six counties
5. **Trend data** showing fiscal year growth

The result will be a dashboard that answers the critical question: **"What did we get for our $1.77 million investment?"**

Answer: Over 2,168 lives touched, 2,312+ naloxone kits deployed, significant overdose reductions in two counties, and innovative programs that can serve as models for the rest of North Carolina.
