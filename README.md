# NBA_Mojo_Data_Uploader

This repository contains the python script that I use to download NBA player data as a csv file from https://s3.amazonaws.com/static.mojo.com/nba-data/future_stats.csv and upload it to my google drive folder. I use windows scheduler to download the data daily and then the Google Cloud API as part of my python script to upload the data file to google drive. 

This repository does NOT contain my windows scheduler task but follow this tutorial: https://www.jcchouinard.com/python-automation-using-task-scheduler/ if you have windows. The Linux/MacOS equivalent is called Cron. It also does NOT contain the JSON file with my Google Cloud API keys. You will need to go to https://console.cloud.google.com/ and authorize Google Drive access, create a service project, create an API key for the project, and save the JSON file that it provides. Lastly for your drive folder ID, go inside your desired drive folder and copy the last section of its URL.

The functionality currently creates a new file every time the script is run, but I will be changing this to only update the existing file. The code for that is commented out because I haven't correctly implemented it yet. I will do so after what's below happens.  

As a note, the url for the AWS S3 bucket currently denies access. It was working as of October 12th, so I'll make sure to check back to see when it starts working again. 
