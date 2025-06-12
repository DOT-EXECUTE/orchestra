# Discord Bot CLI Helper

A command-line tool to help initialize and register commands for your Discord bots.

## Features

- Initialize a new Python-based Discord bot project structure.
- Register slash commands for your bot interactively.

## Commands

### `init`

This command initializes a new Discord bot project. It creates a new directory with the specified project name and populates it with template files to get you started quickly.

**Usage:**

```bash
python orch.py init <project-name>
```

Replace `<project-name>` with the desired name for your bot project (e.g., `my-cool-bot`).

**Generated Files:**

Running this command will create the following structure in a new folder named `<project-name>`:

-   `bot.py`: The main file for your Discord bot, pre-filled with basic setup using `discord.py`.
-   `requirements.txt`: A file listing the Python dependencies for the bot (e.g., `discord.py`, `python-dotenv`).
-   `.env`: An environment file template. You **must** edit this file to add your `DISCORD_TOKEN`.

### `register`

This command helps you register slash commands for your Discord bot with Discord's API. It interactively prompts you for the command's name, description, and any options (including their types, descriptions, and whether they are required, and choices if applicable).

**Important:** You must run this command from *inside* the bot project directory that was created using the `init` command (i.e., the directory containing your `bot.py` and `.env` files). This is because it relies on the `DISCORD_TOKEN` found in the `.env` file.

**Usage:**

Navigate to your bot's project directory:

```bash
cd <project-name>
```

Then run the command:

```bash
python ../orch.py register
```
*(Assuming `orch.py` is in the parent directory, or adjust the path as needed based on your setup if you moved `orch.py`)*

The command will guide you through a series of questions to define your slash commands.

**Output:**

The command definitions are saved to an `output/discord_commands.yaml` file within your project directory. This file serves as a record of the commands you've registered.

## Getting Started

Follow these steps to set up and use the Discord Bot CLI Helper.

### Prerequisites

- Python 3.8 or higher
- Poetry for package management (Install it from [https://python-poetry.org/docs/#installation](https://python-poetry.org/docs/#installation))
- Git

### Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository-url> # Replace <repository-url> with the actual URL of this repository
    cd <repository-directory> # Replace <repository-directory> with the name of the cloned folder
    ```

2.  **Install dependencies using Poetry:**

    This project uses Poetry to manage its dependencies.

    ```bash
    poetry install
    ```
    This will create a virtual environment and install the necessary packages like `click`, `PyYAML`, and `python-dotenv`.

### Initial Setup for Bot Development

After using the `init` command to create your bot project (`<project-name>`):

1.  **Navigate to your new bot project directory:**

    ```bash
    cd <project-name>
    ```

2.  **Create and configure your environment file:**

    The `init` command creates a `.env` file in your project directory. You **must** edit this file to add your Discord bot's token:

    ```env
    DISCORD_TOKEN=YOUR_BOT_TOKEN_HERE
    ```

    Replace `YOUR_BOT_TOKEN_HERE` with your actual bot token from the [Discord Developer Portal](https://discord.com/developers/applications).

## Usage Workflow

Here's a typical workflow for using this tool:

1.  **Initialize your bot project:**
    Use the `init` command from the root directory of this CLI tool to create a new bot project.

    ```bash
    # Make sure you are in the root directory of the discord-bot-cli-helper
    python orch.py init my-awesome-bot
    ```

2.  **Configure your bot:**
    -   Navigate into your newly created project directory (e.g., `cd my-awesome-bot`).
    -   Edit the `.env` file and add your `DISCORD_TOKEN`.
    -   Customize your `bot.py` as needed (add cogs, event handlers, etc.).
    -   Add any additional Python dependencies to your `requirements.txt` and install them (e.g., `pip install -r requirements.txt` within the bot's virtual environment if you choose to create one for the bot itself, or manage it with Poetry if you convert the bot project to a Poetry project).

3.  **Register slash commands:**
    Once your bot token is set up in `.env`, run the `register` command from *within your bot project directory* to define and register your slash commands with Discord.

    ```bash
    # Make sure you are inside your bot's project directory (e.g., my-awesome-bot)
    python ../orch.py register
    ```
    *(Adjust path to `orch.py` if necessary)*

4.  **Run your bot:**
    After registering commands, you can run your bot using:

    ```bash
    # Make sure you are inside your bot's project directory
    python bot.py
    ```

## Contributing

Contributions are welcome! If you have suggestions for improvements or find any issues, please feel free to open an issue or submit a pull request on the project's repository.

For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
