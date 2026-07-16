from typing import TypedDict, Optional, List


class UserProfile(TypedDict):
    id: int
    name: str
    email: str
    bio: Optional[str]


def format_user_profile(users: List[UserProfile]) -> List[str]:
    formatted_users = []

    for user in users:
        profile = (
            f"ID: {user['id']}\n"
            f"Name: {user['name']}\n"
            f"Email: {user['email']}\n"
            f"Bio: {user['bio'] if user['bio'] else 'No bio available'}"
        )
        formatted_users.append(profile)

    return formatted_users


users = [
    {
        "id": 1,
        "name": "Alice",
        "email": "alice@example.com",
        "bio": "Python Developer",
    },
    {
        "id": 2,
        "name": "Bob",
        "email": "bob@example.com",
        "bio": None,
    },
    {
        "id": 3,
        "name": "Charlie",
        "email": "charlie@example.com",
        "bio": "Data Scientist",
    },
]

profiles = format_user_profile(users)

for profile in profiles:
    print(profile)
    print("-" * 30)