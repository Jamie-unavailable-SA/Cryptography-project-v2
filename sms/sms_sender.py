"""
We'll use infobip
"""

import os
import requests
from sms.sms_sender import send_sms_otp
send_sms_otp("+254111225169", "123456")

INFOBIP_BASE_URL = os.getenv("d9dvm8.api.infobip.com")
INFOBIP_API_KEY = os.getenv("e3a65ed3232a74d142876b47fdfca574-4bee5948-d20b-416a-9478-d27b3ea2d167")
INFOBIP_FROM_NUMBER = os.getenv("+254111225169")

if not all([INFOBIP_BASE_URL, INFOBIP_API_KEY, INFOBIP_FROM_NUMBER]):
    raise RuntimeError("Missing Infobip config (BASE_URL, API_KEY, FROM_NUMBER)")

def send_sms_otp(to_phone: str, otp_code: str) -> None:
    body = f"Your OTP is: {otp_code}"
    url = f"{INFOBIP_BASE_URL}/sms/2/text/advanced"
    headers = {
        "Authorization": f"App {INFOBIP_API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    payload = {
        "messages": [
            {
            "form": INFOBIP_FROM_NUMBER,
            "destinations": [{"to": to_phone}],
            "text": body,
            }
        ]
    }
    response = requests.post(url, headers = headers, json = payload)
    if response.ok:
        print(f"[✓] OTP sent via infobip to {to_phone}")
    else:
        print("[x] infobip error: ", response.status_code, response.text)
        response.raise_for_status()