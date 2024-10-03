# Telegram Group Cleaner Bot

A Telegram bot that automatically removes all non-admin members from a specific group. This bot uses the **Telethon** library to interact with the Telegram API and perform the removal of group members.

## Features:
- Fetches all members from a specific Telegram group.
- Automatically kicks all non-admin members from the group.
- Designed to handle large groups efficiently.

---

## Prerequisites:
To use this bot, you need:
- A Telegram bot created via [BotFather](https://t.me/BotFather).
- A Telegram API ID and API Hash from [Telegram API Development Tools](https://my.telegram.org).
- Python 3.7 or higher installed on your machine.

---

## How to Get Your API ID, API Hash, and Bot Token

### 1. Getting API ID and API Hash
You need to get your API ID and API Hash from Telegram’s API portal to use their services.

#### Steps:
1. **Go to Telegram’s API Development Tools**:
   - Visit [https://my.telegram.org](https://my.telegram.org) in your web browser.
   
2. **Log in to your Telegram Account**:
   - Enter your phone number, and Telegram will send you a verification code to log in.

3. **Create a new app**:
   - Once logged in, click on **API Development Tools**.
   - Fill in the required fields (e.g., App title, Short name, etc.) to create a new application.
   
4. **Obtain your credentials**:
   - After creating the application, you will be given your **API ID** and **API Hash**. You will use these credentials in your bot configuration.

### 2. Getting Your Bot Token
1. **Create a bot on Telegram**:
   - Open Telegram and search for [@BotFather](https://t.me/BotFather).
   - Use the command `/newbot` and follow the instructions to create a new bot.
   - After you create the bot, you will receive the **Bot Token**, which you will use in the bot configuration.

---

## Project Setup

### Step 1: Clone the Repository
First, clone this repository to your local machine:
```bash
git clone https://github.com/your-username/telegram-bot-cleaner.git
```
### Step 2: Install the Dependencies
Navigate into the project directory and install the required Python packages:
```bash
cd telegram-bot-cleaner
pip install -r requirements.txt
```
### Step 3: Configure the Bot
Add your API ID, API Hash, Bot Token, and Group ID (either the numeric ID or group username) in the following format:
- api_id = 'YOUR_API_ID'
- api_hash = 'YOUR_API_HASH'
- bot_token = 'YOUR_BOT_TOKEN'
- group_id = 'YOUR_GROUP_ID'  # Can be @username or numeric ID

### Step 4: Run the Bot
Now, run the bot with the following command:
```bash
python cleaner.py
```
Once the bot is running, it will fetch all members from the specified group and start removing all non-admin members.

# Notes:

- Bot Permissions: Make sure your bot has appropriate permissions in the group (admin rights) to kick users.

- Test in Small Groups: Before using this bot on large groups, it’s a good idea to test it in smaller groups to ensure everything works as expected.

### Credits:
MRX7014
