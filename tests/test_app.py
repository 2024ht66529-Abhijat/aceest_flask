import pytest
from app import create_app

def test_home_page():
    app = create_app()
    app.testing = True
    client = app.test_client()
    res = client.get('/')
    assert res.status_code == 200