import argparse
import json
from azure.storage.filedatalake import DataLakeServiceClient
from azure.identity import ClientSecretCredential
from azure.core.exceptions import AzureError

def get_directory_sizes_gb(tenant_id, client_id, client_secret, account_name, container_name, directory_paths):
    try:
        print(f"Connecting to ADLS with account_name: {account_name}, container_name: {container_name}")
        credential = ClientSecretCredential(tenant_id, client_id, client_secret)
        service_client = DataLakeServiceClient(account_url=f"https://{account_name}.dfs.core.windows.net",
                                               credential=credential)

        file_system_client = service_client.get_file_system_client(file_system=container_name)

        sizes_gb = {}

        for directory_path in directory_paths:
            print(f"Processing directory: {directory_path}")
            total_size_bytes = 0
            paths = file_system_client.get_paths(path=directory_path, recursive=True)
            for path in paths:
                if not path.is_directory:
                    total_size_bytes += path.content_length

            total_size_gb = total_size_bytes / (1024 ** 3)  # Convert bytes to GB
            sizes_gb[directory_path] = total_size_gb

        return sizes_gb

    except AzureError as e:
        print(f"An error occurred: {e}")
        return None

def main(tenant_id, client_id, client_secret, account_name, container_name, directory_paths_file):
    print(f"tenant_id: {tenant_id}")
    print(f"client_id: {client_id}")
    print(f"account_name: {account_name}")
    print(f"container_name: {container_name}")
    print(f"directory_paths_file: {directory_paths_file}")

    with open(directory_paths_file, 'r') as f:
        directory_paths = json.load(f)

    sizes_gb = get_directory_sizes_gb(tenant_id, client_id, client_secret, account_name, container_name, directory_paths)
    if sizes_gb is not None:
        for directory, size in sizes_gb.items():
            print(f"Directory: {directory}, Size: {size:.2f} GB")
    else:
        print("Failed to retrieve the directory sizes.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get ADLS directory sizes.')
    parser.add_argument('--tenant_id', required=True, help='Tenant ID for authentication')
    parser.add_argument('--client_id', required=True, help='Client ID for authentication')
    parser.add_argument('--client_secret', required=True, help='Client Secret for authentication')
    parser.add_argument('--account_name', required=True, help='ADLS account name')
    parser.add_argument('--container_name', required=True, help='ADLS container name')
    parser.add_argument('--directory_paths_file', required=True, help='Path to JSON file containing list of directory paths')

    args = parser.parse_args()

    main(args.tenant_id, args.client_id, args.client_secret, args.account_name, args.container_name, args.directory_paths_file)
