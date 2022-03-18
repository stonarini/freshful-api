import json


def test_update_one(client):
    res = client.patch("/items/AgedBrie?sell_in=100&quality=100")
    assert res.status_code == 200
    assert res.content_type == "application/json"
    assert res.data == b"null\n"

    res = client.get("/items/AgedBrie?sell_in=100&quality=100")
    assert res.status_code == 200
    assert res.content_type == "application/json"
    assert json.loads(res.data) == {"name": "AgedBrie", "sell_in": 100, "quality": 100}

    res = client.get("/items/AgedBrie")
    data = json.loads(res.data)
    assert len(data) == 3
    assert res.status_code == 200
    assert res.content_type == "application/json"


def test_update_one_default_values(client):
    res = client.patch("/items/AgedBrie")
    assert res.status_code == 200
    assert res.content_type == "application/json"
    assert res.data == b"null\n"

    res = client.get("/items/AgedBrie?sell_in=0&quality=0")
    assert res.status_code == 200
    assert res.content_type == "application/json"
    assert json.loads(res.data) == {"name": "AgedBrie", "sell_in": 0, "quality": 0}

    res = client.get("/items/AgedBrie")
    data = json.loads(res.data)
    assert len(data) == 3
    assert res.status_code == 200
    assert res.content_type == "application/json"
