import requests
import os

# Load the AIO API token from environment variable
aio_api_token = os.getenv('AIO_API_TOKEN')
# aio_api_url = 'https://sportzinteractive.atlassian.net/plugins/servlet/ac/com.kaanha.jira.tcms/aio-tcms-app-overview?/api/v1/project/10322/testcycle/IQA-CY-1/import/results'  # Replace with your AIO API URL
aio_api_url = 'https://sportzinteractive.atlassian.net/plugins/servlet/ac/com.kaanha.jira.tcms/aio-tcms-app-overview?project.key=IQA&project.id=10322'

# Define the path to the Robot Framework results
results_path = '../../Mobile/Android/KC/results/output.xml'

# Prepare the request headers
headers = {
    'Authorization': f'AioAuth {aio_api_token}',
    'Content-Type': 'application/xml'
}

# Read the Robot Framework results file
with open(results_path, 'r') as file:
    results_xml = file.read()

# Send the results to AIO
response = requests.post(aio_api_url, headers=headers, data=results_xml)

# Check the response
if response.status_code == 200:
    print('results successfully updated to AIO.')
else:
    print(f'Failed to update results to AIO. Status code: {response.status_code}')
    print(f'Response: {response.text}')

