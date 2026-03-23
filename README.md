# **Password Generator Bot**

This Telegram bot combines versatility and security, helping you effectively manage your digital security. Using the Diceware method, it generates strong, memorable passwords and includes tools for encryption and strength analysis.

<img width="1015" height="373" alt="image" src="https://github.com/user-attachments/assets/fc410725-aa2f-4261-a5f2-af19c2d281d1" />



# **Project Structure**

<img width="263" height="392" alt="image" src="https://github.com/user-attachments/assets/1ac927fd-b89c-42fe-9dad-288be49dc150" />



# **Key Features**

**1) Diceware Generation**: Produce strong passphrases using a curated list of real words. Easy to memorize for humans, but highly resistant to brute-force attacks.

**2) Strength Checker**: Analyze your password and receive immediate feedback on its complexity and security level.

**3) PIN Generator**: Quickly generate random numerical codes for devices or quick unlocks.

**4) Caesar Cipher**: Tool to encrypt and decrypt messages using one of the earliest and simplest encryption techniques.

# **Installation**

To run the bot locally, follow these steps:

**1) Fork this repository and clone your fork into your machine using**

```bash
git clone git@github.com:USERNAME/Password-Generator-Bot.git
```
Then type this:

```bash
cd Password-Generator-Bot
```


**2) Install dependencies:**

Ensure you have Python installed, then run:

```bash
pip install -r requirements.txt
```

**3) Configuration:**

Create a .env file in the project root and add your Telegram API Token obtained from [BotFather](https://telegram.me/BotFather)

Below there is an example for your .env file:

```bash
TELEGRAM_BOT_TOKEN=your_token_here
```

**4) Run the bot:**

```bash
python -m bot.main
```

# **Technologies Used**

- Python 3.12.2

- Python-Telegram-Bot

- Python-Dotenv

# **Contributing**

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

# **Authors**

[Andrea Aprile](https://github.com/Andy-ai-pixel)  

[Antonio Pistone](https://github.com/Antonio4603)  

[Gabriel Calabrese](https://github.com/calabresegabriel78-dotcom)
