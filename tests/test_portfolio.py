import pytest

from pages.portfolio import portfolio


@pytest.mark.smoke
def test_portfolio_view_more_clicking(page):
    obj=portfolio(page)
    obj.portfolio_view_more_clicking()



@pytest.mark.smoke
def test_all_portfolio_projects_clicking_dynamic(page):
    obj=portfolio(page)
    obj.all_portfolio_projects_clicking_dynamic()