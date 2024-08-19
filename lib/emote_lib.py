import re
from collections import defaultdict
from typing import Dict, List, AsyncIterator

# Constant for the message fetch limit
MESSAGE_FETCH_LIMIT = 10000

def extract_emote_usage(messages: List[str]) -> Dict[str, int]:
    """
    Extracts and counts emote usage from a list of messages.

    Parameters:
    - messages (List[str]): A list of chat messages.

    Returns:
    - Dict[str, int]: A dictionary mapping emotes to their usage counts.
    """
    emote_usage = defaultdict(int)
    emote_pattern = re.compile(r"<:\w+:\d+>")

    for message in messages:
        emotes = emote_pattern.findall(message)
        for emote in emotes:
            emote_usage[emote] += 1

    return dict(emote_usage)

async def fetch_chat_messages(channels: List[AsyncIterator]) -> List[str]:
    """
    Fetches chat messages from a list of channels.

    Parameters:
    - channels (List[AsyncIterator]): A list of channel objects supporting async iteration.

    Returns:
    - List[str]: A list of message contents.
    """
    messages = []
    for channel in channels:
        async for message in channel.history(limit=MESSAGE_FETCH_LIMIT):
            messages.append(message.content)
    return messages