""" Write your test for the task here"""
# pylint: disable=redefined-outer-name, unused-argument


def test_task3(client):
    """Testing that pages have the correct information"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data
    response = client.get("/about")
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data
    response = client.get("/portfolio")
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data
    response = client.get("/contact")
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data
    response = client.get("/static/css/style.css")
    assert response.status_code == 200
    assert b'.column_2' in response.data
