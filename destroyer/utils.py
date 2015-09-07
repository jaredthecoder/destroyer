"""utils.py - Module containing various utility functions"""


import random

from .settings import question_prompts, insult_prompts


def get_random_prompt(name, prompt_type):
    """ Fetches a random prompt for displaying to user. Could be a question or an insult.

    :param name: Name to insert into prompt
    :type name: str or unicode
    :returns: filled in random prompt
    """
    if prompt_type == 'question':
        empty_prompt = random.choice(question_prompts)
    if prompt_type == 'insult':
        empty_prompt = random.choice(insult_prompts)
    prompt = empty_prompt.format(name=name)
    return prompt
