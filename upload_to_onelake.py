# Upload file to OneLake

from azure.identity import DefaultAzureCredential
from azure.storage.filedatalake import DataLakeServiceClient

cred = DefaultAzureCredential()
svc = DataLakeServiceClient("https://onelake.dfs.fabric.microsoft.com", credential=cred)
fs = svc.get_file_system_client("<workspace_name>")  # Replace with your workspace name

# Directory path in the lakehouse
dir_path = "<path_to_lakehouse_directory>"  # Replace with your directory path
dir_client = fs.get_directory_client(dir_path)
try:
    dir_client.create_directory()
except Exception:
    pass  # Ignore if the directory already exists

# Upload file
file_client = dir_client.get_file_client("<file_name>")  # Replace with your file name
with open("<path_to_your_file>", "rb") as f:
    file_client.upload_data(f, overwrite=True)

print("✅ Sucessefully uploaded to Lakehouse : " + dir_path )
