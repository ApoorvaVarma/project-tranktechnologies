class contact_us:
    def __init__(self, page):
        self.page = page

        # Navigation link to Contact Us page
        self.contact_us_link = page.locator('(//a[text()="Contact us"])[1]')
        # self.contact_us_link = page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')

        # "Get a Free Consultation" Form Locators
        # Note: Index [2] targets the on-page "Get a free consultation" form
        # (Index [1] is the hidden "GET IN TOUCH" header modal form in the DOM)
        self.your_name = page.locator('(//input[@placeholder="Your Name"])[2]')
        # self.your_name = page.locator('(//input[@name="name"])[2]')

        self.your_email = page.locator('(//input[@placeholder="Your Mail"])[2]')
        # self.your_email = page.locator('(//input[@name="email"])[2]')

        self.your_phone = page.locator('(//input[@placeholder="Your Phone"])[2]')
        # self.your_phone = page.locator('(//input[@name="phone"])[2]')

        self.send_otp = page.locator('(//button[contains(text(), "Send OTP")])[2]')
        # self.send_otp = page.locator('(//a[contains(text(), "Send OTP")])[2]')

        self.enter_otp = page.locator('(//input[@placeholder="Enter OTP"])[2]')
        # self.enter_otp = page.locator('(//input[@name="otp"])[2]')

        self.your_company = page.locator('(//input[@placeholder="Your Company"])[2]')
        # self.your_company = page.locator('(//input[@name="company"])[2]')

        # "Choose a Service" Dropdown & Options
        # Options: "Web Development", "App Development", "UI / UX Design",
        #          "Graphic Design", "Digital Marketing", "Business Listing", "Others"
        self.choose_service = page.locator('(//select[@name="service"])[2]')
        # self.choose_service = page.locator('(//select[option[contains(text(), "Choose a Service")]])[2]')

        self.your_message = page.locator('(//textarea[@placeholder="Your Message"])[2]')
        # self.your_message = page.locator('(//textarea[@name="message"])[2]')

        self.submit_btn = page.locator('(//input[@type="submit"])[2]')
        # self.submit_btn = page.locator('(//button[@type="submit"])[2]')

    def free_consultation_form_filling(
        self, name, email, phone, otp, company, message
    ):
        self.contact_us_link.click()
        self.page.wait_for_load_state("load")
        self.your_name.fill(name)
        self.your_email.fill(email)
        self.your_phone.fill(phone)
        self.send_otp.click()
        self.enter_otp.fill(otp)
        self.your_company.fill(company)
        self.choose_service.select_option(label="Web Development")
        self.your_message.fill(message)
        self.submit_btn.click()
        self.page.wait_for_load_state("load")

