import json


def check_header(res, data):
    assert res.status_code == 200
    assert res.content_type == "application/json"
    assert set(["name", "sell_in", "quality"]) == set(data[0])


def check_response_data(data, ln, name, sell_in=0, quality=0):
    assert len(data) == ln
    assert data[0]["name"] == name
    assert data[0]["sell_in"] >= sell_in
    assert data[0]["quality"] >= quality


def test_get_item_by_agedbrie(client):
    res = client.get("/items/AgedBrie")
    data = json.loads(res.data)
    check_header(res, data)
    check_response_data(data, 3, "AgedBrie")


def test_get_item_by_sulfuras(client):
    res = client.get("/items/Sulfuras")
    data = json.loads(res.data)
    check_header(res, data)
    check_response_data(data, 2, "Sulfuras")


def test_get_item_filter_by_quality(client):
    res = client.get("/items/AgedBrie?quality=0")
    data = json.loads(res.data)
    check_header(res, data)
    check_response_data(data, 2, "AgedBrie")

    res = client.get("/items/Sulfuras?quality=0")
    data = json.loads(res.data)
    check_header(res, data)
    check_response_data(data, 2, "Sulfuras")


def test_get_item_filter_by_sellin(client):
    res = client.get("/items/BackstagePass?sell_in=5")
    data = json.loads(res.data)
    check_header(res, data)
    check_response_data(data, 1, "BackstagePass", 5)

    res = client.get("/items/AgedBrie?sell_in=7")
    data = json.loads(res.data)
    check_header(res, data)
    check_response_data(data, 1, "AgedBrie", 7)
