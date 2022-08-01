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
        await message.channel.send("ゲームを開始するもふ！")

    # start inference
    if message.content.startswith("/game /discuss"):
        selected = random.choice(registered_list)
        word = None
        for key in selected.keys():
            word = selected[key]

        str = ""
        for pair in registered_list:
            for key in pair.keys():
                str = str + key + " "
                #print(str)
        await message.channel.send("お題は\"{}\"だもふ！みんなで順番にお題について語りながら，誰のお題か当ててもふ！参加者は{}もふ".format(word, str))

    # get state
    if message.content.startswith("/game /state"):
        num = len(registered_list)

        str = ""
        for pair in registered_list:
            for key in pair.keys():
                str = str + key + " "
                #print(str)

        # str
        await message.channel.send("現在{}人({})が言葉を登録しているもふ！".format(num, str))

    if message.content.startswith("/game /vote"):
        str = "!poll \"狼はだれ？\""
        for pair in registered_list:
           for key in pair.keys():
                str = str + " \"" + key + "\""

        await message.channel.send(str)

    # get state
    if message.content.startswith("/game /wine"):
        await message.channel.send("<:wineshou:915268406134059039>")

    # show answer
    if message.content.startswith("/game /answer"):
        if selected is not None:
            await message.channel.send("答え：{}".format(selected))
        else:
            await message.channel.send("手順が間違っていたみたい，やり直してもふ！(discussされないかももふ)")

    # Register Word
    if message.content.startswith("/game /register "):
        if client.user != message.author:
            split_word = message.content.split(" ")
            if len(split_word) < 3:
                await message.channel.send("もう一度試してみてもふ！　半角スペース使ってるか確認してもふ")
            else:
                added_word = split_word[2]
                registered_list.append({message.author.name:added_word})
                await message.channel.send("ワードを受け付けたもふ！:{}:{}".format(message.author.name, added_word))

client.run("") # ""の間にトークンを記載
