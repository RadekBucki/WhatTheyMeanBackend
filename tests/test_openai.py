import base64
import os
import unittest

import backend.ai


class TestOpenAI(unittest.TestCase):

    def test_transcribe(self):
        with open(os.path.join('audio', 'monologue.mp3'), 'rb') as mp3_file:
            encoded_audio = base64.b64encode(mp3_file.read())
            text = backend.ai.transcribe(encoded_audio)
        self.assertNotEquals(text, '')
    
    def test_sum_up(self):
        text = ("The media will not show the magnitude of this crowd. Even I, when I turned on today, I looked, and I "
                "saw thousands of people here, but you don’t see hundreds of thousands of people behind you because "
                "they don’t want to show that. We have hundreds of thousands of people here, and I just want them to "
                "be recognized by the fake news media. Turn your cameras please and show what’s really happening out "
                "here because these people are not going to take it any longer. They’re not going to take it any longer. "
                "Go ahead. Turn your cameras, please. Would you show? They came from all over the world, actually, "
                "but they came from all over our country. I just really want to see what they do. I just want to see "
                "how they covered. I’ve never seen anything like it. But it would be really great if we could be covered "
                "fairly by the media. The media is the biggest problem we have as far as I’m concerned, single biggest problem, "
                "the fake news and the big tech. Big tech is now coming into their own. "
                "We beat them four years ago. We surprised them. We took them by surprise and this year, they rigged an election. "
                "They rigged it like they’ve never rigged an election before. By the way, last night, they didn’t do a bad job either, "
                "if you notice. I’m honest. I just, again, I want to thank you. It’s just a great honor to have this kind of crowd and to be before you. "
                "Hundreds of thousands of American patriots are committed to the honesty of our elections and the integrity of our glorious Republic. "
                "All of us here today do not want to see our election victory stolen by emboldened radical left Democrats, which is what they’re doing and stolen by the fake news media. "
                "That’s what they’ve done and what they’re doing. We will never give up. We will never concede, it doesn’t happen. You don’t concede when there’s theft involved.")
        summary = backend.ai.sum_up(text)
        self.assertLess(len(summary), len(text))


if __name__ == '__main__':
    unittest.main()
