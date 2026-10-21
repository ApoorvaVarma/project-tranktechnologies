class footer:
    def __init__(self,page):
        self.page=page
        #footer
        #web developement
        # w = page.locator('//a[@href="https://www.tranktechnologies.com/web-development-company"]')
        # w.click()
        self.page.goto("https://www.tranktechnologies.com/")
        self.page.wait_for_load_state('load')
        self.cmsWD=page.locator('//a[@href="https://www.tranktechnologies.com/cms-website-development-company"]')
        self.eComDev=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[7]')
        self.cwpd=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company"])[1]')
        self.footer_l1=[self.cmsWD,self.eComDev,self.cwpd]


        self.uiux_title=page.locator('//a[@href="https://www.tranktechnologies.com/ui-ux-design-company"]')
        self.mobile=page.locator('//a[@href="https://www.tranktechnologies.com/mobile-app-design-company"]')
        self.resDesign=page.locator('//a[@href="https://www.tranktechnologies.com/responsive-web-design-company"]')
        self.brandIdentity=page.locator('//a[@href="https://www.tranktechnologies.com/brand-identity-design-services-company"]')
        self.footer_l2=[self.uiux_title,self.mobile,self.resDesign,self.brandIdentity]


        #footer-Add dev
        #aDco=page.locator('(//a[@href="https://www.tranktechnologies.com/app-development-company"])[2]')
        self.iosmobile=page.locator('//a[@href="https://www.tranktechnologies.com/ios-mobile-app-development-company"]')
        self.adroidmob=page.locator('//a[@href="https://www.tranktechnologies.com/android-mobile-app-development-company"]')
        self.hybrid=page.locator('//a[@href="https://www.tranktechnologies.com/hybrid-mobile-app-development-company"]')
        self.cross=page.locator('//a[@href="https://www.tranktechnologies.com/cross-platform-mobile-app-development-company"]')
        self.progressive=page.locator('//a[@href="https://www.tranktechnologies.com/progressive-web-app-development-company"]')
        self.footer_l3=[self.mobile,self.iosmobile,self.adroidmob,self.hybrid,self.cross,self.progressive,]


        #Footer-portfolio
        self.gD=page.locator('//a[@href="https://www.tranktechnologies.com/graphic-design-company"]')
        
        #graphicdesign=page.locator('//a[@href="/graphic-design-company-in-india"]')
        self.logo=page.locator('//a[@href="https://www.tranktechnologies.com/logo-design-company"]')
        self.banner=page.locator('//a[@href="https://www.tranktechnologies.com/banner-design-company"]')
        self.packdesign=page.locator('//a[@href="https://www.tranktechnologies.com/packaging-design-company"]')
        self.bussCards=page.locator('//a[@href="https://www.tranktechnologies.com/business-cards-design-company"]')
        self.footer_l4=[self.gD,self.logo,self.banner,self.packdesign,self.bussCards]


        
    def footer_click1(self):
        for i in self.footer_l1:
            i.click()
            self.page.wait_for_load_state('load')
            self.page.go_back()

    def footer_click2(self):
        for i in self.footer_l2:
            i.click()
            self.page.wait_for_load_state('load')
            self.page.go_back()

    def footer_click3(self):
        for i in self.footer_l3:
            i.click()
            self.page.wait_for_load_state('load')
            self.page.go_back()

    def footer_click4(self):
        for i in self.footer_l4:
            i.click()
            self.page.wait_for_load_state('load')
            self.page.go_back()