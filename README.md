# [ITCringeParse](https://vk.com/itcringe)

[!["Made with Python"][1]](https://www.python.org/) [![][2]][3]

[1]: https://img.shields.io/badge/Made%20with-Python-%23FFD242?logo=python&logoColor=white
[2]: https://img.shields.io/badge/python-3.9.6-blue.svg
[3]: https://www.python.org/downloads/release/python-396

> This script parses posts from your VK group and publishes them in the Telegram channel (text and photos).

## Installation
```bash
git clone https://github.com/Moonquit/itcringebot.git
```


## Usage
1. ### Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

2. ### Configure `src/config.py`
    - You need to create a bot in Telegram via [@BotFather](https://t.me/botfather) and get a token.
    - Add the created bot to your Telegram channel and grant administrator rights.
    - Fill in the variables in the `src/config.py`:

        |Name|Type|Required to fill|Description|
        |:-|:-:|:-:|:-|
        |TG_TOKEN|str|+|Telegram bot token|
        |TG_CHANNEL|str|+|Link to Telegram channel (required with @)|
        |VK_TOKEN|str|+|VK bot longpoll token|
        |VK_API_VERSION|str|-|VK API version|


3. ### Run
    ```bash
    python -m src
    ```
