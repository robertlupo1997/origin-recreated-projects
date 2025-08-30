#!/usr/bin/env python3

import pandas as pd
import os
from datetime import datetime
import tempfile
import argparse

def load_rfi_data(csv_path):
    """Load RFI data from CSV file."""
    try:
        df = pd.read_csv(csv_path)
        df['date_submitted'] = pd.to_datetime(df['date_submitted'])
        return df
    except FileNotFoundError:
        print(f"Error: CSV file not found at {csv_path}")
        return None
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None

def generate_summary_report(df):
    """Generate summary statistics from RFI data."""
    summary = {
        'Total RFIs': len(df),
        'Open RFIs': len(df[df['status'] == 'Open']),
        'Pending RFIs': len(df[df['status'] == 'Pending']),
        'Closed RFIs': len(df[df['status'] == 'Closed']),
        'Critical Priority': len(df[df['priority'] == 'Critical']),
        'High Priority': len(df[df['priority'] == 'High']),
        'Average Estimated Cost': df['estimated_cost'].mean(),
        'Total Estimated Cost': df['estimated_cost'].sum(),
        'Most Common Category': df['category'].mode().iloc[0] if not df['category'].mode().empty else 'N/A',
        'Report Generated': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return summary

def create_excel_report(df, output_path):
    """Create Excel report with multiple sheets."""
    try:
        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            # Main data sheet
            df.to_excel(writer, sheet_name='RFI_Data', index=False)
            
            # Summary sheet
            summary = generate_summary_report(df)
            summary_df = pd.DataFrame(list(summary.items()), columns=['Metric', 'Value'])
            summary_df.to_excel(writer, sheet_name='Summary', index=False)
            
            # Category breakdown
            category_stats = df.groupby('category').agg({
                'rfi_id': 'count',
                'estimated_cost': ['sum', 'mean']
            }).round(2)
            category_stats.columns = ['Count', 'Total_Cost', 'Avg_Cost']
            category_stats.to_excel(writer, sheet_name='Category_Breakdown')
            
            # Status breakdown
            status_stats = df.groupby('status').size().reset_index(name='Count')
            status_stats.to_excel(writer, sheet_name='Status_Breakdown', index=False)
        
        return True
    except Exception as e:
        print(f"Error creating Excel file: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Process RFI data and generate Excel report')
    parser.add_argument('--input', default='synthetic_data.csv', help='Input CSV file path')
    parser.add_argument('--output', help='Output Excel file path')
    parser.add_argument('--temp', action='store_true', help='Use temporary directory for output')
    
    args = parser.parse_args()
    
    # Determine input path (relative to script location)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, args.input)
    
    # Load data
    print(f"Loading RFI data from {csv_path}")
    df = load_rfi_data(csv_path)
    
    if df is None:
        return 1
    
    print(f"Loaded {len(df)} RFI records")
    
    # Determine output path
    if args.temp:
        temp_dir = tempfile.gettempdir()
        output_path = os.path.join(temp_dir, 'rfi_report.xlsx')
    elif args.output:
        output_path = args.output
    else:
        output_path = os.path.join(script_dir, 'rfi_report.xlsx')
    
    # Create Excel report
    print(f"Generating Excel report: {output_path}")
    success = create_excel_report(df, output_path)
    
    if success:
        print(f"Excel report successfully created: {output_path}")
        return 0
    else:
        print("Failed to create Excel report")
        return 1

if __name__ == "__main__":
    exit(main())