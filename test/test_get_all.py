import json


def test_get_all(client):
    res = client.get("/items")
    data = json.loads(res.data)
    assert res.status_code == 200
    assert res.content_type == "application/json"
    assert len(data) == 8
    assert set(["name", "sell_in", "quality"]) == set(data[0])
    assert data[0]["name"] is not None
    assert data[0]["sell_in"] >= 0
    assert data[0]["quality"] >= 0
