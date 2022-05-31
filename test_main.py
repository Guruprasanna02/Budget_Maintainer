from fastapi.testclient import TestClient

import main

app = main.app

client = TestClient(app)


def test_read_main():
	response = client.post("/users/", json={"name": "test", "income": 85000})
	assert response.status_code == 200
	assert response.json() == {"name":"test","id":1,"income":85000,"balance":85000}

	response = client.get("/users")
	assert response.status_code == 200
	assert response.json() == [{"name":"test","id":1,"income":85000,"balance":85000}]

	response = client.get("/users/1")
	assert response.status_code == 200
	assert response.json() == {"name":"test","id":1,"income":85000,"balance":85000}

	response = client.get("/users/2")
	assert response.status_code == 404
	assert response.json() == {"detail":"User not found"}

	response = client.post("/expense/", json={"name": "test", "expense": 5000})
	assert response.status_code == 200
	assert response.json() == {"name":"test","id":1,"income":85000,"balance":80000}

	response = client.post("/expense/", json={"name": "test", "expense": 200})
	assert response.status_code == 200
	assert response.json() == {"name":"test","id":1,"income":85000,"balance":79800}