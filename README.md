# README

## Description:
This Python script is created solely for educational purposes. The creator bears no responsibility for any usage or consequences related to this code. The script facilitates the extraction of chats from Telegram. 

## Setup:
To use this script, you need to obtain API credentials from [my.telegram.org](https://my.telegram.org). After obtaining the API ID and hash, you should fill in the variables `api_id` and `api_hash` in the script.

Install the necessary dependencies by running:
```
pip install -r requirements.txt
```

## Usage:
1. Register and obtain API credentials from [my.telegram.org](https://my.telegram.org).
2. Fill in the `api_id` and `api_hash` variables in the script with your obtained credentials.
3. Run the script.
4. When prompted, enter the number corresponding to the chat from which you want to extract messages.
5. The script will download media files (photos, videos, audios, documents) from the specified chat and save them to the "downloads" directory.
6. Text messages from the chat will be saved in a file named "dwarf.txt" along with their timestamps.

## License:
This script is distributed under the terms of the GNU Affero General Public License (AGPL) Version 3. You can find a copy of the license in the `LICENSE` file accompanying this script. Please read the license carefully before using this script.

## Disclaimer:
This script is provided as-is, without any guarantees. The creator does not take responsibility for any actions taken with this script. Use it at your own risk.