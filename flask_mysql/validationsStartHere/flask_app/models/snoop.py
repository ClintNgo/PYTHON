from flask import flash
import re
class Snoop:

    @staticmethod
    def validate_victim(victim):
        email_regex = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]+$')
        social_regex = re.compile(r'^\d{3}-\d{2}-\d{4}$')
        is_valid = True

        if len(victim["fullname"]) < 1:
            flash ("Full Name is required!")
            is_valid = False
        if not email_regex.match(victim["email"]):
            flash ("Invalid Email!")
            is_valid = False
        if len(victim["maiden"]) < 1:
            flash ("Mother's maiden name is required!")
            is_valid = False
        if not social_regex.match(victim["social"]):
            flash ("Invalid Social!")
            is_valid = False
        if "trash" not in victim:
            flash ("We need your trash")
            is_valid = False
        return is_valid