from app.main import home


def test_home_returns_expected_payload():
    response = home()

    assert response["Model"]["title"] == "Python Dev"
    assert response["Model"]["company"] == "ABC Technologies"
    assert response["Schema"]["salary"] == 750000
