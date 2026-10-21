import pytest
from pages.footer import footer

@pytest.mark.smoke
def test_footer_click1(page):
    obj=footer(page)
    obj.footer_click1()

@pytest.mark.smoke
def test_footer_click2(page):
    obj=footer(page)
    obj.footer_click2()


@pytest.mark.smoke
def test_footer_click3(page):
    obj=footer(page)
    obj.footer_click3()

@pytest.mark.smoke
def test_footer_click4(page):
    obj=footer(page)
    obj.footer_click4()
