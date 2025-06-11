from utils.files import copyTemplate as ct
from dotenv import load_dotenv
from pathlib import Path
import requests
import click
import yaml
import time
import sys
import os

@click.command()
@click.argument("name")
def init(name: str):
	"""Creates a new project template"""
	try:
		projectPath = Path(f"../{name}")
		projectPath.mkdir(parents=True, exist_ok=True)
		
		files = {
			"bot.py" : "Main Bot File",
			"requirements.txt" : "Pip Dependency File",
			".env" : "Enviroment Variable File"
		}

		for filename, desc in files.items():
			dest = ct(filename, name)
			click.echo(f"✓ Created: {desc} -> {dest}")
		time.sleep(1)
		click.echo("\n\n⚠ '.env' Must be updated with your bots token\n\n")

	except FileNotFoundError as e:
		click.echo(f"❌ Error: Template not found - {str(e)}")

	except Exception as e:
		click.echo(f"❌ Unexpected error: {str(e)}")

@click.command
def register():
	"""Register slash commands with a series of questions, Must be in project folder"""
	load_dotenv()

	AppId = int(click.prompt("What's Your Client ID [App ID]?\n"))
	CmdMaxCount = int(click.prompt("How many commands are you registering?\n"))
	TOKEN = os.getenv("DISCORD_TOKEN")
	URL = f"https://discord.com/api/v9/applications/{AppId}/commands"

	CmdCount = 1

	# == Check for/Make Output file ==
	output_dir = os.path.join("..", "output")
	os.makedirs(output_dir, exist_ok=True)  # Ensure the folder exists (REQUIRES ADMIN) 

	output_path = os.path.join(output_dir, "discord_commands.yaml")

	# == Write the YAML with correct options ==
	with open(output_path, "w") as f:
		while CmdCount <= CmdMaxCount:
			CommandName = click.prompt(f"What's the name of command {CmdCount}?\n")
			CommandDescription = click.prompt(f"What's the description of command {CmdCount}?\n")

			# Ask how many options
			OptMaxCount = click.prompt("How many options do you want (Press enter to skip)?\n", default="")
			options = []

			if OptMaxCount.strip() == "":
				OptMaxCount = 0
			else:
				OptMaxCount = int(OptMaxCount)

			OptCount = 0

			while OptCount < OptMaxCount:
				option_name = click.prompt(f"Enter the name of option {OptCount + 1}:\n")
				option_type = click.prompt(f"Enter the type of option '{option_name}' (e.g., 6 for Member, 3 for string):\n")
				option_description = click.prompt(f"Enter a description for option '{option_name}':\n")
				option_required = click.prompt(f"Is option '{option_name}' required? [Y/n]\n").lower() == 'y'

				# Ask for choices if applicable
				choices = []
				add_choices = click.prompt(f"Do you want to add choices for '{option_name}'? [Y/n]\n").lower() == 'y'
				while add_choices:
					choice_name = click.prompt(f"Enter the choice name for '{option_name}':\n")
					choice_value = click.prompt(f"Enter the value for choice '{choice_name}':\n")
					choices.append({"name": choice_name, "value": choice_value})
					add_choices = click.prompt(f"Do you want to add another choice for '{option_name}'? [Y/n]\n").lower() == 'y'

				# Add the option data to the options list
				option_data = {
					"name": option_name,
					"type": int(option_type),
					"description": option_description,
					"required": option_required,
				}

				if choices:
					option_data["choices"] = choices

				options.append(option_data)
				OptCount += 1

			# Write the command and options to the file
			f.write(f"""- name: {CommandName}
	description: {CommandDescription}
	""")
			if options:
				f.write("  options:\n")
				for option in options:
					f.write(f"""    - name: {option['name']}
		type: {option['type']}
		description: {option['description']}
		required: {str(option['required']).lower()}\n""")
					if 'choices' in option:
						f.write("      choices:\n")
						for choice in option['choices']:
							f.write(f"""        - name: {choice['name']}
			value: {choice['value']}\n""")
			CmdCount += 1

	# == Read YAML ==
	with open(output_path, "r") as file:
		yamlContent = file.read()

	commands = yaml.safe_load(yamlContent)
	headers = {"Authorization": f"Bot {TOKEN}", "Content-Type": "application/json"}

	# == Create Commands ==
	for command in commands:
		res = requests.post(URL, json=command, headers=headers)  # Fix: json=command (not commands)
		commandName = command["name"]
		click.echo(f"Command {commandName} created: {res.status_code}")
		if res.status_code != 200 and res.status_code != 201:
			click.echo(f"ERROR: {res.text}")  # Debug output