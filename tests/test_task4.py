""" Write your test for the task here"""


# pylint: disable=redefined-outer-name, unused-argument


def test_task4(client):
    """This tests if there is the test 'about page' on the about page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<h1>Home</h1>' in response.data
    assert b'<p>' in response.data

    page_links_and_copyright(response)

    response = client.get("/about")
    assert response.status_code == 200
    assert b'<h1>About</h1>' in response.data
    assert b'<p>' in response.data
    page_links_and_copyright(response)

    response = client.get("/portfolio")
    assert response.status_code == 200
    assert b'<h1>Portfolio</h1>' in response.data
    assert b'<p>' in response.data
    page_links_and_copyright(response)


def page_links_and_copyright(response):
    """Checks the sites main menu links"""

    assert b'<link rel="stylesheet"' in response.data
    assert b'<menu>' in response.data
    assert b'<li><a href="/">Home</a> </li>' in response.data
    assert b'<li><a href="/about">About</a> </li>' in response.data
    assert b'<li><a href="/portfolio">Portfolio</a> </li>' in response.data
    assert b'Copyright' in response.data
