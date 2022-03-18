import json


def test_get_inexistent_routes(client):
    res = client.get("/item/")
    assert res.status_code == 404
    assert res.content_type == "application/json"

    res = client.get("/AgedBrie/")
    assert res.status_code == 404
    assert res.content_type == "application/json"


def test_invalid_properties(client):
    res = client.get("/items/AgedBrie?quality=quality&sell_in=sell_in")
    assert res.status_code == 400
    assert res.content_type == "application/json"
    assert (
        res.data
        == b'{"message": "The browser (or proxy) sent a request that this server could not understand."}\n'
    )


def test_incorrect_properties(client):
    res = client.get("/items/AgedBrie?price=10")
    assert res.status_code == 400
    assert res.content_type == "application/json"
    assert (
        res.data
        == b'{"message": "The browser (or proxy) sent a request that this server could not understand."}\n'
    )
