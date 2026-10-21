
class portfolio:
    def __init__(self, page):
        self.page = page

        # Navigation link to Portfolio page
        self.portfolio_link = page.locator('(//a[text()="Portfolio"])[1]')
        # self.portfolio_link = page.locator('(//a[@href="https://www.tranktechnologies.com/portfolio"])[1]')

        # Portfolio -> "View More" locators for each project card
        self.project_1_view_more = page.locator('(//a[contains(text(), "View More")])[1]')
        self.project_2_view_more = page.locator('(//a[contains(text(), "View More")])[2]')
        self.project_3_view_more = page.locator('(//a[contains(text(), "View More")])[3]')
        self.project_4_view_more = page.locator('(//a[contains(text(), "View More")])[4]')
        self.project_5_view_more = page.locator('(//a[contains(text(), "View More")])[5]')
        self.project_6_view_more = page.locator('(//a[contains(text(), "View More")])[6]')
        self.project_7_view_more = page.locator('(//a[contains(text(), "View More")])[7]')
        self.project_8_view_more = page.locator('(//a[contains(text(), "View More")])[8]')
        self.project_9_view_more = page.locator('(//a[contains(text(), "View More")])[9]')
        self.project_10_view_more = page.locator('(//a[contains(text(), "View More")])[10]')
        self.project_11_view_more = page.locator('(//a[contains(text(), "View More")])[11]')
        self.project_12_view_more = page.locator('(//a[contains(text(), "View More")])[12]')

        self.portfolio_view_more_list = [
            self.project_1_view_more,
            self.project_2_view_more,
            self.project_3_view_more,
            self.project_4_view_more,
            self.project_5_view_more,
            self.project_6_view_more,
            self.project_7_view_more,
            self.project_8_view_more,
            self.project_9_view_more,
            self.project_10_view_more,
            self.project_11_view_more,
            self.project_12_view_more,
        ]

        # Generic locator matching all "View More" buttons on the Portfolio page
        self.all_view_more = page.locator('//a[contains(text(), "View More")]')

    def portfolio_view_more_clicking(self):
        self.portfolio_link.click()
        self.page.wait_for_load_state("load")
        for i in self.portfolio_view_more_list:
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def all_portfolio_projects_clicking_dynamic(self):
        self.portfolio_link.click()
        self.page.wait_for_load_state("load")
        count = self.all_view_more.count()
        for index in range(1, count + 1):
            self.page.locator(f'(//a[contains(text(), "View More")])[{index}]').click()
            self.page.wait_for_load_state("load")
            self.page.go_back()