import asyncio

import discord
import random
from discord.ext import commands


class Commands(commands.Cog):
    party_rocker_cooldown = []
    cheaters_list = []
    muted = False

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('GramerBot: Commands Loaded')

    # @commands.command(aliases=['pr', 'partyrocker'])
    # async def party_rocker(self, ctx: commands.Context):
    #     if ctx.channel.id == 627604248565383179:
    #         if ctx.author.id in self.party_rocker_cooldown:
    #             await ctx.send('You must wait 30 seconds to use that command again!')
    #         elif ctx.author.id not in self.party_rocker_cooldown:
    #             self.party_rocker_cooldown.append(ctx.author.id)
    #             await ctx.send('Let\'s say, hypothetically, party rock was in the house tonight. That would imply everybody would just have a good time, am i right? Therefore, we are going to make you lose your mind. Now, for the sake of arguement, what do we just want to see you do? The right answer is: shake that. The implications of this means that when in the club: party rock, in other, politically incorrect words, if you see an attractive, weddable female, she is on my jock.')
    #             await asyncio.sleep(30)
    #             self.party_rocker_cooldown.remove(ctx.author.id)

    @commands.command(aliases=['au-toggle','au-mute','au-unmute','aum','aut'])
    async def au_toggle(self, ctx:commands.Context):
        sender: discord.Member = ctx.author
        guild: discord.Guild = ctx.guild
        if sender.voice is not None:
            if guild.get_role(749342485154889748) in sender.roles:
                vc = sender.voice.channel
                memberIDs = vc.voice_states.keys()
                for x in memberIDs:
                    member: discord.Member = await guild.fetch_member(x)
                    if not self.muted:
                        await member.edit(mute=True)
                    elif self.muted:
                        await member.edit(mute=False)

                self.muted = not self.muted

    @commands.command()
    async def gg(self, ctx: commands.Context):
        if ctx.channel.id == 627604248565383179:
            await ctx.send('https://media.discordapp.net/attachments/627599152288759808/774702891653922866/unknown.png')

    @commands.command()
    async def cat(self, ctx: commands.Context):
        if ctx.channel.id == 627604248565383179:
            await ctx.send('https://media.discordapp.net/attachments/627599152288759808/766719956330872832/IMG_0257.png')

    @commands.command()
    async def scienceguy(self, ctx: commands.Context):
        if ctx.channel.id == 627604248565383179:
            await ctx.send('https://media.discordapp.net/attachments/703786833993007104/703787600506257479/klspxx7re2v41.png?width=586&height=562')

    @commands.command()
    async def h2o(self, ctx: commands.Context):
        if ctx.channel.id == 627604248565383179:
            await ctx.send('https://media.discordapp.net/attachments/703786833993007104/703792385812856832/unknown.png')

    @commands.command()
    async def smort(self, ctx: commands.Context):
        if ctx.channel.id == 627604248565383179:
            await ctx.send('https://media.discordapp.net/attachments/745465769868918805/768907412421607474/smort.png')

    @commands.command(aliases=['hb'])
    async def happyboi(self, ctx: commands.Context):
        if ctx.channel.id == 627604248565383179:
            await ctx.send(
                'https://cdn.discordapp.com/attachments/627604248565383179/763384795316092948/ETj6lUoWAAUN_p0.png')

    @commands.command()
    async def cock(self, ctx):
        cockimage = ['https://media.discordapp.net/attachments/627604248565383179/763574810080837692/2Q.png',
                     'https://media.discordapp.net/attachments/627604248565383179/763574867806257182/Z.png',
                     'https://media.discordapp.net/attachments/627604248565383179/763574882964471818/Z.png']
        if ctx.channel.id == 627604248565383179:
            await ctx.send(random.choice(cockimage))

    @commands.command()
    async def shrug(self, ctx):
        if ctx.channel.id == 627604248565383179:
            await ctx.send('¯\_(ツ)_/¯')

    # @commands.command(aliases=['dd'])
    # async def defaultdance(self, ctx):
    #     image = ['https://tenor.com/view/shaggy-default-dance-victory-gif-14972422',
    #              'https://tenor.com/view/sonic-sonic-the-hedgehog-sonic-the-fortnite-fortnite-default-dance-gif-13050297',
    #              'https://tenor.com/view/roblox-fortnite-dance-default-memes-cool-gif-12661768',
    #              'https://tenor.com/view/sans-fortnite-dance-default-gif-12693690']
    #     await ctx.send(random.choice(image))

    @commands.command()
    async def dancin(self, ctx):
        if ctx.channel.id == 627604248565383179:
            await ctx.send('https://media.discordapp.net/attachments/627604248565383179/765352277132574740/Smug_Dancin.gif')

    @commands.command()
    async def jream(self, ctx):
        if ctx.channel.id == 627604248565383179:
            await ctx.send(':face_vomiting: JREAM <:DeadJream:749648709117280397>')

    @commands.command()
    async def cheats(self, ctx: commands.Context):
        if ctx.channel.id == 627604248565383179:
            if ctx.author.id == 357966938301005825:
                if ctx.author.id in self.cheaters_list:
                    self.cheaters_list.remove(ctx.author.id)
                    await ctx.send('CHEATS DISABLED')
                elif ctx.author.id not in self.cheaters_list:
                    self.cheaters_list.append(ctx.author.id)
                    await ctx.send('CHEATS ENABLED')
            else:
                await ctx.send('YOU MUST BE KCSUP TO CHEAT!!!')

    @commands.command()
    async def quadneo(self, ctx: commands.Context):
        if ctx.channel.id == 627604248565383179:
            if ctx.author.id in self.cheaters_list:
                chance = 100
            else:
                chance = random.randint(1, 100)

            outcome = 100 - chance

            if outcome != 0:
                await ctx.send(format(ctx.author.mention) + ' undershot the QuadNeo by: ' + str(outcome) + '%')
            elif outcome == 0:
                await ctx.send(
                    format(ctx.author.mention) + ' undershot the QuadNeo by: ' + str(outcome) + '%\nYou did the QuadNeo!')

    # @commands.command()
    # async def getbanned(self, ctx):
    #     await ctx.send('https://media.discordapp.net/attachments/627599152288759808/769644916065697843/d37.png')

    @commands.command()
    async def speedrun(self, ctx: commands.Context):
        if ctx.channel.id == 627604248565383179:
            await ctx.send('https://www.youtube.com/watch?v=kX4c8-QaOK8&ab_channel=ShellGuy')

    @commands.command(aliases=['tito'])
    async def nude(self, ctx):
        if ctx.channel.id == 627604248565383179:
            await ctx.send('<:TitoNude:767855958373826590>')

    @commands.command()
    async def darkness(self, ctx):
        if ctx.channel.id == 627604248565383179:
            await ctx.send(format(
                ctx.author.name) + ' thinks the darkness is their ally? They merely adopted the dark. I was born in it, molded by it. I didn\'t see the light until I was already a man, by then it was nothing to me but blinding!')

    @commands.command(aliases=['8ball', 'eightball'])
    async def _8ball(self, ctx, *, question):
        answers = ['As I see it, yes.',
                   'Ask again later.',
                   'Better not tell you now.',
                   'Cannot predict now.',
                   'Concentrate and ask again.',
                   'Don’t count on it.',
                   'It is certain.',
                   'It is decidedly so.',
                   'Most likely.',
                   'My reply is no.',
                   'My sources say no.',
                   'Outlook not so good.',
                   'Outlook good.',
                   'Reply hazy, try again.',
                   'Signs point to yes.',
                   'Very doubtful.',
                   'Without a doubt.',
                   'Yes.',
                   'Yes – definitely.',
                   'You may rely on it.']

        if ctx.channel.id == 627604248565383179:
            if '@everyone' in question:
                await ctx.send('Don\'t try to @ everyone!!!')
            elif '@here' in question:
                await ctx.send('Don\'t try to @ here!!!')
            else:
                await ctx.send(f'Question: {question}\nAnswer: {random.choice(answers)}')

    @commands.command()
    async def nicecock(self, ctx):
        if ctx.channel.id == 627604248565383179:
            await ctx.send(
                'https://media.discordapp.net/attachments/627604248565383179/763574459680423946/EP3EKLqW4AExQma.png?width=318&height=562')

    @commands.command()
    async def sock(self, ctx):
        if ctx.channel.id == 627604248565383179:
            await ctx.send('sock')
            await ctx.send('https://media.discordapp.net/attachments/604847674704920681/765234724633313280/image0.png?width=316&height=562')

    # @commands.command()
    # async def multiply(self, ctx, a, b):
    #
    #     await ctx.send(str(a) + ' * ' + str(b) + ' = ' + str(a * b))

    #'<@&627571395752230942>\n' (@everyone)


    # (USE ONLY IF YOU NEED TO SETUP THE ROLES CHANNEL AGAIN!)
    # @commands.command()
    # async def roles_setup(self, ctx):
    #     msg = await self.client.get_channel(764708179895386133).send(
    #                                                                  'This is the channel where you can get certain roles'
    #                                                                  ' (that are pingable by anyone) to be notified if'
    #                                                                  ' other people want some more people to play the'
    #                                                                  ' certain game relating to the role they pinged!\n\n'
    #                                                                  'React with: <:DeadJream:749648709117280397> for'
    #                                                                  ' <@&764707083521753108>\nReact with: ⛏ for'
    #                                                                  ' <@&764706626246148136>\nReact with: 🔪 for'
    #                                                                  ' <@&764707317659729971>\n\nAnyone can mention'
    #                                                                  ' these roles, so please make sure to mention them'
    #                                                                  ' only if you want more people for the game'
    #                                                                  ' specified in that role!')
    #     await msg.add_reaction(emoji='<:DeadJream:749648709117280397>')
    #     await msg.add_reaction(emoji='⛏')
    #     await msg.add_reaction(emoji='🔪')

    @commands.command()
    async def apply_edits(self, ctx, message_id):
        if ctx.author.id == 357966938301005825:
            test = await ctx.fetch_message(message_id)
            await asyncio.sleep(1)
            await test.edit(content=str(
                'This is the channel where you can get certain roles'
                ' (that are pingable by anyone) to be notified if'
                ' other people want some more people to play the'
                ' certain game relating to the role they pinged!\n\n'
                'React with: <:DeadJream:749648709117280397> for'
                ' <@&764707083521753108>\nReact with: ⛏ for'
                ' <@&764706626246148136>\nReact with: 🔪 for'
                ' <@&764707317659729971>\n'
                'React with: <:FunnieMouse:757612472109760552> for <@&767214158495350814>'
                '\nReact with: <:scaredcat:713200863744884757> for <@&768973529244762112>'
                '\n\nAnyone can mention'
                ' these roles, so please make sure to mention them'
                ' only if you want more people for the game'
                ' specified in that role!'
            ))
            await test.add_reaction(emoji='<:scaredcat:713200863744884757>')
        elif ctx.author.id != 357966938301005825:
            await ctx.send('You cannot apply edits! You must be KCsup to do this!')
            print(format(ctx.author.name) + ' tried to unload apply edits.')

    @commands.command()
    async def edit(self, ctx: commands.Context, message_id, *, new):
        if ctx.author.id == 357966938301005825:
            message = await ctx.fetch_message(message_id)
            await message.edit(content=str(new))
        else:
            await ctx.send('You cannot apply edits! You must be KCsup to do this!')
            print(format(ctx.author.name) + ' tried to unload apply edits.')


def setup(client):
    client.add_cog(Commands(client))
