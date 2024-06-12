from faker import Faker
import pandas as pd


def generate_fake_user_data(num_data: int = 100, path: str = "fake_user.csv"):
    fake = Faker()
    df = pd.DataFrame(
        {
            "id": [x for x in range(1, num_data + 1)],
            "username": [fake.name() for _ in range(num_data)],
            "address": [fake.address() for _ in range(num_data)],
        }
    )
    df.to_csv(path, index=False)
