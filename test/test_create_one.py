import json


def test_create_one(client):
    res = client.put("/items/TestItem?sell_in=10&quality=10")
    assert res.status_code == 200
    assert res.content_type == "application/json"
    assert res.data == b"null\n"

    res = client.get("/items/TestItem?sell_in=10&quality=10")
    assert res.status_code == 200
    assert res.content_type == "application/json"
    assert json.loads(res.data) == {"name": "TestItem", "sell_in": 10, "quality": 10}

    res = client.get("/items/TestItem")
    data = json.loads(res.data)
    assert len(data) == 1
    assert res.status_code == 200
    assert res.content_type == "application/json"
    assert data == [{"name": "TestItem", "sell_in": 10, "quality": 10}]


def test_create_one_default_values(client):
    res = client.put("/items/TestItem")
    assert res.status_code == 200
    assert res.content_type == "application/json"
    assert res.data == b"null\n"

    res = client.get("/items/TestItem?sell_in=0&quality=0")
    assert res.status_code == 200
    assert res.content_type == "application/json"
    assert json.loads(res.data) == {"name": "TestItem", "sell_in": 0, "quality": 0}
