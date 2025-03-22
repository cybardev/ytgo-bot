# ytgo-bot

Discord bot to call ytgo

<img height="128px" width="128px" src="./ytgo.png" alt="ytgo logo"><img height="128px" src="./ytgo-banner.png" alt="ytgo banner">

## Usage

1. Create a bot via Discord Developer Portal.

2. From the left list of tabs, select Installation and copy the Install Link.

3. Visit the Install Link in a browser and add your bot to desired server(s) and/or guild(s).

4. Deploy bot to Render using the button under [Deployment](#deployment).
    - Set the `BOT_TOKEN` environment variable to your bot's token (Discord Developer Portal `>` Bot `>` Token)

2. Messages with `!yt` are tracked. Send `!yt <search term>` in a server/guild with the bot to return the URL of the first search result on YouTube with the specified query.

## Deployment

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/cybardev/ytgo-bot)
