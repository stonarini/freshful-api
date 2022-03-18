import json


def test_get_one(client):
    res = client.get("/items/AgedBrie?sell_in=9&quality=9")
    data = json.loads(res.data)
    assert res.status_code == 200
    assert res.content_type == "application/json"
    assert set(["name", "sell_in", "quality"]) == set(data)
    assert data["name"] == "AgedBrie"
    assert data["sell_in"] == 9
    assert data["quality"] == 9

    res = client.get("/items/ConjuredItem?sell_in=3&quality=8")
    data = json.loads(res.data)
    assert res.status_code == 200
    assert res.content_type == "application/json"
    assert set(["name", "sell_in", "quality"]) == set(data)
    assert data["name"] == "ConjuredItem"
    assert data["sell_in"] == 3
    assert data["quality"] == 8


def test_get_one_inexistent(client):
    res = client.get("/items/AgedBrie?sell_in=100&quality=100")
    assert res.status_code == 200
    assert res.content_type == "application/json"
    assert res.data == b"null\n"
