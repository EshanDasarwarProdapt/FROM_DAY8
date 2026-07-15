from user_auth import UserAuth


def test_register_login():
    auth = UserAuth()

    assert auth.register("user1", "password") == True
    assert auth.login("user1", "password") == True


def test_register_existing_user():
    auth = UserAuth()

    # admin already exists in UserAuth
    assert auth.register("admin", "newpassword") == False


def test_login_wrong_password():
    auth = UserAuth()

    auth.register("user2", "password2")

    assert auth.login("user2", "wrongpassword") == False