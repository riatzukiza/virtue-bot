from coffeebot import config, utils
from mattermostdriver import Driver


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

    team_name = config.TEAM_NAME
    channel_name = config.CHANNEL_NAME
    members = utils.get_channel_members(driver, team_name, channel_name)



if __name__ == '__main__':
    main()
