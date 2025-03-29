import pandas as pd

def get_insights(file_path):
    try:
        # Read CSV file
        df = pd.read_csv(file_path)

        # Extract basic insights
        insights = {
            "columns": df.columns.tolist(),  # Column names
            "summary": df.describe().to_dict(),  # Statistical summary
            "missing_values": df.isnull().sum().to_dict(),  # Count of missing values per column
        }
        
        return insights

    except Exception as e:
        return {"error": str(e)}
