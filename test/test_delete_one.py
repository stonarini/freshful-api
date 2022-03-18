import json


def test_create_one(client):
    res = client.delete("/items/AgedBrie?sell_in=7&quality=0")
    assert res.status_code == 200
    assert res.content_type == "application/json"
    assert res.data == b"null\n"

    res = client.get("/items/AgedBrie?sell_in=7&quality=0")
    assert res.status_code == 200
    assert res.content_type == "application/json"
    assert res.data == b"null\n"


def test_create_one_default_values(client):
    num_items = len(json.loads(client.get("/items/AgedBrie").data))

    res = client.delete("/items/AgedBrie")
    assert res.status_code == 200
    assert res.content_type == "application/json"
    assert res.data == b"null\n"

    res = client.get("/items/AgedBrie")
    data = json.loads(res.data)
    assert res.status_code == 200
    assert res.content_type == "application/json"
    assert len(data) == num_items - 1
