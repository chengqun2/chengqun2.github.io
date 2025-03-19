import pandas as pd
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def read_and_print_excel(file_path: str) -> pd.DataFrame:
    """
    Read and analyze Excel file contents with detailed logging.
    
    Args:
        file_path (str): Path to the Excel file
    Returns:
        pd.DataFrame: The loaded Excel data
    """
    try:
        # Validate file exists
        excel_path = Path(file_path)
        if not excel_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
            
        # Read Excel with explicit parameters
        df = pd.read_excel(
            file_path,
            engine='openpyxl',
            na_filter=False,  # Don't interpret empty cells as NaN
            keep_default_na=False  # Don't convert default NA values
        )
        
        # Log detailed information about the data
        logger.info(f"Total rows read: {len(df)}")
        logger.info(f"Columns found: {df.columns.tolist()}")
        
        # Check for empty rows
        empty_rows = df.index[df.isnull().all(1)].tolist()
        if empty_rows:
            logger.warning(f"Found empty rows at indices: {empty_rows}")
            
        # Print row by row for debugging
        logger.info("\nRow by row contents:")
        for index, row in df.iterrows():
            logger.info(f"Row {index}: {row.to_dict()}")
        
        return df
        
    except Exception as e:
        logger.error(f"Error reading Excel file: {str(e)}")
        raise

if __name__ == "__main__":
    try:
        excel_file_path = "F:/Academy/tutors.xlsx"
        df = read_and_print_excel(excel_file_path)
        
        # Additional checks
        logger.info(f"\nShape of dataframe: {df.shape}")
        logger.info(f"Column dtypes:\n{df.dtypes}")
        
    except Exception as e:
        logger.error(f"Failed to process Excel file: {e}")