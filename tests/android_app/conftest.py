from time import sleep

import pytest
from appium.options.android import UiAutomator2Options

from appium import webdriver
from selene import browser
import os
import config
from utils import attach


@pytest.fixture(scope='function', autouse=True)
def android_mobile_management():
    options = UiAutomator2Options().load_capabilities({

        'platformName': config.settings.android_platform,
        'platformVersion': config.settings.android_version,
        'deviceName': config.settings.android_device,

        'app': config.settings.app_url,

        'bstack:options': {
            'projectName': config.settings.project_name,
            'buildName': config.settings.build_name,
            'sessionName': config.settings.session_name,

            'userName': config.settings.browserstack_username,
            'accessKey': config.settings.browserstack_key
        }
    })

    browser.config.driver = webdriver.Remote(config.settings.browserstack_url, options=options)

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    attach.allure_attach_bstack_screenshot()

    session_id = browser.driver.session_id
    attach.allure_attach_bstack_video(session_id)
    browser.quit()