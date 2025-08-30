"""Excel formatting utilities."""
from openpyxl.styles import Font, PatternFill
from openpyxl.worksheet.worksheet import Worksheet

def format_header_row(worksheet: Worksheet, row: int = 1):
    """Apply consistent formatting to header row."""
    header_font = Font(bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
    
    for cell in worksheet[row]:
        if cell.value:
            cell.font = header_font
            cell.fill = header_fill

def auto_adjust_columns(worksheet: Worksheet):
    """Auto-adjust column widths based on content."""
    for column in worksheet.columns:
        max_length = 0
        column_letter = column[0].column_letter
        
        for cell in column:
            if cell.value:
                max_length = max(max_length, len(str(cell.value)))
        
        adjusted_width = min(max_length + 2, 50)  # Cap at 50 chars
        worksheet.column_dimensions[column_letter].width = adjusted_width
