from flask_discord_interactions import (Response, ResponseType, ActionRow,
                                        Button, ComponentType, ButtonStyles,
                                        SelectMenu, SelectMenuOption)


def test_parse_arguments(discord, client):
    @discord.custom_handler()
    def handler(ctx, string_arg, int_arg: int):
        return f"String: {string_arg}, type(int_arg): {type(int_arg)}"

    assert client.run_handler(handler, "hello!", "42").content == \
        "String: hello!, type(int_arg): <class 'int'>"


def test_action_row(discord, client):
    @discord.command()
    def action_row(ctx):
        return Response(
            content="Hi!",
            components=[
                ActionRow()
            ]
        )

    expected = {
        "type": ResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
        "data": {
            "content": "Hi!",
            "embeds": None,
            "flags": 0,
            "tts": False,
            "allowed_mentions": {"parse": ["roles", "users", "everyone"]},
            "components": [{
                "type": ComponentType.ACTION_ROW
            }]
        }
    }

    assert client.run("action_row").dump() == expected


def test_button(discord, client):
    @discord.command()
    def button(ctx):
        return Response(
            content="Hi!",
            components=[
                ActionRow(components=[
                    Button(
                        style=ButtonStyles.PRIMARY,
                        custom_id="my_button",
                        label="My Button"
                    )
                ])
            ]
        )

    expected = {
        "type": ResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
        "data": {
            "content": "Hi!",
            "embeds": None,
            "flags": 0,
            "tts": False,
            "allowed_mentions": {"parse": ["roles", "users", "everyone"]},
            "components": [{
                "type": ComponentType.ACTION_ROW,
                "components": [{
                    "type": ComponentType.BUTTON,
                    "style": ButtonStyles.PRIMARY,
                    "custom_id": "my_button",
                    "label": "My Button",
                    "disabled": False
                }]
            }]
        }
    }

    assert client.run("button").dump() == expected


def test_select_menu(discord, client):
    @discord.command()
    def selectmenu(ctx):
        return Response(
            content="Hi!",
            components=[
                ActionRow(components=[
                    SelectMenu(
                        custom_id="my_menu",
                        placeholder="Choose an option",
                        options=[
                            SelectMenuOption(
                                label="Option 1",
                                value="option1"
                            ),
                            SelectMenuOption(
                                label="Option 2",
                                value="option2"
                            )
                        ]
                    )
                ])
            ]
        )

    expected = {
        "type": ResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
        "data": {
            "content": "Hi!",
            "embeds": None,
            "flags": 0,
            "tts": False,
            "allowed_mentions": {"parse": ["roles", "users", "everyone"]},
            "components": [{
                "type": ComponentType.ACTION_ROW,
                "components": [{
                    "type": ComponentType.SELECT_MENU,
                    "custom_id": "my_menu",
                    "placeholder": "Choose an option",
                    "disabled": False,
                    "options": [
                        {
                            "label": "Option 1",
                            "value": "option1",
                            "default": False,
                        },
                        {
                            "label": "Option 2",
                            "value": "option2",
                            "default": False,
                        }
                    ],
                    "max_values": 1,
                    "min_values": 1,
                }]
            }]
        }
    }

    assert client.run("selectmenu").dump() == expected
