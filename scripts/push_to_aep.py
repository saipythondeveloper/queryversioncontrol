import os
import json
import requests

# Get the file passed from GitHub Actions
sql_file_path = os.getenv("SQL_FILE_PATH")
if not sql_file_path:
    raise ValueError("SQL_FILE_PATH env variable not provided.")

# Read SQL from file
with open(sql_file_path, "r") as f:
    sql_content = f.read().strip()

# Extract name from filename (remove extension, replace _ with space)
file_name = os.path.basename(sql_file_path).replace(".sql", "")
query_name = file_name.replace("_", " ")

# Prepare AEP API call
aep_url = f"https://platform.adobe.io/data/foundation/query/query-templates/{file_name}"

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f"Bearer {os.getenv('AEP_TOKEN')}",
    'x-gw-ims-org-id': os.getenv("AEP_ORG_ID"),
    'x-api-key': os.getenv("AEP_API_KEY"),
    'x-sandbox-name': os.getenv("AEP_SANDBOX")
}

payload = json.dumps({
    "sql": sql_content,
    "name": query_name
})

response = requests.put(aep_url, headers=headers, data=payload)

print("Status Code:", response.status_code)
print("Response:", response.text)

if response.status_code not in [200, 201]:
    raise SystemExit("Failed to push to AEP")
