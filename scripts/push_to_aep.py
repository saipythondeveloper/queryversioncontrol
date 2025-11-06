import os
import json
import requests

sql_file_paths = os.getenv("SQL_FILE_PATH", "").strip().split()
if not sql_file_paths:
    raise ValueError("No SQL files provided.")

headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsIng1dSI6Imltc19uYTEta2V5LWF0LTEuY2VyIiwia2lkIjoiaW1zX25hMS1rZXktYXQtMSIsIml0dCI6ImF0In0.eyJpZCI6IjE3NjI0NDYxNjIwNjVfODg2YWM4MzEtZTQ1Yy00NmVjLTlkZjAtMmFiNjcwNWJkNzJhX3V3MiIsIm9yZyI6IkU3RTdBMDMzNTU3NkM1QkM3RjAwMDEwMUBBZG9iZU9yZyIsInR5cGUiOiJhY2Nlc3NfdG9rZW4iLCJjbGllbnRfaWQiOiI3MTQ5ZTJhMjU4MGI0OTcyOWI4NzNlOTRlZTYwODljZiIsInVzZXJfaWQiOiIzQkI5MjJGNzY4RkE4RTc4MEE0OTVDNDVAdGVjaGFjY3QuYWRvYmUuY29tIiwiYXMiOiJpbXMtbmExIiwiYWFfaWQiOiIzQkI5MjJGNzY4RkE4RTc4MEE0OTVDNDVAdGVjaGFjY3QuYWRvYmUuY29tIiwiY3RwIjozLCJtb2kiOiIzMDRkNmJmMCIsImV4cGlyZXNfaW4iOiI4NjQwMDAwMCIsInNjb3BlIjoib3BlbmlkLHNlc3Npb24sQWRvYmVJRCxyZWFkX29yZ2FuaXphdGlvbnMsYWRkaXRpb25hbF9pbmZvLnByb2plY3RlZFByb2R1Y3RDb250ZXh0IiwiY3JlYXRlZF9hdCI6IjE3NjI0NDYxNjIwNjUifQ.dTrqiCokifMLcNmG5pLlw_UEDnhXnbTLeVm5x33gLaQnrwOj3ZcQD2hWtLrzbExm8oofrlLQ3Vjk6YKrSgjlwI1aRhdA2u64oIYo2fLBcoybZdEV23oeFbrDaAjCWuPpD1vWIjamaWqBZQo5KBdD6r0u_L1O-X5uCeMtfV-r-4dsPb7sVHwDOMN8vBHBzDYSpDJsYf5m0fe3roSZP9y4bnh5NlUdDvwdfytT6RtHpNRZ6vnveHmXXucrsZqJeOaORwYT1gYfSgIbZgV293Jyx61BNzKFVKS3dwQc5ZIdWNuoeu-yif-MF2O4Hvv7aY9bJLs1oq7AX0VH-OPBSRAVMA',
  'x-gw-ims-org-id': 'E7E7A0335576C5BC7F000101@AdobeOrg',
  'x-api-key': '7149e2a2580b49729b873e94ee6089cf',
  'x-sandbox-name': 'aep-bootcamp',
  #'x-request-id': '{{x-request-id}}',
  #'User-Agent': '{{User-Agent}}'
}


for sql_file_path in sql_file_paths:
    with open(sql_file_path, "r") as f:
        sql_content = f.read().strip()

    file_name = os.path.basename(sql_file_path).replace(".sql", "")
    query_name = file_name.replace("_", " ")
    aep_url = "https://platform.adobe.io/data/foundation/query/query-templates/34ef17e7-ea09-4a83-93d9-1d7d340815bb"

    payload = json.dumps({
        "sql": sql_content,
        "name": query_name
    })

    print(f"Pushing {file_name} to AEP...")
    response = requests.put(aep_url, headers=headers, data=payload)
    print("Status Code:", response.status_code)
    print("Response:", response.text)

    if response.status_code not in [200, 201]:
        raise SystemExit(f"Failed to push {file_name} to AEP")
