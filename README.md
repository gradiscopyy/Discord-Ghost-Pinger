# Discord-Ghost-Pinger

A simple Discord bot that pings `@everyone` in a specified channel and then instantly deletes the message. This can be useful for situations where you need to notify users without leaving a visible trace, or move servers, also this may useful for other things!

## Features

- Pings `@everyone` in a specified channel.
- Automatically deletes the ping message after a brief delay (0.5).

## Installation

### Prerequisites

- Python 3.8+
- `discord.py` library

### Steps

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/ghost-ping-bot.git
    cd ghost-ping-bot
    ```

2. **Install the required dependencies**:

    ```bash
    pip install discord
    ```

3. **Configure the bot**:

    Setup `config.json` file in the root directory with the following content:

    ```json
    {
        "token": "YOUR_BOT_TOKEN_HERE",
        "channel": "YOUR_CHANNEL_ID_HERE",
        "minutes": "YOUR_MINUTES_HERE"
    }
    ```

    Replace `YOUR_BOT_TOKEN_HERE` with your actual bot token, and `YOUR_CHANNEL_ID_HERE` put here with the ID of the channel where you want the bot to ping `@everyone` also in `YOUR_MINUTES_HERE` here put the minutes that will give the bot a notice when to ping again.

4. **Run the bot**:

    ```bash
    python bot.py
    ```

## Usage

Once the bot is running, it will automatically start pinging `@everyone` in the specified channel and delete the message instantly after sending.

## Contributing

Feel free to open issues or submit pull requests if you have any suggestions or improvements.

# discord: gradiscopy.

