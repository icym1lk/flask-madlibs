"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Wow, what a {place}! How many {adjective} {noun} did you eat to get this place? I would have {verb} hundreds of {plural_noun} to get it."""
)

story3 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Fade in, it's dusk and {place} is just beginning to come alive. There's a loud bang and out of nowhere a {adjective} {noun} appears. "You son of a bitch! You {verb} my {plural_noun}! You're going to pay!"""
)

story4 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """{place}, the year is 1467. You don't know why you're here but you sure as hell {adjective} {noun}. You begin to {verb} as {plural_noun} start marching towards you."""
)
