""" Do not change these tests, or I will fail you for cheating"""

# pylint: disable=redefined-outer-name, unused-argument
import os
from os.path import exists
from app.config import Config


def test_task1_site_folders_and_files_exist():
    """This the site files exist"""

    assert exists(os.path.join(Config.BASE_DIR, "templates"))
    assert exists(os.path.join(Config.BASE_DIR, "templates", "index.html"))
    assert exists(os.path.join(Config.BASE_DIR, "templates", "base.html"))
    assert exists(os.path.join(Config.BASE_DIR, "templates", "portfolio.html"))
    assert exists(os.path.join(Config.BASE_DIR, "templates", "about.html"))
    assert exists(os.path.join(Config.BASE_DIR, "templates", "contact.html"))
    assert exists(os.path.join(Config.BASE_DIR, "static"))
    assert exists(os.path.join(Config.BASE_DIR, "static", "css"))
    assert exists(os.path.join(Config.BASE_DIR, "static", "css", "style.css"))
