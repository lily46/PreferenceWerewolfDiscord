import time

import discord
import random

registered_dict = {}
registered_dict_backup = {}
client = discord.Client()
wolf = None


@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('----')


@client.event
async def on_message(message):
    global is_run, registered_dict, wolf, registered_dict_backup
    # Start Game
    if message.content.startswith('/game /start'):
        registered_dict = dict()
        wolf = None
        await message.channel.send('ゲームを開始するもふ！')

    # start inference
    if message.content.startswith('/game /discuss'):
        registered_dict_backup = registered_dict.copy()
        wolf = random.choice(list(registered_dict.items()))
        word = wolf[1]
        people_str = ' '.join(registered_dict.keys())

        await message.channel.send(f'お題は"{word}"だもふ！みんなで順番にお題について語りながら，誰のお題か当ててもふ！参加者は{people_str}もふ')

    # get state
    if message.content.startswith('/game /state'):
        num = len(registered_dict)
        people_str = ' '.join(registered_dict.keys())

        await message.channel.send(f'現在{num}人({people_str})が言葉を登録しているもふ！')

    if message.content.startswith('/game /vote'):
        message_str = '!poll "狼はだれ？" '
        quoted_people = map(lambda x: f'"{x}"', registered_dict.keys())
        people_str = ' '.join(quoted_people)
        message_str += people_str

        await message.channel.send(message_str)

    # get state
    if message.content.startswith('/game /wine'):
        await message.channel.send('<:wineshou:915268406134059039>')

    # show answer
    if message.content.startswith('/game /answer'):
        if wolf is not None:
            await message.channel.send(f'答え：{wolf}')
        else:
            await message.channel.send('手順が間違っていたみたい，やり直してもふ！(discussされないかももふ)')

    # Open Word
    if message.content.startswith('/game /open'):
        author_name = message.author.name
        if author_name in registered_dict_backup:
            word = registered_dict[author_name]
            await message.channel.send(f'{author_name}さんのお題は、{word}もふ！')

    # Register Word
    if message.content.startswith('/game /register '):
        if client.user != message.author:
            split_word = message.content.split(' ')
            if len(split_word) < 3:
                await message.channel.send('もう一度試してみてもふ！　半角スペース使ってるか確認してもふ')
            else:
                added_word = split_word[2]
                author_name = message.author.name
                registered_dict[author_name] = added_word
                await message.channel.send(f'ワードを受け付けたもふ！:{author_name}:{added_word}')


client.run('')  # ''の間にトークンを記載
