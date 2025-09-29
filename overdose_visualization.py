#!/usr/bin/env python3
"""
Overdose Trends Visualization for SPARC Counties
Creates presentation-quality charts for overdose data analysis
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import numpy as np

# Set style for presentation-quality plots
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

def load_and_filter_data():
    """Load CSV data and filter for target counties and overdose data"""
    # Load the data
    df = pd.read_csv('county data/NCInjuryDataDL (1).csv')

    # Target counties
    target_counties = ['Robeson', 'Cumberland', 'Richmond', 'Columbus', 'Bladen', 'Scotland']

    # Filter for target counties and overdose death data
    county_data = df[
        (df['Ind Place'].isin(target_counties)) &
        (df['Ind Id'] == 'DEATH_ANY_MED_DRUG')
    ].copy()

    # Convert date column to datetime
    county_data['Date'] = pd.to_datetime(county_data['Ind Date Anchor'], errors='coerce')
    county_data['Year'] = county_data['Date'].dt.year

    # Clean numeric columns
    county_data['Deaths'] = pd.to_numeric(county_data['Ind Num'], errors='coerce')
    county_data['Rate'] = pd.to_numeric(county_data['Ind Rate'], errors='coerce')
    county_data['Population'] = pd.to_numeric(county_data['Ind Denom'], errors='coerce')

    # Drop rows with missing essential data
    county_data = county_data.dropna(subset=['Year', 'Deaths', 'Rate'])

    return county_data

def create_trends_line_chart(data):
    """Create line chart showing overdose death trends over time"""
    plt.figure(figsize=(14, 8))

    for county in data['Ind Place'].unique():
        county_subset = data[data['Ind Place'] == county].sort_values('Year')
        plt.plot(county_subset['Year'], county_subset['Deaths'],
                marker='o', linewidth=3, markersize=8, label=f'{county} County')

    plt.title('Overdose Death Trends by County (2011-Present)', fontsize=18, fontweight='bold', pad=20)
    plt.xlabel('Year', fontsize=14, fontweight='bold')
    plt.ylabel('Number of Overdose Deaths', fontsize=14, fontweight='bold')
    plt.legend(fontsize=12, frameon=True, shadow=True)
    plt.grid(True, alpha=0.3)

    # Improve tick labels
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    plt.tight_layout()
    plt.savefig('overdose_trends_line.png', dpi=300, bbox_inches='tight')
    print("Created: overdose_trends_line.png")

def create_rates_comparison_chart(data):
    """Create bar chart comparing overdose death rates"""
    # Get most recent year data for each county
    latest_data = data.loc[data.groupby('Ind Place')['Year'].idxmax()]

    plt.figure(figsize=(12, 8))
    bars = plt.bar(latest_data['Ind Place'], latest_data['Rate'],
                   color=['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6', '#1abc9c'],
                   alpha=0.8, edgecolor='black', linewidth=1.5)

    # Add value labels on bars
    for bar, value in zip(bars, latest_data['Rate']):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,
                f'{value:.1f}', ha='center', va='bottom', fontsize=12, fontweight='bold')

    plt.title('Overdose Death Rates by County (Most Recent Data)',
              fontsize=18, fontweight='bold', pad=20)
    plt.xlabel('County', fontsize=14, fontweight='bold')
    plt.ylabel('Deaths per 100,000 Population', fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)

    plt.tight_layout()
    plt.savefig('overdose_rates_comparison.png', dpi=300, bbox_inches='tight')
    print("Created: overdose_rates_comparison.png")

def create_heatmap_chart(data):
    """Create heatmap showing overdose trends across counties and years"""
    # Pivot data for heatmap
    heatmap_data = data.pivot(index='Ind Place', columns='Year', values='Rate')

    plt.figure(figsize=(14, 8))
    sns.heatmap(heatmap_data, annot=True, fmt='.1f', cmap='Reds',
                cbar_kws={'label': 'Deaths per 100,000 Population'},
                linewidths=0.5)

    plt.title('Overdose Death Rate Heatmap by County and Year',
              fontsize=18, fontweight='bold', pad=20)
    plt.xlabel('Year', fontsize=14, fontweight='bold')
    plt.ylabel('County', fontsize=14, fontweight='bold')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12, rotation=0)

    plt.tight_layout()
    plt.savefig('overdose_heatmap.png', dpi=300, bbox_inches='tight')
    print("Created: overdose_heatmap.png")

def create_total_deaths_chart(data):
    """Create chart showing total deaths by county across all years"""
    total_deaths = data.groupby('Ind Place')['Deaths'].sum().sort_values(ascending=False)

    plt.figure(figsize=(12, 8))
    bars = plt.bar(total_deaths.index, total_deaths.values,
                   color=['#c0392b', '#2980b9', '#27ae60', '#d68910', '#8e44ad', '#17a2b8'],
                   alpha=0.8, edgecolor='black', linewidth=1.5)

    # Add value labels on bars
    for bar, value in zip(bars, total_deaths.values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,
                f'{int(value)}', ha='center', va='bottom', fontsize=12, fontweight='bold')

    plt.title('Total Overdose Deaths by County (All Years Combined)',
              fontsize=18, fontweight='bold', pad=20)
    plt.xlabel('County', fontsize=14, fontweight='bold')
    plt.ylabel('Total Number of Deaths', fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)

    plt.tight_layout()
    plt.savefig('total_overdose_deaths.png', dpi=300, bbox_inches='tight')
    print("Created: total_overdose_deaths.png")

def print_summary_statistics(data):
    """Print summary statistics"""
    print("\n" + "="*60)
    print("OVERDOSE TRENDS SUMMARY")
    print("="*60)

    print(f"\nData Range: {int(data['Year'].min())} - {int(data['Year'].max())}")
    print(f"Counties Analyzed: {', '.join(sorted(data['Ind Place'].unique()))}")

    print("\nMost Recent Year Data:")
    latest_data = data.loc[data.groupby('Ind Place')['Year'].idxmax()]
    for _, row in latest_data.sort_values('Rate', ascending=False).iterrows():
        print(f"  {row['Ind Place']:12}: {row['Deaths']:3.0f} deaths ({row['Rate']:5.1f} per 100k)")

    print("\nTotal Deaths by County (All Years):")
    total_deaths = data.groupby('Ind Place')['Deaths'].sum().sort_values(ascending=False)
    for county, deaths in total_deaths.items():
        print(f"  {county:12}: {deaths:3.0f} total deaths")

def main():
    """Main function to create all visualizations"""
    print("Loading and processing overdose data...")

    try:
        data = load_and_filter_data()

        if data.empty:
            print("No data found for the specified counties and criteria.")
            return

        print(f"Found {len(data)} records for analysis")

        # Create all visualizations
        print("\nCreating visualizations...")
        create_trends_line_chart(data)
        create_rates_comparison_chart(data)
        create_heatmap_chart(data)
        create_total_deaths_chart(data)

        # Print summary
        print_summary_statistics(data)

        print(f"\nAll visualizations created successfully!")
        print("Files saved: overdose_trends_line.png, overdose_rates_comparison.png, overdose_heatmap.png, total_overdose_deaths.png")

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()