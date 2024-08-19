# Raph Manager

This is a Nextcord-based bot addon for [Jailbreak Vision](https://github.com/Poco-Coco/Jailbreak-Vison-v3), primarily designed to generate graphs based on the results of dyno speed tests.

> ⚠️ **Caution:** This bot has not been actively maintained for a significant period of time and may be out of date. Users may need to make modifications to ensure proper functionality. Please proceed with caution and be prepared to update code as necessary.

## Table of Contents
- [Raph Manager](#raph-manager)
  - [Table of Contents](#table-of-contents)
  - [Setup](#setup)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Commands](#commands)
    - [General Commands](#general-commands)
      - [`!reloadcogs`](#reloadcogs)
    - [Slash Commands](#slash-commands)
      - [`/list`](#list)
    - [Graph Generator Commands](#graph-generator-commands)
      - [`!structure`](#structure)
    - [Error Handling](#error-handling)
  - [Permissions](#permissions)

## Setup

### Prerequisites
1. Python 3.8+
2. Install the required dependencies:
   ```bash
   pip install nextcord matplotlib cooldowns
   ```

### Installation
1. Clone the repository and navigate to the project folder:
   ```bash
   git clone https://github.com/your-repository-url.git
   cd your-bot-folder
   ```

2. Add your bot token in the `TOKEN` variable within the `main.py` file:
   ```python
   TOKEN = "YOUR_BOT_TOKEN"
   ```

3. Add your `OWNER_ID` variable within the `main.py` file (Optional):
    ```python
    TOKEN = "YOUR_BOT_TOKEN"
    ```

1. Run the bot:
   ```bash
   python main.py
   ```

The bot will start up, load all available cogs, and print a message when online.

## Commands

### General Commands

#### `!reloadcogs`
Reloads all cogs currently in the bot's `raphsmanager/cogs` directory.

- **Usage**: `!reloadcogs`
- **Permission**: This command is restricted to users with specific IDs (e.g., `699452241312219147`). Unauthorized users will receive a "You don't have permission" message.

### Slash Commands

#### `/list`
Displays all the servers the bot is currently in, along with their member counts.

- **Usage**: `/list`

### Graph Generator Commands

The graph generator uses JSON data attached to a command to generate graphs. The JSON should have a structure that includes `Settings` and `SpeedTest` keys.

#### `!structure`
Generates a graph from the attached JSON file.

- **Usage**: Attach a JSON file to the command and run:
   ```bash
   !structure
   ```
- **Parameters**:
  - `GraphTransparent` (Optional, default: `False`): If set to `True`, the generated graph will have a transparent background.
  
- **Example JSON structure**:
    ```json
    {
      "Settings": {
        "Test Mode": "Test",
        "Vehicle Name": "Car"
      },
      "SpeedTest": {
        "0": {
          "Time": "0",
          "Speed": "0"
        },
        "1": {
          "Time": "1",
          "Speed": "50"
        },
        ...
      }
    }
    ```

- **Output**: The bot will generate and send back the graph as an image file.

### Error Handling

The bot includes cooldown handling, and users will be notified if they attempt to use a command that is still on cooldown. The message will display how much time is left before they can retry the command.

## Permissions

- **Bot Owner**: Some commands like `!reloadcogs` are restricted to specific user IDs (e.g., `90120417429414122`), which is typically the bot owner.
  
- **General Users**: All users can access public commands like `/list` and graph generation commands unless otherwise restricted.
