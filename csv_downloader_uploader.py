## Currently Mojo is denying access to its S3 bucket with player data so we'll revisit this. Still need to add functionality such that it updates the csv on google drive rather than creating a new file.

import requests
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

# URL of the CSV file to download
csv_url = "https://s3.amazonaws.com/static.mojo.com/nba-data/future_stats.csv"

# Path to store the downloaded CSV file
csv_file_path = "Data/nba_data.csv"

# Google Drive API credentials (service account key) file path
credentials_file_path = "nba-mojo-csv-download-upload-a1661e90aca7.json"

# Google Drive folder ID where you want to upload the CSV file
drive_folder_id = "1_lbnl5-JWch9F9kUl1uee9iA_f70iiCM"

# # Google Drive file ID for the CSV file that you want to update
# csv_file_id = '1n1XiTR4LaJxOWTacDu5YOGDGb0_sD8yk'

# Function to download CSV file
def download_csv(url, file_path):
    response = requests.get(url)
    with open(file_path, "wb") as file:
        file.write(response.content)

# Function to upload CSV file to Google Drive
def upload_to_google_drive(file_path, folder_id, credentials_path):
# def upload_to_google_drive(file_path, file_id, folder_id, credentials_path):
    credentials = service_account.Credentials.from_service_account_file(credentials_path)
    
    drive_service = build("drive", "v3", credentials=credentials)

    file_metadata = {
        "name": os.path.basename(file_path),
        "parents": [folder_id]
    }
    
    # Create a new file
    media = drive_service.files().create(
        body=file_metadata,
        media_body=file_path,
        fields="id"
    )
    media = media.execute()

    # # Update existing file with csv_file_id (Not yet implemented)
    # media = drive_service.files().update(
    #     fileID=file_id
    #     body=file_metadata,
    #     media_body=file_path,
    # )
    # media = media.execute()

    print("File ID:", media.get("id"))

# Main function to download and upload CSV file
def main():
    download_csv(csv_url, csv_file_path)
    upload_to_google_drive(csv_file_path, drive_folder_id, credentials_file_path)
    # upload_to_google_drive(csv_file_path, csv_file_id, drive_folder_id, credentials_file_path)

if __name__ == "__main__":
    main()
