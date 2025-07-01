from faker import Faker

class Helpers:
    fake = Faker()

    @staticmethod
    def fake_email():
        return Helpers.fake.email()