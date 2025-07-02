import discord

class OAuthView(discord.ui.View):
    """View with OAuth button."""

    def __init__(self, oauth_url: str, provider_name: str):
        super().__init__(timeout=300)
        self.oauth_url = oauth_url
        self.provider_name = provider_name

        button = discord.ui.Button(
            label=f"Connect {provider_name}",
            style=discord.ButtonStyle.link,
            url=oauth_url
        )
        self.add_item(button)
