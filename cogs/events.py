import discord
from discord.ext import commands
import asyncio
import datetime
from datetime import date, datetime

intents = discord.Intents.default()
intents.members = True
intents.reactions = True
intents.messages = True


class Events(commands.Cog):
    cooldown = []

    def __init__(self, client, ):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('GramerBot: Events Loaded')

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        fullstring = str(message.content)

        if message.author == self.client.user:
            return

        # if message.content.startswith('!'):
        #     if message.channel.id != 627604248565383179:
        #         return
        if message.channel.type == discord.ChannelType.private:
            if message.author.id in self.cooldown:
                return
            elif message.author.id not in self.cooldown:
                self.cooldown.append(message.author.id)
                async with message.channel.typing():
                    await asyncio.sleep(2)
                await message.author.send('Why have thy\'th DMed me?')
                await asyncio.sleep(1.5)
                async with message.channel.typing():
                    await asyncio.sleep(3)
                await message.author.send('Wait never mind, I don\'t care...')
                self.cooldown.remove(message.author.id)

        if message.channel.id != 627594979468116053: # Not in announcements
            if '@everyone' in fullstring:
                today = datetime.today()
                now = today.strftime('(%m/%d/%Y) %H:%M')
                print('-----------------------------------------')
                print('Pinged @everyone:\n')
                print('@er: ' + str(message.author))
                print('Channel: ' + str(message.channel))
                print('Time: ' + str(now))
                print('-----------------------------------------')
                # await message.channel.send('LOL thx for the @ everyone ' + str(message.author.mention))
            elif '@here' in fullstring:
                today = datetime.today()
                now = today.strftime('(%m/%d/%Y) %H:%M')
                print('-----------------------------------------')
                print('Pinged @here:\n')
                print('@er: ' + str(message.author))
                print('Channel: ' + str(message.channel))
                print('Time: ' + str(now))
                print('-----------------------------------------')
                # await message.channel.send('LOL thx for the @ here ' + str(message.author.mention))

            if len(message.mentions) == 1:
                today = datetime.today()
                now = today.strftime('(%m/%d/%Y) %H:%M')
                print('-----------------------------------------')
                print('Pinged Someone:\n')
                print('@er: ' + str(message.author))
                print('Channel: ' + str(message.channel))
                print('Time: ' + str(now))
                print('Person Pinged: [')
                for x in message.mentions:
                    print(str(x.name) + '#' + str(x.discriminator))
                print(']')
                print('-----------------------------------------')
            elif len(message.mentions) > 1:
                today = datetime.today()
                now = today.strftime('(%m/%d/%Y) %H:%M')
                print('-----------------------------------------')
                print('Pinged Multiple People:\n')
                print('@er: ' + str(message.author))
                print('Channel: ' + str(message.channel))
                print('Time: ' + str(now))
                print('People Pinged: [')
                for x in message.mentions:
                    print(str(x.name) + '#' + str(x.discriminator))
                print(']')
                print('-----------------------------------------')


        if message.channel.id != 627594979468116053 or \
                message.channel.id != 764708179895386133: # Not in announcements or roles
            if message.guild.get_role(764707083521753108) in message.role_mentions or \
                    message.guild.get_role(764706626246148136) in message.role_mentions or \
                    message.guild.get_role(764707317659729971) in message.role_mentions or \
                    message.guild.get_role(767214158495350814) in message.role_mentions or \
                    message.guild.get_role(768973529244762112) in message.role_mentions:
                if len(message.role_mentions) > 1:
                    today = datetime.today()
                    now = today.strftime('(%m/%d/%Y) %H:%M')
                    print('-----------------------------------------')
                    print('Pinged Multiple Pingable Roles:\n')
                    print('@er: ' + str(message.author))
                    print('Channel: ' + str(message.channel))
                    print('Time: ' + str(now))
                    print('Roles Pinged: ' + str(message.role_mentions))
                    print('-----------------------------------------')
                    await message.delete()
                    await message.channel.send(str(message.author.mention) + ' Only @ one pingable role at a time!')
                elif len(message.role_mentions) == 1:
                    today = datetime.today()
                    now = today.strftime('(%m/%d/%Y) %H:%M')
                    print('-----------------------------------------')
                    print('Pinged a Pingable Role:\n')
                    print('@er: ' + str(message.author))
                    print('Channel: ' + str(message.channel))
                    print('Time: ' + str(now))
                    print('Role Pinged: ' + str(message.role_mentions))
                    print('-----------------------------------------')

        if message.channel.id == 627604248565383179:
            if 'gramer' in fullstring.lower():
                await message.channel.send('Did someone say, GRAMER?!?!?!?!')

            if 'gamer' in fullstring.lower():
                await message.channel.send('Did you mean, GRAMER?!?!?!?!')
            if not message.content.startswith('!'):
                if 'dream' in fullstring.lower() and \
                        'good' in fullstring.lower() and \
                        'bad' not in fullstring.lower():
                    await message.channel.send('Dream and Good shouldn\'t be in the same sentance.')
                elif 'jream' in fullstring.lower() and \
                        'good' in fullstring.lower() and \
                        'bad' not in fullstring.lower():
                    await message.channel.send('Jream and Good shouldn\'t be in the same sentance.')

                if 'dream' in fullstring.lower() and \
                        'bad' in fullstring.lower() and \
                        'good' not in fullstring.lower():
                    await message.channel.send('I agree, Dream is Bad.')
                elif 'jream' in fullstring.lower() and \
                        'bad' in fullstring.lower() and \
                        'good' not in fullstring.lower():
                    await message.channel.send('I agree, Jream is Bad.')

                if 'dream' in fullstring.lower() and \
                        'good' not in fullstring.lower() and \
                        'bad' not in fullstring.lower():
                    await message.channel.send('No.')
                elif 'jream' in fullstring.lower() and \
                        'good' not in fullstring.lower() and \
                        'bad' not in fullstring.lower():
                    await message.channel.send('No.')

        # else:
        #     await self.client.process_commands(message)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, reaction):
        # if str(reaction.emoji) == '<:DeadJream:749648709117280397>':
        #     print('poop!')
        # print(str(reaction.emoji) + '\n' + str(reaction.channel_id))
        # print(str(reaction.guild_id) + '\n' + str(reaction.user_id) + '\n' + str(reaction.member.roles))
        #
        # if str(self.client.get_channel(reaction.channel_id)) == '📒»-general':
        #     if str(reaction.emoji) == '🇮🇪':
        #         await reaction.member.add_roles(reaction.member.guild.get_role(627612349083156501), reason=None, atomic=False)

        if reaction.channel_id == 764708179895386133:
            if str(reaction.emoji) == '<:DeadJream:749648709117280397>':
                await reaction.member.add_roles(reaction.member.guild.get_role(764707083521753108), reason=None,
                                                atomic=False)
            elif str(reaction.emoji) == '⛏':
                await reaction.member.add_roles(reaction.member.guild.get_role(764706626246148136), reason=None,
                                                atomic=False)
            elif str(reaction.emoji) == '🔪':
                await reaction.member.add_roles(reaction.member.guild.get_role(764707317659729971), reason=None,
                                                atomic=False)
            elif str(reaction.emoji) == '<:FunnieMouse:757612472109760552>':
                await reaction.member.add_roles(reaction.member.guild.get_role(767214158495350814), reason=None,
                                                atomic=False)
            elif str(reaction.emoji) == '<:scaredcat:713200863744884757>':
                await reaction.member.add_roles(reaction.member.guild.get_role(768973529244762112), reason=None,
                                                atomic=False)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, reaction: discord.RawReactionActionEvent):
        guild = self.client.get_guild(reaction.guild_id)
        if guild.get_member(reaction.user_id) is None:
            member = await guild.fetch_member(reaction.user_id)
        else:
            member = await guild.fetch_member(reaction.user_id)
        if reaction.channel_id == 764708179895386133:
            if str(reaction.emoji) == '<:DeadJream:749648709117280397>':
                await member.remove_roles(guild.get_role(764707083521753108), reason=None, atomic=False)
            elif str(reaction.emoji) == '⛏':
                await member.remove_roles(guild.get_role(764706626246148136), reason=None, atomic=False)
            elif str(reaction.emoji) == '🔪':
                await member.remove_roles(guild.get_role(764707317659729971), reason=None, atomic=False)
            elif str(reaction.emoji) == '<:FunnieMouse:757612472109760552>':
                await member.remove_roles(guild.get_role(767214158495350814), reason=None, atomic=False)
            elif str(reaction.emoji) == '<:scaredcat:713200863744884757>':
                await member.remove_roles(guild.get_role(768973529244762112), reason=None, atomic=False)


def setup(client):
    client.add_cog(Events(client))
