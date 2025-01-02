This Repo will hold Azure operations scripts

# Get ADLS Directory Sizes

This script calculates the sizes of specified directories in an Azure Data Lake Storage (ADLS) account.

## Prerequisites

- Python 3.6 or higher
- Azure SDK for Python
- Azure credentials with access to the ADLS account

## Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd azure_dbx_operations/adls
    ```

2. Install the required Python packages:
    ```sh
    pip install azure-identity azure-storage-file-datalake
    ```

## Usage

1. Create a JSON file containing the list of directory paths you want to check. For example, [directory_paths.json] as below:
    ```json
    [
        "path/to/directory1",
        "path/to/directory2"
    ]
    ```

2. Run the script with the required arguments:
    ```sh
    python get_adls_size.py --tenant_id <your_tenant_id> --client_id <your_client_id> --client_secret <your_client_secret> --account_name <your_account_name> --container_name <your_container_name> --directory_paths_file <path_to_directory_paths_file>
    ```

### Arguments

- `--tenant_id`: Tenant ID for authentication
- `--client_id`: Client ID for authentication
- `--client_secret`: Client Secret for authentication
- `--account_name`: ADLS account name
- `--container_name`: ADLS container name
- `--directory_paths_file`: Path to JSON file containing list of directory paths

### Example

```sh
python get_adls_size.py --tenant_id "your-tenant-id" --client_id "your-client-id" --client_secret "your-client-secret" --account_name "your-account-name" --container_name "your-container-name" --directory_paths_file "directory_paths.json"
