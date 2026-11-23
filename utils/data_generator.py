# utils/test_data.py

from uuid import uuid4


class DataGenerator:

    @staticmethod
    def get_name():
        return f"User_{uuid4().hex[:6]}"

    @staticmethod
    def get_email():
        return f"user_{uuid4().hex[:8]}@gmail.com"