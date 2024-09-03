import requests

# Configuration
api_url = 'https://tcms.aiojiraapps.com/aio-tcms/api/v1/project/IQA/testcycle/IQA-CY-3/import/results?type=Robot'
api_token = 'YTJmNDBiNmUtMWZkNS0zZmFkLWI3NjYtMTYwN2QyMWY0ZTIwLjliZTFlZjVkLWZkMjMtNGUwMy1iN2ExLTk0MDZjOWUyMzMzOA=='  # Replace with your actual API token
file_path = '../../Mobile/Android/KC/results/output.xml'  # Path to the file you want to upload

# Prepare the headers
headers = {
    'accept': 'application/json;charset=utf-8',
    'Authorization': f'AioAuth {api_token}',
}

# Prepare the form data
files = {
    'file': open(file_path, 'rb')  # Open the file in binary read mode
}
data = {
    'createNewRun': 'true',
    'addCaseToCycle': 'true',
    'createCase': 'true',
    'forceUpdateCase': 'true',
}

# Make the POST request
try:
    response = requests.post(api_url, headers=headers, files=files, data=data)

    # Check the response
    if response.status_code == 200:
        print('Results successfully updated to AIO.')
    else:
        print(f'Failed to update results to AIO. Status code: {response.status_code}')
        print(f'Response: {response.text}')
except requests.exceptions.RequestException as e:
    print(f'Request failed: {e}')
finally:
    # Ensure the file is closed after the request
    files['file'].close()

