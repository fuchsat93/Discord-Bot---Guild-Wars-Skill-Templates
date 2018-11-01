import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from dw_template_decoder import template_decoder_func
from web_scrape import skillbar_maker

import time

attributes_true_string = ""
skills_true_string = ""

Client = discord.Client()
client = commands.Bot(command_prefix="?")


@client.event
async def on_ready():
    print("Bot is ready!")

return_vals = []


@client.event
async def on_message(message):
    if message.content[:10] == "!template" or message.content[:10] == "!Template ":
        skill_template = message.content[10:]
        attributes_true_string = ""
        skills_true_string = ""
        version_number_true, primary_profession_true, secondary_profession_true, attributes_true, skills_true = template_decoder_func(skill_template)
        skillbar_maker(skills_true)
        for x, y in attributes_true:
            attributes_true_string = attributes_true_string + "\n" + " " + str(x) + ": " + str(y)
        for x in skills_true:
            skills_true_string = skills_true_string + "\n" + "-  " + str(x)
        await client.send_message(message.channel,
                "Primary Profession: " + primary_profession_true +
                "\nSecondadry Profession: " + secondary_profession_true +
                attributes_true_string +
                "\n-------Skills-------" +
                skills_true_string.replace('_', ' ')
        )
        with open("**YOUR PATH HERE**\\skill_template.jpg", 'rb') as f:
            await client.send_file(message.channel, f)
    elif message.content[:11] == "!Discordway" or message.content[:11] == "!discordway":
        await client.send_message(message.channel, "Welcome to the Discordway bot!" +
                "\nPlease type '!Template (Skill template)' to view a skill template" +
                "\nExample: !Template OQhkAkB8QGOEJAhzKACYeWGQO1FD")

client.run("**YOUR CODE HERE**")
