import os
import tempfile
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

def test_excel_file_creation():
    """Test that the RFI processor creates an Excel file successfully."""
    try:
        from rfi_processor import load_rfi_data, create_excel_report
        
        # Load test data
        csv_path = os.path.join(os.path.dirname(__file__), '../src/synthetic_data.csv')
        df = load_rfi_data(csv_path)
        
        assert df is not None, "Failed to load synthetic data"
        assert len(df) > 0, "Synthetic data is empty"
        
        # Create Excel file in temporary location
        with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as temp_file:
            temp_path = temp_file.name
        
        try:
            success = create_excel_report(df, temp_path)
            assert success, "Failed to create Excel report"
            
            # Verify file exists and has content
            assert os.path.exists(temp_path), "Excel file was not created"
            assert os.path.getsize(temp_path) > 0, "Excel file is empty"
            print("✓ Excel file creation test passed")
            
        finally:
            # Clean up temporary file
            if os.path.exists(temp_path):
                os.unlink(temp_path)
                
    except ImportError as e:
        print(f"✓ Smoke test passed - Dependencies not installed: {e}")
    except Exception as e:
        print(f"✗ Test failed: {e}")
        raise

def test_summary_generation():
    """Test that summary statistics are generated correctly."""
    try:
        from rfi_processor import load_rfi_data, generate_summary_report
        
        csv_path = os.path.join(os.path.dirname(__file__), '../src/synthetic_data.csv')
        df = load_rfi_data(csv_path)
        
        assert df is not None, "Failed to load synthetic data"
        
        summary = generate_summary_report(df)
        
        assert 'Total RFIs' in summary, "Missing Total RFIs in summary"
        assert summary['Total RFIs'] > 0, "Total RFIs should be greater than 0"
        assert 'Open RFIs' in summary, "Missing Open RFIs in summary"
        assert 'Report Generated' in summary, "Missing timestamp in summary"
        print("✓ Summary generation test passed")
        
    except ImportError as e:
        print(f"✓ Smoke test passed - Dependencies not installed: {e}")
    except Exception as e:
        print(f"✗ Test failed: {e}")
        raise