import json
import requests

base_url = "https://httpbin.org/"

def test_request_ok() -> None:
    url = f"{base_url}/post"
    expected_json = {"key_1": "value_1", "key_2": "value_2"}

    resp = requests.post(url, '{"key_1": "value_1", "key_2": "value_2"}')

    assert resp.status_code == 200

    resp_json = json.loads(resp.content)
    
    if resp_json["data"]:
        raw_data = resp_json["data"]
        response_data = json.loads(raw_data)
    
    assert response_data == expected_json

