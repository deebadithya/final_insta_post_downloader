# Instagram Post Downloader Bot

![Instagram Post Downloader Bot](https://img.shields.io/badge/status-active-brightgreen.svg)

## Overview
Instagram Post Downloader Bot is a serverless bot built on Azure Functions that enables users to download Instagram posts using a Telegram bot interface. Leveraging the power of serverless architecture, webhook integration, and the Telegram API, this bot provides seamless access to Instagram content.

## Features
- Downloads public resources from Instagram posts.
- Supports user login to download private content.
- Utilizes the Instabot Python package for Instagram interaction.
- Azure Functions serve as the backend for webhook communication.
- Telegram API facilitates bot interaction and messaging.

## Setup

### 1. Obtain Bot API Token
- Create a bot on Telegram using BotFather.
- Follow the instructions to provide basic information, and BotFather will generate an API token for your bot.

### 2. Create Azure Function
- Create an Azure Function app.
- Choose the appropriate trigger type (e.g., HTTP trigger).
- Implement the function logic to handle incoming requests and interact with the Telegram API.

### 3. Connect Azure and Telegram with Webhook
- Set up a webhook in your Azure Function to receive updates from Telegram.
- Configure the webhook URL to point to your Azure Function endpoint.
- Ensure proper security measures are in place to handle incoming requests securely.

### 4. Implement Post Downloading
- Utilize the Instabot Python package to download Instagram posts.
- Implement functionality to handle public and private content downloads.
- Ensure proper error handling and user authentication mechanisms are in place.

## Usage
1. Start a conversation with your Telegram bot.
2. Send the bot API token obtained from BotFather to initialize the bot.
3. Use commands or interactive messaging to interact with the bot and download Instagram posts.

## Additional Information
- Serverless architecture offers scalability and cost-efficiency for running the bot backend.
- Webhook integration ensures real-time communication between Telegram and Azure Functions.
- Instabot Python package provides convenient methods for interacting with Instagram's API.


## Contribution
Contributions are welcome! Feel free to open issues or pull requests for any improvements or features you'd like to add.

## Acknowledgements
- Telegram API: [Telegram Bot API](https://core.telegram.org/bots/api)
- Azure Functions: [Azure Serverless Computing](https://azure.microsoft.com/en-us/services/functions/)
- Instabot: [Instabot - An Instagram Bot](https://github.com/instagrambot/instabot)


For any questions or support, please [open an issue](https://github.com/your_username/final_insta_post_downloader/issues).
