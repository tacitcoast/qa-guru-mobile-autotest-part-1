from appium.options.ios import XCUITestOptions
import pytest
from selene import browser
import os
import config
from utils import attach
from appium import webdriver


@pytest.fixture(scope='function', autouse=True)
def ios_mobile_management():
    options = XCUITestOptions().load_capabilities({

        "app": config.settings.ios_app_url,

        "deviceName": config.settings.ios_device,
        "platformName": config.settings.ios_platform,
        "platformVersion": config.settings.ios_version,


        "bstack:options": {
            "userName": config.settings.browserstack_username,
            "accessKey": config.settings.browserstack_key,
            "projectName": config.settings.project_name,
            "buildName": config.settings.build_name,
            "sessionName": config.settings.session_name
    }
})

    browser.config.driver = webdriver.Remote(config.settings.browserstack_url, options=options)

    browser.config.timeout = float(os.getenv('timeout', '10.0'))
    yield
    attach.allure_attach_bstack_screenshot()
    browser.quit()
