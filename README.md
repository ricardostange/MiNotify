# MiNotify
Send message notifications to Mi Band using Python and Telegram

# Setting it up
1. Activate Telegram notifications on your Mi Fit app  
Profile -> Your Device -> Application Alert -> Manage applications -> Telegram  
2. Create a telegram bot. An easy way is to message @BotFather on Telegram.
3. Download the file **minotify.py**
4. Place the Telegram bot token that was created in string "YOUR_TOKEN_HERE"
5. Install Telegram-python dependency by running
`pip install python-telegram-bot`

# How To Use
First, create your bot:  
  
`bot = MiNotify('YOUR_TOKEN_HERE')`  
  
Then wait for '/start' from the user:  
  
`bot.wait_for_start()`
  
After that you can send notifications using:  
  
`bot.message("Your message here")`

# Issues and Sugestions
Email me: ricstange@gmail.com

# Contributing
Feel free to contribute by forking and adding new funcionality/cleaning up code/making any change.  
