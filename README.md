# mr-dale

## Overview
mr-dale is a discord bot that you can use in your team collaboration. 
You can deploy it to your local environment and connect it to discord server of your project. 
This bot is being developed for the Russian-speaking audience. 
before deploying and launching this bot in your environment, you need to create an application on the [Discord Developer Portal](https://discordapp.com/developers/applications/). 
for more information about creating an app and configuring a bot for discord, see the official documentation. 
At the first launch mr-dale creates a separate text channel for interaction with the server members. 


## Deployment and launch

### Prerequisites
Before deploying the project, make sure that the following dependencies are installed on your system:
* [python interpreter](https://www.python.org/). requires python version 3.8.x. 
* [poetry](https://python-poetry.org/). it is a necessary tool for managing python project dependencies, as well as organizing isolated virtual environments. 


### Instolation
Firstly clone this repository at your local machine via git. 
then run the following command to install the project and all its dependencies:
```
poetry install --no-dev
```
If you need to deploy a development environment that includes additional dependencies, use the following command:
```
poetry install
```


### Setting up and running the bot
Before starting the bot, you need to configure the environment variable "mrdtoken". 
this variable must contain the secret token required to interact with the discord api. 
to launch the bot, run the following command:
```
poetry run start-bot
```
