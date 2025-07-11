"""
loads all necessary environment variables & provides defaults
"""

import os
from typing import Optional
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

INFOBIP_BASE_URL: Optional[str] = os.getenv("d9dvm8.api.infobip.com")
INFOBIP_API_KEY: Optional[str] = os.getenv("e3a65ed3232a74d142876b47fdfca574-4bee5948-d20b-416a-9478-d27b3ea2d167")
INFOBIP_FROM_NUMBER: Optional[str] = os.getenv("+254111225169")

if not INFOBIP_BASE_URL or not INFOBIP_API_KEY or not INFOBIP_FROM_NUMBER:
    raise RuntimeError("Missing required infobip configuration(API key, base URL or sender ID)")

DEFAULT_OTP_LENGTH: int = int(os.getenv("DEFAULT_OTP_LENGTH", "6"))
DEFAULT_OTP_TTL_SECONDS: int = int(os.getenv("DEFAULT_OTP_TTL", "300"))