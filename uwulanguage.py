import discord
import re
import random
import json

class uwu(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.uwu_enabled = True
        self.actions = [
            "*boops your nose*",
            "*nuzzles*",
            "*blushes*",
            "*wags tail*",
            "*sweats*",
            "*giggles*",
            "*pounces on you*"
        ]
        self.faces = ["uwu", "owo", ">w<", "^w^", "(・`ω´・)", "UwU"]

    def uwuify(self, text: str) -> str:
        text = re.sub(r'[rl]', 'w', text)
        text = re.sub(r'[RL]', 'W', text)
        
        text = re.sub(r'n([aeiou])', r'ny\1', text)
        text = re.sub(r'N([aeiou])', r'Ny\1', text)
        text = re.sub(r'N([AEIOU])', r'NY\1', text)
        text = text.replace('ove', 'uv').replace('OVE', 'UV')
        words = text.split(' ')
        new_words = []

        for word in words:

            if not word or word.startswith(('<@', '<#', '<:', '<a:')):
                new_words.append(word)
                continue


            if random.random() < 0.12 and len(new_words) > 0:
                new_words.append(random.choice(self.actions))

  
            if len(word) > 1 and word[0].isalpha() and random.random() < 0.25:
                first_char = word[0]
    
                if random.random() < 0.30:
                    word = f"{first_char}-{first_char.lower()}-{word}"
                else:
                    word = f"{first_char}-{word}"

            new_words.append(word)

        final_text = ' '.join(new_words)

        return f"{final_text} {random.choice(self.faces)}"

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('Type "!toggleuwu" in any chat to turn the auto edit on or off.')

    async def on_message(self, message):
        if message.author.id != self.user.id:
            return


        if message.content.lower() == '!toggleuwu':
            self.uwu_enabled = not self.uwu_enabled
            await message.edit(content=f"*UwU mode is now {'ON' if self.uwu_enabled else 'OFF'}*")
            return
        if not message.content or not self.uwu_enabled:
            return
        if any(message.content.endswith(f" {face}") for face in self.faces):
            return
        if 'http://' in message.content or 'https://' in message.content:
            return
        uwu_text = self.uwuify(message.content)
        if uwu_text != message.content:
            try:
                await message.edit(content=uwu_text)
            except discord.HTTPException:
                pass
with open('config.json', 'r') as f:
    config = json.load(f)

client = uwu()
client.run(config['token'])
