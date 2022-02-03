from mattermostdriver import Driver

import config
import utils


def main():
    print("Creating Mattermost Driver...")
    driver_options = {
        'url': config.URL,
        'login_id': config.USERNAME,
        'password': config.PASSWORD,
        'port': config.PORT,
        'token': config.PASSWORD,
        'scheme': 'https',
        'port': 443,
        'verify': True,
        'auth': None,
        'timeout': 30,
        'request_timeout': None,
        'debug': False
    }
    driver = Driver(driver_options)

    driver.login()
    driver.users.get_user('me')

    channel_name = config.CHANNEL_NAME
    utils.post_quote(driver, channel_name)




if __name__ == '__main__':
    main()
