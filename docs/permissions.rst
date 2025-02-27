Permissions
===========

Discord allows defining permissions for each slash command in a specific guild
or at the global level. Flask-Discord-Interactions provides a Permission class
and two major ways of setting the permissions of a command.

Permission class
----------------

The :class:`.Permission` class accepts either a role ID or a user ID.

.. autoclass:: flask_discord_interactions.Permission
    :members:


Slash Command constructor
-------------------------

You can define permissions when defining a Slash Command. These will be
registered immediately after your Slash Command is registered.

You can set the ``default_permission``, then use the ``permissions`` parameter
to specify any overwrites.

.. code-block:: python

    @discord.command(default_permission=False, permissions=[
        Permission(role="786840072891662336")
    ])
    def command_with_perms(ctx):
        "You need a certain role to access this command"

        return "You have permissions!"

Context object
--------------

You can also use the :meth:`.Context.overwrite_permissions` method to overwrite
the permissions for a command. By default, this is the command currently
invoked. However, you can specify a command name.

.. code-block:: python

    @discord.command(default_permission=False)
    def locked_command(ctx):
        "Secret command that has to be unlocked"

        return "You have unlocked the secret command!"


    @discord.command()
    def unlock_command(ctx):
        "Unlock the secret command"

        ctx.overwrite_permissions(
            [Permission(user=ctx.author.id)], "locked_command")

        return "Unlocked!"

