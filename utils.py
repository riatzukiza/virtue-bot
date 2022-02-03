import random


def get_channel(driver, team_name, channel_name):
    """
    Retrieve a channel given a team and channel name.
    Returns the JSON response from the Mattermost API.
    """
    response = driver.channels.get_channel_by_name_and_team_name(
        team_name, channel_name)
    return response


def get_channel_members(driver, team_name, channel_name):
    """
    Retrieve all of the members from a channel given a team and channel name.
    Returns a list of user IDs sorted alphabetically.
    """
    channel = get_channel(driver, team_name, channel_name)
    channel_id = channel['id']

    # By default, the Mattermost API will return only 60 members. Set this to
    # an amount that is at least the number of members in the channel to get
    # all members
    params = {
        'per_page': '10000'
    }
    response = driver.channels.get_channel_members(channel_id, params=params)

    bot = driver.users.get_user('me')
    bot_id = bot['id']

    # Return all of the user IDs excluding the bot's user ID (don't want to
    # count the bot as a user in pairings)
    members = [
        member['user_id'] for member in response if (
            member['user_id'] != bot_id)]

    # Sort the member list alphabetically so that when we create pairs in the
    # database using the list, we won't create duplicate pairs (A <-> B is the
    # same as B <-> A)
    members.sort()

    return members

def select_quote():
    with open("./mediations.sentances.txt") as sentances:
        line = random.choice(sentances.readlines())
        return line


def post_quote(driver, channel_id):
    message_options = {
        "channel_id": channel_id,
        "message": select_quote()
    }

    response = driver.posts.create_post(message_options)
    return response
