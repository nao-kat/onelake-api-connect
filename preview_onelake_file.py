#This file uses the Python SDK to retrieve and display the first 5 rows of table data stored in OneLake.

from azure.identity import DefaultAzureCredential
from azure.storage.filedatalake import DataLakeServiceClient

cred = DefaultAzureCredential()
svc = DataLakeServiceClient("https://onelake.dfs.fabric.microsoft.com", credential=cred)
fs = svc.get_file_system_client("<workspace_name>")  # Replace with your workspace name

file_path = "<path_to_your_file>"  # (e.g.) <lakehouse_name>.lakehouse/Tables/sample.csv
file_client = fs.get_file_client(file_path)

props = file_client.get_file_properties()
print(f"✅ File size: {props.size} bytes")

# Display only the first few lines after downloading.
download = file_client.download_file()
content = download.readall()
text = content.decode('utf-8', errors='ignore')  # Handle character encoding issues.

lines = text.splitlines()
for ln in lines[:5]:  # The first 5 rows.

    print(ln)