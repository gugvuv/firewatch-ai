def test_health(client):
    r = client.get("/api/v1/health")
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "ok"
    assert "timestamp" in body


def test_data_status(client):
    r = client.get("/api/v1/system/data-status")
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "ok"
    assert "sources" in body
    assert "checked_at" in body
