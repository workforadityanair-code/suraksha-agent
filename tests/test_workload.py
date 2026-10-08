import requests

print("[CLIENT] Sending signed transaction to Mock Gateway...")

try:
    headers = {
        "X-Gateway-Auth": "Bearer mock_valid_ed25519_signature_key_99"
    }
    res = requests.post(
        "http://host.docker.internal:8000/v1/dpi/verify", 
        json={"txn_id": "TXN_INDIA_1024", "amount": 250.0},
        headers=headers
    )
    print(f"[CLIENT] Status: {res.status_code}")
    print(f"[CLIENT] Response: {res.text}")
except Exception as e:
    print(f"[CLIENT] Failed to connect: {e}")