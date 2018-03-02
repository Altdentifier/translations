class Strings:
    time_at = "at"

    #;setup
    start_setup =  "You have started bot setup, to begin, first, do you want to enable alt and spambot indentification. You can still use manual verification with the `;force` command."
    true_or_false = "Type `True` or `False`"
    altdentification_set_to = "Altdentification set to "
    enter_administrator = "\nIf you have a role for humans, please enter its id now.\nIf you do not or do not want the human role to be taken away when it has been assigned by another bot, enter a 0\n"
    to_retrieve = "\nA list of roles is provided for your convenience.\nIf your config is incorrect, please use the ;info command to find my support server.\n"
    setup_human_disabled = "Human role disabled. Do you wish to enable logging features? \nIf yes, enter `True`, if you do not, enter `False`"
    human_received_1 = "Human role <@&"
    human_received_2 = "> received.\n\nDo you wish to enable logging features?\nIf yes, enter `True`, if you do not, enter `False`"
    enable_logging = "Do you wish to enable logging features?\nIf yes, enter `True`, if you do not, enter `False`"
    enter_logging = "Please mention your logging channel. Make sure to put a `#` (pound/hashtag) sign in front of the name, so that the link shows up blue. (Channel ID's are also supported.)"
    logging_received_1 = "<#"
    logging_received_2 = "> set to logging channel."
    logging_received_3 = " set to logging channel."
    enter_general = "Please mention your general channel. Make sure to put a `#` (pound/hashtag) sign in front of the name, so that the link shows up blue. (Channel ID's are also supported.)\nIf the bot cannot send the DM, the user will be mentioned here, so they can turn on DM's from server members."
    general_received = "> set to general channel.\n\nPlease mention your bot channel, this should be hidden, as messages from the bot will containt a bypass code, that when entered by the user grant immediate passage from the system. Make sure to put a `#` (pound/hashtag) sign in front of the name, so that the link shows up blue. (Channel ID's are also supported)"
    enter_bot_channel = " set to general channel.\n\nPlease mention your bot channel, this should be hidden, as messages from the bot will containt a bypass code, that when entered by the user grant immediate passage from the system. Make sure to put a `#` (pound/hashtag) sign in front of the name, so that the link shows up blue. (Channel ID's are also supported)"
    setup_complete_1 = "<#"
    setup_complete_2 = "> set to bot channel.\nSetup is now complete"
    setup_complete_3 = " set to bot channel.\nSetup is now complete"
    could_not_retrieve= "Sadly, we could not retrieve a list of roles. You should use a roleinfo command, like Dyno's ?roleinfo. This must be done in a different channel, otherwise it will be regarded as input."
    if_in_setup = 'Setup is already active on this server. Setup will be available after 10 minutes, in the case of a fatal error.'

    #;info
    info_description = "Spambot and Alt detection, fighting and general logging bot. Profile picture by Mozilla, <https://github.com/mozilla/fxemoji>"

    #;settings
    settings_embed_title = "Settings"
    settings_no = "The request has been cancelled."
    setup_description_1 = "1. Enable Altdentification\n2. Admin Role\n3. Mod Role\n4. Human Role\n5. Logging\n6. General Channel\n7. Bot Channel\n8. Language\n9. Prefix\n10. Timezone\n11. Minimum account age\n12. Autorole\n13. Authentication Methods\n14. Timeout Action\n15. Log Channel\n16. Log Options\nType number of the option you require.\nType `exit` to stop."
    setup_description_2 = "1. Enable Altdentification\n2. Admin Role\n3. Mod Role\n4. Human Role\n5. Logging\n6. General Channel\n7. Bot Channel\n8. Language\n9. Prefix\n10. Timezone\n11. Minimum account age\n12. Autorole\n13. Authentication Methods\n14. Timeout Action\nType number of the option you require.\nType `exit` to stop"
    settings_one_1 = "Altdentification is currently set to: "
    settings_one_2 = ". Do you wish to change it? Type `Yes`, otherwise type `No` to cancel."
    settings_one_3 = "Enter `True` to enable altdentification, or `False` to disable it."
    settings_one_4 = "Succes! Altdentification has been set to: "
    settings_two_1 = "The current admin role is: <@&"
    settings_two_2 = ">. Do you wish to change it? Type `Yes`, otherwise type `No` to cancel."
    settings_two_3 = "Enter the id of the new admin role."
    settings_two_4 = "Succes! The admin role has been set to: <@&"
    settings_two_5 = "You have not entered a number. Role ID's should always be numbers.\nPlease enter the correct ID now, or enter a 0 to disable it."
    settings_two_6 = "You have entered an incorrect number two times in a row. Exiting configuration..."
    settings_three_1 = "The current mod role is: <@&"
    settings_three_2 = ">. Do you wish to change it? Type `Yes`, otherwise type `No` to cancel."
    settings_three_3 = "Enter the id of the new mod role."
    settings_three_4 = "Succes! The mod role has been set to: <@&"
    settings_four_1 = "The current human role is: <@&"
    settings_four_2 = ">. Do you wish to change it? Type `Yes`, otherwise type `No` to cancel."
    settings_four_3 = "Enter the id of the new human role."
    settings_four_4 = "Succes! The human role has been set to: <@&"
    settings_five_1 = "Logging is currently set to: "
    settings_five_2 = ". Do you wish to change it? Type `Yes`, otherwise type `No` to cancel."
    settings_five_3 = "Enter `True` to enable logging, or `False` to disable it."
    settings_five_4 = "Succes! Logging has been set to: "
    settings_five_5 = "Enter the id of the new logging channel."
    settings_five_6 = "Succes! The logging channel has been set to: <#"
    settings_six_1 = "The general channel is currently set to: <#"
    settings_six_2 = ">. Do you wish to change it? Type `Yes`, otherwise type `No` to cancel."
    settings_six_3 = "Enter the id of the new general channel, or mention it."
    settings_six_4 = "Succes! The general channel has been set to: <#"
    settings_six_5 = "Succes! The general channel has been set to: "
    settings_seven_1 = "The bot channel is currently set to: <#"
    settings_seven_2 = ">. Do you wish to change it? Type `Yes`, otherwise type `No` to cancel."
    settings_seven_3 = "Enter the id of the new bot channel, or mention it."
    settings_seven_4 = "Succes! The bot channel has been set to: <#"
    settings_seven_5 = "Succes! The bot channel has been set to: "
    settings_eight_1 = "The logging channel is currently set to: <#"
    settings_eight_2 = ">. Do you wish to change it? Type `Yes`, otherwise type `No` to cancel."
    settings_eight_3 = "Enter the id of the new logging channel, or mention it."
    settings_eight_4 = "Succes! The logging channel has been set to: <#"
    settings_eight_5 = "Succes! The logging channel has been set to: "
    settings_nine_1 = "Language currently set to: "
    settings_nine_2 = ". Do you wish to change it? Type `Yes`, otherwise type `No` to cancel."
    settings_nine_3 =  "Enter a language code.\nSupported languages: `en` for English\n`nl` for Dutch\n`fr` for French or `it` for Italian."
    settings_nine_4 = "Succes! Language has been set to: "
    settings_ten_1 = "Prefix currently set to: `"
    settings_ten_2 = "`. Do you wish to change it? Type `Yes`, otherwise type `No` to cancel."
    settings_ten_3 = "Enter the new prefix."
    settings_ten_4 = "Succes! Prefix has been set to: `"
    settings_eleven_1 = "Timezone currently set to: UTC/GMT + "
    settings_eleven_2 = "\nDo you wish to change it? Type `Yes`, otherwise type `No` to cancel."
    settings_eleven_3 = "Enter the difference in hours between your timezone and GMT. For example, for CEST enter `1`"
    settings_eleven_4 = "Succes! Timezone has been set to: UTC/GMT + "
    settings_twelve_1 = "Minimum account age currently set to: "
    settings_twelve_2 = "\nDo you wish to change it? Type `Yes`, otherwise type `No` to cancel."
    settings_twelve_3 = "Enter the age the account must be younger than to be verified in days. If you want all users to be verified, use a 0."
    settings_twelve_4 = "Succes! Minimum account age has been set to: "
    settings_thirteen_1 = "Autorole currently set to: `"
    settings_thirteen_2 = "`\nDo you wish to change it? Type `Yes`, otherwise type `No` to cancel."
    settings_thirteen_3 = "To enable autorole, type `True`. To disable, type `False`. "
    settings_thirteen_4 = "Succes! Autorole has been set to: `"
    settings_fourteen_1 = "Enter the name of the authentication method you want to toggle.\nWe support the following methods: `Overwatch`, `Reddit`, `Twitter`, `Captcha` and `Steam`\n\nThe following methods are enabled on this guild: "
    settings_fourteen_2 = "Reddit disabled"
    settings_fourteen_3 = "Steam disabled"
    settings_fourteen_4 = "Twitter disabled"
    settings_fourteen_5 = "Reddit enabled"
    settings_fourteen_6 = "Steam enabled"
    settings_fourteen_7 = "Twitter enabled"
    settings_fourteen_8 = "You need to have at least one authentication method active"
    settings_fourteen_9 = "\nType `exit` to stop"
    settings_fourteen_10 = "Overwatch enabled"
    settings_fourteen_11 = "Overwatch disabled"
    settings_fourteen_12 = "Captcha enabled"
    settings_fourteen_13 = "Captcha disabled"
    settings_fifteen_1 = "Enter the name of the log option you want to toggle.\nWe support the following items to log:\n`MEMBER JOIN`, `MESSAGE DELETE`, `MESSAGE EDIT`, `CHANNEL CREATE`, `CHANNEL DELETE`, `CHANNEL UPDATE`, `MEMBER LEAVE/KICKED`, `MEMBER BANNED`, `MEMBER UNBANNED`, `ROLE CREATE`, `ROLE EDITED`, `ROLE DELETE`, `GUILD UPDATE`, `MEMBER UPDATE`, `VOICE STATE UPDATE`.\nThe following methods are enabled on this guild:\n "
    settings_fifteen_2 = " enabled"
    settings_fifteen_3 = " disabled"
    settings_sixteen_1 = "Choose an option that you want to be used on people who do not respond to the bot. You can send `kick` to kick them, `role` to give them a role, you can set this afterwards or `nothing` to do nothing."
    settings_sixteen_2 = "Timeout action set to `kick`. Members that do not respond to the bot will be kicked."
    settings_sixteen_3 = "Timeout action set to `nothing`. Nothing will happen to members that do not respond to the bot."
    settings_sixteen_4 = "Timeout action set to `role. Please enter the full name of the role that you want to give them."
    settings_sixteen_5 = "This role could not be found. Your timeout action has been reverted to default. (kick)"
    settings_sixteen_6 = "The following role will be given if a user does not respond to the bot: '"
    in_settings = "Settings are already open on this server."

    #on_member_join
    on_member_join_1 = 'Member joined'

    #on_message_delete
    message_deleted_1 = '**Message from <@'
    message_deleted_2 = '> deleted in <#'

    #on_message_edit
    #message_deleted_1 = '**Message from <@'
    on_message_edit_1 = '> edited in <#'
    on_message_edit_2 = 'Before'
    on_message_edit_3 = 'After'

    #on_channel_create
    on_channel_create_1 = 'Channel added'
    on_channel_create_2 = '\n**Topic:**\n'

    #on_channel_delete
    on_channel_delete_1 = 'Channel deleted'
    #on_channel_create_2 = '\n**Topic:**\n'

    #on_channel_update
    on_channel_update_1 = '**Channel <#'
    on_channel_update_2 = '> edited**'
    #on_message_edit_2 = 'Before'
    #on_message_edit_3 = 'After'
    on_channel_update_3 = '**Name:** '
    on_channel_update_4 = '\n**Topic:** '
    on_channel_update_5 = "Voice Channel"
    on_channel_update_6 = "Category"

    #on_member_remove
    on_member_remove_1 = 'Person left/kicked'

    #on_member_ban
    on_member_ban_1 = 'Person banned'

    #on_member_unban
    on_member_unban_1 = 'Person unbanned'

    #on_server_role_create
    on_server_role_create_1 = 'Role "'
    on_server_role_create_2 = '" created'
    on_server_role_create_3 = '**Name: **<@&'
    on_server_role_create_4 = '>\n**Color:** '
    on_server_role_create_5 = '\n**Hoisted:** '
    on_server_role_create_6 = '\n**Mentionable:** '

    #on_server_role_delete
    #inherit role_create
    on_server_role_delete_1 = '" deleted'
    on_server_role_delete_2  = '**Name:** '
    on_server_role_delete_3 = '\n**Color:** '

    #on_server_role_update
    on_server_role_update_1 = '" edited'
    #on_message_edit_2 = 'Before'
    #on_message_edit_3 = 'After'

    #on_server_update
    on_server_update_1 = 'Server edited'
    # on_message_edit_2 = 'Before'
    # on_message_edit_3 = 'After'
    on_server_update_2 ='\n**Region: **'
    on_server_update_3 = '\n**Member count: **'
    on_server_update_4 = '\n**Channel count: **'
    on_server_update_5 = '\n**Owner: **'

    #on_member_update
    on_member_update_1 = '**Role <@&'
    on_member_update_2 = '> given**'
    on_member_update_3 = '> taken**'
    on_member_update_4 = '**Nickname changed**'
    on_member_update_5 = '**Nickname: **'

    #check_age
    check_age_1 = "Suspicious account detected"
    check_age_2 = ' has an account that is less than your minimum age requirement, or has been identified as a spambot, spammer or ban-evader.\n\n'
    check_age_3 = ' has entered the server at '
    check_age_4 = ', but the account was made on '
    check_age_5 = '.\n\nThe bot has initiated the authentication process.'
    check_age_6 = 'Hello '
    check_age_7 = ',\n\nWelcome to '
    check_age_8 = '. The server administrators have setup extra defenses, in their defense against spambots and alternate accounts. Unfortunately, your account was flagged as suspicious by our system, or a moderator has manually initiated a check on your account.\n\nIf the automatic process clears your account, you are free to engage in the server. If you do not make it, your account will be removed from the server.\nIn the case of failure, administrators will be able to override the system.\n\nKind regards,\n\nThe '
    check_age_9 = ' modteam.'
    check_age_10 = '\n\nYou have 10 minutes to respond to this message, and 5 minutes for every follow-up question.\nPlease type the name of the authentication method you wish to use.\nThe following authentication methods are available: '
    check_age_11 = '>, Your account is blocking private messages from members in this server. Please enable direct messages. You will receive a new message in 1 minute.'
    check_age_12 = ' kicked for not responding.'
    check_age_13 = 'Sadly, you have not responded to me in the alotted time.\nYou have been kicked from the server'
    check_age_14 = "ADDENDUM: Your account has been found in our list of Verified Spambots. If you believe this is in error, please appeal in our support server."
    check_age_15 = "WARNING! THIS USER HAS BEEN FOUND IN OUR LIST OF VERIFIED SPAMBOTS. IT IS RECOMMENDED YOU BAN THIS USER IMMEDIATELY."
    check_age_16 = "WARNING! This user has been found in our list of spam accounts, but this user is a human."
    check_age_17 = "WARNING! This user is a possible ban-evader!"
    check_age_18 = "ADDENDUM: Your account has been found in our list of possible ban evaders. If you believe this is in error, please appeal in our support server."
    check_age_19 = "ADDENDUM: Your account has been found in our list of advertising users. If you believe this is in error, please appeal in our support server."
    check_age_20 = "A moderator has allowed your account to bypass verification."
    check_age_21 = "\nBypass Code: "
    check_age_22 = "The Reddit verification method is not enabled on this guild. Please use another option"
    check_age_23 = "The Steam verification method is not enabled on this guild. Please use another option"
    check_age_24 = "The Twitter verification method is not enabled on this guild. Please use another option"
    check_age_25 = "The Overwatch verification method is not enabled on this guild. Please use another option"
    check_age_26 = ' given role for not responding: '
    check_age_27 = ' did not respond. Nothing was done.'
    check_age_28 = 'Sadly, you have not responded to me in the alotted time.\nWhat will happen, is up to the moderators.'
    check_age_29 = 'Sadly, you have not responded to me in the alotted time.\nYou have been given the following role: '
    check_age_30 = " has been allowed to skip verification by a moderator on your server."
    check_age_31 = "The Captcha verification method is not enabled on this guild. Please use another option."
    check_age_32 = ' is already being verified. Verification for this user will unlock after 30 minutes in the case of a fatal error.'

    #on_reddit
    on_reddit_1 = 'How do I verify my account? Add your Reddit account to your Discord profile and press the following link: \n<https://altdentifier.xyz/authenticate?user_id='
    on_reddit_16 = '>\nYour account will be automatically checked. Failing to authorize within 5 minutes means verification will fail.\n\nBy authenticating, you agree with our TOS. View it here: <https://altdentifier.xyz/tos>'
    on_reddit_2 = 'The authentication code was incorrect. Restarting...'
    on_reddit_3 = 'Username: '
    on_reddit_4 = '\nLink Karma: '
    on_reddit_5 = '\nComment Karma: '
    on_reddit_6 = '\nAccount age: '
    on_reddit_7 = "This was a demonstration of the bots features. No data has been sent to the server moderators."
    on_reddit_8 = 'Your account has passed verification. The API connection has been deleted, so that attackers cannot use your code to gain information.'
    on_reddit_9 = 'Your Reddit account was not deemed adequate for verification.\nThe API connection has been deleted, so that attackers cannot use your code to gain information.\n\nType `retry` to retry, or to choose a different method of authentication.\nType `manual` to alert moderators of the failure, so that they can look into it.\nNot responding in 5 minutes results in a kick.'
    on_reddit_10 = '@here Manual assistance required for <@'
    on_reddit_11 = 'You have not added a Reddit account to your Discord profile. Problems? Type `manual`.\nThe API connection has been deleted, so that attackers cannot use your code to gain information.\n\nType `retry` to retry, or to choose a different method of authentication.\nType `manual` to alert moderators of the failure, so that they can look into it.\nNot responding in 5 minutes results in a kick.'
    on_reddit_12 = 'Guild list:'
    on_reddit_13 = ' has chosen the Reddit method'
    on_reddit_14 = " has passed verification."
    on_reddit_15 = " did not pass verification."
    on_reddit_17 = " attempted to verify with another user's token. The token belongs to: "
    on_reddit_18 = " encountered an error during verification. User is requested to choose another method."
    on_reddit_19 = " attempted to verify with an invalid token or did not complete authentication. User is requested to choose another method."

    #opnieuw
    opnieuw_1 = 'The following authentication methods are available: '
    opnieuw_2 = '\n\nYou have 10 minutes to respond to this message, and 5 minutes for every follow-up question.'

    #on_steam
    on_steam_1 = 'How do I verify my account? Add your Steam account to your Discord profile and press the following link: \n<https://www.altdentifier.xyz/authenticate?user_id='
    on_steam_12 = '>. Your account will be automatically checked. Failing to authorize within 5 minutes means verification will fail.\n\nBy authenticating, you agree with our TOS. View it here: <https://altdentifier.xyz/tos>'
    on_steam_2 = "%d days, %d hours, %d minutes and %d seconds"
    on_steam_3 = 'Name: '
    on_steam_4 = '\nTotal Games (with playtime): '
    on_steam_5 = '\nTotal Playtime: '
    on_steam_6 = 'Your Steam account was not deemed adequate for verification.\nThe API connection has been deleted, so that attackers cannot use your code to gain information.\n\nType `retry` to retry, or to choose a different method of authentication.\n `manual` to alert moderators of the failure, so that they can look into it.\nNot responding in 5 minutes results in a kick.'
    on_steam_7 = '\nLink: http://steamcommunity.com/profiles/'
    on_steam_8 = '\nGames: 0'
    on_steam_9 = 'You have not added a Steam profile to your Discord profile. Problems? Type `manual`\nThe API connection has been deleted, so that attackers cannot use your code to gain information.\n\nType `retry` to retry, or to choose a different method of authentication.\nType `manual` to alert moderators of the failure, so that they can look into it.\not responding in 5 minutes results in a kick.'
    on_steam_10 = ' has chosen the Steam method'
    on_steam_11 = 'We have found a Steam profile, but we could not retrieve information. Is your Steam profile private? Problems? Type `manual`\nThe API connection has been deleted, so that attackers cannot use your code to gain information.\n\nType `retry` to retry, or to choose a different method of authentication.\nType `manual` to alert moderators of the failure, so that they can look into it.\not responding in 5 minutes results in a kick.'

    #on_overwatch
    on_overwatch_1 = " has chosen the Overwatch method"
    on_overwatch_2 = '**PLEASE NOTE: OVERWATCH AUTHENTICATION IS CURRENTLY IN BETA AND HAS ONLY BEEN TESTED WITH AN EU PC ACCOUNT. PLEASE REPORT ANY ISSUES YOU FIND ON THE DEVELOPERS SERVER, FOUND USING ;info.\nHow do I verify my account? Add your Battle.net account to your Discord profile, make sure that it is visible on your profile and press the following link: \n<https://altdentifier.xyz/authenticate?user_id='
    on_overwatch_15 = '>\nYour account will be automatically checked. Failing to authorize within 5 minutes means verification will fail.\n\nBy authenticating, you agree with our TOS. View it here: <https://altdentifier.xyz/tos>'
    on_overwatch_3 = "Battle.net Username: "
    on_overwatch_4 = "\nExperience Level: "
    on_overwatch_5 = "\nQuickplay games Played: "
    on_overwatch_6 = "\nQuickplay wins: "
    on_overwatch_7 = "\nQuickplay losses: "
    on_overwatch_8 = "\nCompetitive Rank: "
    on_overwatch_9 = 'Your Overwatch account was not deemed adequate for verification. Problems? Type `manual`.\nThe API connection has been deleted, so that attackers cannot use your code to gain information.\n\nType `retry` to retry, or to choose a different method of authentication.\nType `manual` to alert moderators of the failure, so that they can look into it.\nNot responding in 5 minutes results in a kick.'
    on_overwatch_10 = "Your Battle.net account does not have verified status. Please disconnect your Battle.net account, and reconnect. Make sure that it is visible on your profile. Problems? Type `manual`.\nThe API connection has been deleted, so that attackers cannot use your code to gain information.\n\nType `retry` to retry, or to choose a different method of authentication.\nType `manual` to alert moderators of the failure, so that they can look into it.\nNot responding in 5 minutes results in a kick."
    on_overwatch_11 = 'You have not added a Battle.net profile to your Discord profile. Problems? Type `manual`\nThe API connection has been deleted, so that attackers cannot use your code to gain information.\n\nType `retry` to retry, or to choose a different method of authentication.\nType `manual` to alert moderators of the failure, so that they can look into it.\not responding in 5 minutes results in a kick.'
    on_overwatch_12 = "In which region are you playing Overwatch?\nType: `us` for Americas, `eu` for Europe or `kr` for Korea"
    on_overwatch_13 = "On which platform are you playing Overwatch? Remember that even as a console player, you should still use a PC to connect your battle.net account to Discord.\nType: `pc` for PC (Windows), `xbox` for Xbox One or `playstation` for Playstation 4."
    on_overwatch_14 = "We could not retrieve any Overwatch data. Is your platform incorrect? \nRestarting..."

    #;help
    help_1 = "Help"
    help_2 = "**;setup**\nUsed at first setup\n**;legacysetup**\nUse the old setup if the new one does not work for you\n**;invite**\nSend the bot's invite link\n**;info**\nShows info about the bot\n**;raidmode**\nEnables anti-raid mode, which automatically does an authentication attempt on all new users\n**;settings**\nEdit bot settings\n**;force [user_id]/[user_mention]**\nForce a user to complete authentication, even if they weren't selected automatically\n\nYour prefix may vary, but you can always mention the bot if you forget it."

    # on_voice_state_update
    vu_1 = "entered voice channel **#"
    vu_2 = "left voice channel **#"
    vu_3 = "went from voice channel **#"
    vu_4 = "** to voice channel **#"

    # on_twitter
    on_twitter_1 = 'How do I verify my account? Add your Twitter account to your Discord profile and press the following link: \n<https://www.altdentifier.xyz/authenticate?user_id='
    on_twitter_10 = '>\nYour account will be automatically checked. Failing to authorize within 5 minutes means verification will fail.\n\nBy authenticating, you agree with our TOS. View it here: <https://altdentifier.xyz/tos>'
    on_twitter_2= 'Your Twitter account was not deemed adequate for verification.\nThe API connection has been deleted, so that attackers cannot use your code to gain information.\n\nType `retry` to retry, or to choose a different method of authentication.\n `manual` to alert moderators of the failure, so that they can look into it.\nNot responding in 5 minutes results in a kick.'
    on_twitter_3 = 'You have not added a Twitter account to your Discord profile. Problems? Type `manual`.\nThe API connection has been deleted, so that attackers cannot use your code to gain information.\n\nType `retry` to retry, or to choose a different method of authentication.\nType `manual` to alert moderators of the failure, so that they can look into it.\nNot responding in 5 minutes results in a kick.'
    on_twitter_4 = 'Username: '
    on_twitter_5 = "\nTweets: "
    on_twitter_6 = "\nFollowers: "
    on_twitter_7 = "\nAccount Age: "
    on_twitter_8 = " days."
    on_twitter_9 = " has chosen the Twitter method"

    # on_simple
    on_simple_1 = " has chosen the captcha method."
    on_simple_2 = "Please go to <https://altdentifier.xyz/captcha?user_id="
    on_simple_8 = "> and complete the captcha, then simply press the submit button. If you don't complete the captcha in 5 minutes, the verification will fail."
    on_simple_3 = 'A correct response could not be found. Problems? Type `manual`.\nThe API connection has been deleted, so that attackers cannot use your code to gain information.\n\nType `retry` to retry, or to choose a different method of authentication.\nType `manual` to alert moderators of the failure, so that they can look into it.\nNot responding in 5 minutes results in a kick.'
    on_simple_4 = "Not passed or no captcha received."
    on_simple_5 = "Passed"
    on_simple_6 = "Invalid Hostname. Response did not originate from Altdentifier."
    on_simple_7 = 'Press the following link: <https://www.altdentifier.xyz/authenticate?user_id='
    on_simple_9 = '>. Your account will be automatically checked. Failing to authorize within 5 minutes means verification will fail.\n\nBy authenticating, you agree with our TOS. View it here: <https://altdentifier.xyz/tos>'
    on_simple_10 = 'This authentication code does not belong to your account. Problems? Type `manual`.\nThe API connection has been deleted, so that attackers cannot use your code to gain information.\n\nType `retry` to retry, or to choose a different method of authentication.\nType `manual` to alert moderators of the failure, so that they can look into it.\nNot responding in 5 minutes results in a kick.'
    on_simple_11 = 'An error occured while trying to verify your account. Please try another method. Problems? Type `manual`.\nThe API connection has been deleted, so that attackers cannot use your code to gain information.\n\nType `retry` to retry, or to choose a different method of authentication.\nType `manual` to alert moderators of the failure, so that they can look into it.\nNot responding in 5 minutes results in a kick.'
    on_simple_12 = 'It appears the received token was invalid or you did not respond in time. Please try another method. Problems? Type `manual`.\nThe API connection has been deleted, so that attackers cannot use your code to gain information.\n\nType `retry` to retry, or to choose a different method of authentication.\nType `manual` to alert moderators of the failure, so that they can look into it.\nNot responding in 5 minutes results in a kick.'

    #force
    force_1 = "You cannot use the force command on someone who has administrator permissions"
    force_2 = "You cannot force a bot, that would be silly."

    #audit_log
    audit_log_1 = "Did not respond to message in alotted time"
    audit_log_2 = "AltDentifier Auto-Role"
    audit_log_3 = "Succesfully completed authentication"
    audit_log_4 = "User was selected for authentication"

    #settings_log
    settings_log_1 = "`Enable Altdentification`"
    settings_log_2 = "`Admin Role`"
    settings_log_3 = "`Mod Role`"
    settings_log_4 = "`Human Role`"
    settings_log_5 = "`Logging`"
    settings_log_6 = "`General Channel`"
    settings_log_7 = "`Bot Channel`"
    settings_log_8 = "`Language`"
    settings_log_9 = "`Prefix`"
    settings_log_10 = "`Timezone`"
    settings_log_11 = "`Minimum account age`"
    settings_log_12 = "`Autorole`"
    settings_log_13 = "`Log Channel`"
    settings_log_one = "Setting "
    settings_log_two = "changed to "
    settings_log_three = "Changed by: "
    settings_log_14 = "`Authentication Methods`"
    settings_log_15 = "`Logging Options`"
    settings_log_16 = "`Timeout Action`"

    #prefix
    prefix_1 = "Your prefix is: `"

    #raidmode
    raidmode_1 = "Bot is now configured for anti-raid, will attempt to verify all new joining members regardless of age. If automatic verification is disabled, it will be turned on."
    raidmode_2 = "Anti-raid mode has been turned off, all settings have returned to their old values."