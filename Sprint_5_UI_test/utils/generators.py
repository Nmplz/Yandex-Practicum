import random
import string
from datetime import datetime


def generate_random_email(domain):
    name = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{name}{domain}"


def generate_randon_password():
    pwd = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=8))
    return pwd

def generate_unique_title(base_name: str = "Good") -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{base_name}_{timestamp}"
