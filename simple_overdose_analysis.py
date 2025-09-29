#!/usr/bin/env python3
"""
Simple Overdose Trends Analysis for SPARC Counties
Uses only built-in Python libraries to analyze overdose data
"""

import csv
import json
from collections import defaultdict
from datetime import datetime

def load_and_analyze_data():
    """Load CSV data and analyze overdose trends for target counties"""
    target_counties = ['Robeson', 'Cumberland', 'Richmond', 'Columbus', 'Bladen', 'Scotland']

    county_data = defaultdict(list)

    print("Loading data from CSV file...")

    try:
        with open('county data/NCInjuryDataDL (1).csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                # Filter for target counties and overdose death data
                if (row['Ind Place'] in target_counties and
                    row['Ind Id'] == 'DEATH_ANY_MED_DRUG' and
                    row['Ind Date Anchor']):

                    try:
                        # Parse date and extract year
                        date_str = row['Ind Date Anchor']
                        if '/' in date_str:
                            year = int(date_str.split('/')[-1])
                        else:
                            year = int(date_str[:4])

                        # Parse numeric data
                        deaths = int(row['Ind Num']) if row['Ind Num'].replace(',', '').isdigit() else 0
                        rate = float(row['Ind Rate']) if row['Ind Rate'].replace(',', '').replace('.', '').isdigit() else 0.0
                        population = int(row['Ind Denom'].replace(',', '')) if row['Ind Denom'].replace(',', '').isdigit() else 0

                        county_data[row['Ind Place']].append({
                            'year': year,
                            'deaths': deaths,
                            'rate': rate,
                            'population': population
                        })

                    except (ValueError, IndexError):
                        continue

    except FileNotFoundError:
        print("Error: CSV file not found!")
        return None

    # Sort data by year for each county
    for county in county_data:
        county_data[county].sort(key=lambda x: x['year'])

    return dict(county_data)

def print_trends_analysis(data):
    """Print comprehensive analysis of overdose trends"""
    print("\n" + "="*80)
    print("OVERDOSE TRENDS ANALYSIS FOR SPARC COUNTIES")
    print("="*80)

    if not data:
        print("No data available for analysis.")
        return

    # Get year range
    all_years = set()
    for county_records in data.values():
        for record in county_records:
            all_years.add(record['year'])

    min_year, max_year = min(all_years), max(all_years)
    print(f"\nData Period: {min_year} - {max_year}")
    print(f"Counties: {', '.join(sorted(data.keys()))}")

    # Most recent data analysis
    print(f"\n{'-'*60}")
    print("MOST RECENT DATA (Latest Available Year for Each County)")
    print(f"{'-'*60}")

    recent_data = []
    for county, records in data.items():
        if records:
            latest = max(records, key=lambda x: x['year'])
            recent_data.append((county, latest))

    # Sort by death rate (highest to lowest)
    recent_data.sort(key=lambda x: x[1]['rate'], reverse=True)

    print(f"{'County':<12} {'Year':<6} {'Deaths':<8} {'Rate per 100k':<12} {'Population':<12}")
    print("-" * 60)
    for county, latest in recent_data:
        print(f"{county:<12} {latest['year']:<6} {latest['deaths']:<8} {latest['rate']:<12.1f} {latest['population']:<12,}")

    # Historical trends analysis
    print(f"\n{'-'*60}")
    print("HISTORICAL TRENDS SUMMARY")
    print(f"{'-'*60}")

    for county in sorted(data.keys()):
        records = data[county]
        if len(records) < 2:
            continue

        first_year = records[0]
        last_year = records[-1]

        # Calculate trend
        years_span = last_year['year'] - first_year['year']
        death_change = last_year['deaths'] - first_year['deaths']
        rate_change = last_year['rate'] - first_year['rate']

        trend_direction = "↑" if death_change > 0 else "↓" if death_change < 0 else "→"

        print(f"\n{county} County:")
        print(f"  Period: {first_year['year']} - {last_year['year']} ({years_span} years)")
        print(f"  Deaths: {first_year['deaths']} → {last_year['deaths']} ({death_change:+d}) {trend_direction}")
        print(f"  Rate: {first_year['rate']:.1f} → {last_year['rate']:.1f} ({rate_change:+.1f} per 100k)")

        # Calculate average annual change
        if years_span > 0:
            avg_annual_change = death_change / years_span
            print(f"  Avg annual change: {avg_annual_change:+.1f} deaths/year")

    # Total deaths summary
    print(f"\n{'-'*60}")
    print("TOTAL DEATHS BY COUNTY (All Years Combined)")
    print(f"{'-'*60}")

    county_totals = []
    for county, records in data.items():
        total_deaths = sum(record['deaths'] for record in records)
        county_totals.append((county, total_deaths))

    county_totals.sort(key=lambda x: x[1], reverse=True)

    for county, total in county_totals:
        print(f"{county:<12}: {total:>4} total deaths")

    # Year-by-year breakdown for highest-impact county
    if county_totals:
        highest_county = county_totals[0][0]
        print(f"\n{'-'*60}")
        print(f"YEAR-BY-YEAR BREAKDOWN: {highest_county.upper()} COUNTY")
        print(f"{'-'*60}")

        records = data[highest_county]
        print(f"{'Year':<6} {'Deaths':<8} {'Rate':<10} {'Population':<12}")
        print("-" * 36)
        for record in records:
            print(f"{record['year']:<6} {record['deaths']:<8} {record['rate']:<10.1f} {record['population']:<12,}")

def create_simple_csv_report(data):
    """Create a simple CSV report for easy import into presentation tools"""
    if not data:
        return

    # Create summary report
    with open('overdose_summary_report.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write header
        writer.writerow(['County', 'Year', 'Deaths', 'Rate_per_100k', 'Population'])

        # Write all data
        for county, records in sorted(data.items()):
            for record in records:
                writer.writerow([
                    county,
                    record['year'],
                    record['deaths'],
                    round(record['rate'], 1),
                    record['population']
                ])

    print(f"\nCreated: overdose_summary_report.csv")
    print("This file can be imported into Excel, Google Sheets, or other visualization tools.")

def main():
    """Main function"""
    print("SPARC Counties Overdose Data Analysis")
    print("Analyzing data for: Robeson, Cumberland, Richmond, Columbus, Bladen, and Scotland counties")

    # Load and analyze data
    data = load_and_analyze_data()

    if data:
        print(f"\nSuccessfully loaded data for {len(data)} counties")

        # Print analysis
        print_trends_analysis(data)

        # Create CSV report
        create_simple_csv_report(data)

        print(f"\n{'='*80}")
        print("ANALYSIS COMPLETE")
        print("For presentation-quality charts, import overdose_summary_report.csv into:")
        print("- Excel or Google Sheets for quick charts")
        print("- Tableau, Power BI, or similar tools for advanced visualizations")
        print("- Python with matplotlib/seaborn (if packages are available)")
        print("="*80)

    else:
        print("Failed to load data. Please check the CSV file.")

if __name__ == "__main__":
    main()