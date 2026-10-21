import pytest
from pages.contact_us import contact_us


@pytest.mark.smoke
def test_free_consultation_form_filling(page):
    obj=contact_us(page)
    obj.free_consultation_form_filling("Apoorva","apoorva@gmail.com","7465554544","4566","Google","Infra","Web Development")

