from app import app

def test_home():
    response = app.test_client().get('/')
    # Verify the application successfully returns a 200 OK status
    assert response.status_code == 200
    # Verify the core UI elements rendered correctly
    assert b"Infrastructure Operations" in response.data
    assert b"sohamdocker25" in response.data
    assert b"Soham Sarkar" in response.data
