import os
import shutil
import pandas as pd
import time

# Directory to organize
folder_path = "/path/to/your/folder"

# Create folders based on file extensions
def organize_files():
    for filename in os.listdir(folder_path):
        file_ext = filename.split('.')[-1].lower()
        ext_folder = os.path.join(folder_path, file_ext)

        if not os.path.exists(ext_folder):
            os.makedirs(ext_folder)

        shutil.move(os.path.join(folder_path, filename), ext_folder)
        print(f"Moved {filename} to {ext_folder}")

# Run the function to organize files
organize_files()


# Load the data
file_path = '/path/to/your/data.csv'
df = pd.read_csv(file_path)

# Cleaning process
def clean_data(df):
    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Fill missing values with a placeholder or mean/median
    df.fillna('N/A', inplace=True)

    # Convert column to lowercase
    df['column_name'] = df['column_name'].str.lower()

    # Save cleaned data
    df.to_csv('/path/to/cleaned_data.csv', index=False)
    print("Data cleaned and saved.")

# Run the cleaning function
clean_data(df)


# Path and number of days
folder_path = '/path/to/your/folder'
days = 30
seconds_in_day = 86400

# Function to remove old files
def delete_old_files():
    now = time.time()
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_age = now - os.path.getmtime(file_path)
            if file_age > days * seconds_in_day:
                os.remove(file_path)
                print(f"Deleted {filename} (older than {days} days)")

# Run the function to delete old files
delete_old_files()
