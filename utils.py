import json
import os
import uuid
import re
from datetime import datetime


def load_data(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_data(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def generate_pnr():
    return str(uuid.uuid4())[:8].upper()


def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None
def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10


def validate_age(age):
    return age.isdigit() and 1 <= int(age) <= 120


def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'
    return re.match(pattern, password) is not None


def validate_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False
def find_user_by_email(users, email):
    for user in users:
        if user.get("email") == email:
            return user
    return None


def find_train_by_number(trains, train_no):
    for train in trains:
        if str(train.get("train_no")) == str(train_no):
            return train
    return None


def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")


def get_current_time():
    return datetime.now().strftime("%H:%M:%S")