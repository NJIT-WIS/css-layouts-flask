""" Write your test for the task here"""
# pylint: disable=redefined-outer-name, unused-argument


def test_task2(client):
    """This tests if there is the test 'about page' on the about page"""
    response = client.get("/")
    assert response.status_code == 200
    response = client.get("/about")
    assert response.status_code == 200
    response = client.get("/portfolio")
    assert response.status_code == 200
    response = client.get("/contact")
    assert response.status_code == 200
