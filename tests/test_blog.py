import pytest

from pages.blog import blog


@pytest.mark.smoke
def test_blog(page):
    obj=blog(page)
    obj.blog_clicking()