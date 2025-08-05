from datetime import datetime


def generate_unique_email():
    return f"user_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}@example.com"

def generate_unique_name():
    return f"User_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"