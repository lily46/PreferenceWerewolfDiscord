import discord
import random

registered_list = []
client = discord.Client()
selected = None

@client.event
async def on_ready():
    print("logged in as")
    print(client.user.name)
    print(client.user.id)
    print('----')

@client.event
async def on_message(message):
    global is_run, registered_list, selected
    # Start Game
    if message.content.startswith("/game /start"):
        registered_list = []
        selected = None
        await message.channel.send("ゲームを開始するよ！")

    # start inference
    if message.content.startswith("/game /discuss"):
        selected = random.choice(registered_list)
        word = None
        for key in selected.keys():
            word = selected[key]
        await message.channel.send("お題は\"{}\"だよ！みんなで順番にお題について語りながら，誰のお題か当ててみてね！".format(word))

    # get state
    if message.content.startswith("/game /state"):
        num = len(registered_list)
        await message.channel.send("現在{}人が言葉を登録しているよ！".format(num))

    # show answer
    if message.content.startswith("/game /answer"):
        if selected is not None:
            await message.channel.send("答え：{}".format(selected))
        else:
            await message.channel.send("手順が間違っていたみたい，やり直してね！")

    # Register Word
    if message.content.startswith("/game /register "):
        if client.user != message.author:
            split_word = message.content.split(" ")
            if len(split_word) < 3:
                await message.channel.send("もう一度試してみてね！")
            else:
                added_word = split_word[2]
                registered_list.append({message.author.name:added_word})
                await message.channel.send("ワードを受け付けたよ！:{}:{}".format(message.author.name, added_word))

client.run("") # ""の間にトークンを記載
