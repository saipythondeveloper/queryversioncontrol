import os
import json
import requests

sql_file_paths = os.getenv("SQL_FILE_PATH", "").strip().split()
if not sql_file_paths:
    raise ValueError("No SQL files provided.")

headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsIng1dSI6Imltc19uYTEta2V5LWF0LTEuY2VyIiwia2lkIjoiaW1zX25hMS1rZXktYXQtMSIsIml0dCI6ImF0In0.eyJpZCI6IjE3NjI1NDIzNTM1ODhfMmYxY2U0YzMtZDkwMC00NzE3LWJiM2ItYTFlMWZlZmExOTc1X3V3MiIsIm9yZyI6IkU3RTdBMDMzNTU3NkM1QkM3RjAwMDEwMUBBZG9iZU9yZyIsInR5cGUiOiJhY2Nlc3NfdG9rZW4iLCJjbGllbnRfaWQiOiI3MTQ5ZTJhMjU4MGI0OTcyOWI4NzNlOTRlZTYwODljZiIsInVzZXJfaWQiOiIzQkI5MjJGNzY4RkE4RTc4MEE0OTVDNDVAdGVjaGFjY3QuYWRvYmUuY29tIiwiYXMiOiJpbXMtbmExIiwiYWFfaWQiOiIzQkI5MjJGNzY4RkE4RTc4MEE0OTVDNDVAdGVjaGFjY3QuYWRvYmUuY29tIiwiY3RwIjozLCJtb2kiOiI2MTFhZTM4NSIsImV4cGlyZXNfaW4iOiI4NjQwMDAwMCIsImNyZWF0ZWRfYXQiOiIxNzYyNTQyMzUzNTg4Iiwic2NvcGUiOiJvcGVuaWQsc2Vzc2lvbixBZG9iZUlELHJlYWRfb3JnYW5pemF0aW9ucyxhZGRpdGlvbmFsX2luZm8ucHJvamVjdGVkUHJvZHVjdENvbnRleHQifQ.QKNZ3k-UI0YpyBaB07z2J0Ya-NVqeNwR3JHwp6R2e9u1P2d9daxOOc8QEWugaHEYyDxYpgdLfJUom-oN46k2vCY0ghdIW02d1m5_lkL2QijbXpoKa1uW-x6EZhrxZi1UvlOwTp5i6x3RHC-VZixNYHN1676nfOZ0-IYUqX0t1tmFxPy5BUmyyvZ4D7JBPqRVdSwQZ9jQGIQceT9r1chZbkMCZ0NRexT-rn381_0x4dPxsdw_Z6ieP6XEGkua7atFSgnNl5po5E_k3uQtiRcFwJDyCTrS-E0DdOgL6ZG3wZ4iE0B0LJFX95RgUqPEvkQSxRSjXrYkCnFanNW5QiJJZA',
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

    if response.status_code not in [200, 201, 202]:
        raise SystemExit(f"Failed to push {file_name} to AEP")
