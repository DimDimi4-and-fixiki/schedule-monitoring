def test_ping(client):
    resp = client.get('/api/v1/ping')
    resp.raise_for_status()
    assert resp.json()
