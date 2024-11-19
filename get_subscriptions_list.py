#### This script will use Service Principal for authentication

import requests
import json

# Service principal credentials
tenant_id = 'your-tenant-id'
client_id = 'your-client-id'
client_secret = 'your-client-secret'
resource = 'https://management.azure.com/'

def get_access_token(tenant_id, client_id, client_secret, resource):
    url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"
    payload = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'resource': resource
    }

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        return response.json().get('access_token')
    except requests.exceptions.RequestException as e:
        print(f"Error obtaining access token: {e}")
        return None

def list_subscriptions(access_token):
    url = "https://management.azure.com/subscriptions?api-version=2020-01-01"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error listing subscriptions: {e}")
        return None

def main():
    access_token = get_access_token(tenant_id, client_id, client_secret, resource)
    if access_token:
        subscriptions = list_subscriptions(access_token)
        if subscriptions:
            print(json.dumps(subscriptions, indent=2))

if __name__ == "__main__":
    main()
