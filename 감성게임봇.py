import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("안녕하세여 감성게임봇입니다 저는 감성게임님의 개인 비서 감성게임봇이라고 합니다")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("!명령어"):
        await message.channel.send("안녕,트위치,누구세여?,키,나이,개인정보,제작자[명령어사용시 !를 붙여주세여]")
    if message.content.startswith("!안녕"):
        await message.channel.send("안녕하세요")
    if message.content.startswith("!트위치"):
        await message.channel.send("https://www.twitch.tv/ironless0805/videos")
    if message.content.startswith("!누구세여?"):
        await message.channel.send("안녕하세여 감성게임봇입니다 저는 감성게임님의 개인 비서 감성게임봇이라고 합니다")
    if message.content.startswith("!키"):
        await message.channel.send("173cm")
    if message.content.startswith("!나이"):
        await message.channel.send("17살")
    if message.content.startswith("!개인정보?"):
        await message.channel.send("내 개인정보를 왜 알고싶으신가여?")
    if message.content.startswith("!제작자?"):
        await message.channel.send("해피에몽#0998")



client.run("NjkwNzA5ODM0ODQwMTQ1OTky.XnVvwQ.EcuM0wMaaUykb8DZzsoWlWM8YSU")