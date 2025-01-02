This Repo will hold Azure operations simple scripts

get_adls_size.py -- Uses Sp credentials to get size of required storage account, container, directory sizes in GB

Usage: 

```
python /Users/krishna/scripts/get_adls_size.py --tenant_id YOUR_TENANT_ID --client_id YOUR_CLIENT_ID --client_secret YOUR_CLIENT_SECRET --account_name YOUR_ACCOUNT_NAME --container_name YOUR_CONTAINER_NAME --directory_paths "/path/of/directory_list"
