# Hunter of Legends

Hunter of Legends is a Discord bot that allows you to compete with other people in League of Legends by completing various challenges. Even if you lose the game, you can still earn points by successfully completing the bot's challenges, making the game more fun and engaging.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)



## Features

- **Challenge-Based Gameplay**: Earn points by completing in-game challenges.
- **Leaderboard**: Compete with other players and see who tops the leaderboard.
- **Discord Integration**: Seamless integration with Discord for easy access and use.
- **Dynamic Challenges**: Variety of challenges that change over time to keep the gameplay interesting.

## How It Works

1. **Challenge Issuance**: The bot issues challenges to players in a Discord server.
2. **Gameplay Tracking**: Players complete the challenges in their League of Legends games.
3. **Point Allocation**: Points are awarded based on the completion of challenges, regardless of the game outcome.


## Installation

### Prerequisites

- Python 3.x
- Discord API token
- Riot Games API key
- Discord.py
- 
### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/Amine-Zitoun/Hunter-Of-Legends.git
    cd Hunter-Of-Legends
    ```

2. Set up the environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Set up Discord and Riot API:
    - Obtain a Discord API token and Riot Games API key and set them up in the environment variables or a configuration file.

4. Run the bot:
    ```bash
    python bot.py
    ```

## Usage

1. Add the bot to your Discord server.
2. Use the bot commands to receive and complete challenges.


### Basic Commands

- `!Name`: Set up the tracking and get your prey's name
- `!Score <YourSummnorname> <Prey'sName> `: get Your Score after The Match Finishes.
- `!help`: Get help on using the bot.

## Technologies Used

- **Python**: Programming language for the bot logic.
- **Discord.py**: Library to interact with the Discord API.
- **Riot API**: To gather game data from League of Legends.




