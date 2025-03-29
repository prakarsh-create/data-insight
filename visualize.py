import pandas as pd
import matplotlib.pyplot as plt
import os

STATICS_FOLDER = "statics"
os.makedirs(STATICS_FOLDER, exist_ok=True)

def generate_visual(file_path):
    try:
        # Read CSV file
        df = pd.read_csv(file_path)

        # Select numerical columns
        num_columns = df.select_dtypes(include=["number"]).columns
        
        if len(num_columns) > 0:
            # Create histogram for the first numeric column
            plt.figure(figsize=(8, 6))
            df[num_columns[0]].hist()
            plt.title(f"Histogram of {num_columns[0]}")
            plt.xlabel(num_columns[0])
            plt.ylabel("Frequency")

            # Save plot as an image
            plot_path = os.path.join(STATICS_FOLDER, "histogram.png")
            plt.savefig(plot_path)
            plt.close()
        
        return plot_path if len(num_columns) > 0 else None

    except Exception as e:
        return {"error": str(e)}
