import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session, create_engine
from sqlmodel.pool import StaticPool
from api.main import app
from api.database import get_session


@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


def test_create_and_get_user(client: TestClient):
    # Test User Registration (201 Created)
    response = client.post("/users", json={"name": "Alice Smith", "email": "alice@example.com"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Alice Smith"
    assert data["email"] == "alice@example.com"
    user_id = data["id"]

    # Test User Retrieval (200 OK)
    get_res = client.get(f"/users/{user_id}")
    assert get_res.status_code == 200
    assert get_res.json()["email"] == "alice@example.com"


def test_duplicate_email_conflict(client: TestClient):
    client.post("/users", json={"name": "Bob", "email": "bob@example.com"})
    res = client.post("/users", json={"name": "Bob Duplicate", "email": "bob@example.com"})
    assert res.status_code == 409
    assert "already exists" in res.json()["detail"]


def test_get_nonexistent_user_404(client: TestClient):
    res = client.get("/users/9999")
    assert res.status_code == 404
