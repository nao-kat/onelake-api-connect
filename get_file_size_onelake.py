# This script retrieves the size of a file in Azure Data Lake Storage using the Azure SDK for Python.
# This file is used to verify that the data is actually stored in OneLake before attempting to read the numerical values from it.
from azure.identity import DefaultAzureCredential
from azure.storage.filedatalake import DataLakeServiceClient

def main():
    credential = DefaultAzureCredential()
    account_url = "https://onelake.dfs.fabric.microsoft.com"
    client = DataLakeServiceClient(account_url, credential=credential)

    workspace = "<your_workspace_name>"  # Replace with your workspace name
    lakehouse = "<your_lakehouse_name>"  # Replace with your lakehouse name
    target_path = f"{lakehouse}.lakehouse/<path_to_file>" #(e.g.) Tables/sample.csv


    fs = client.get_file_system_client(workspace)
    file_client = fs.get_file_client(target_path)

    props = file_client.get_file_properties()
    size_bytes = props.size
    print(f"File path: {target_path}")
    print(f"Size: {size_bytes} bytes ({size_bytes/1024**2:.2f} MB)")

if __name__ == "__main__":
    main()
