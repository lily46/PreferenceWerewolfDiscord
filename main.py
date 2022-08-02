import random

import discord

registered_dict = {}
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
    global is_run, registered_dict, wolf
    # Start Game
    if message.content.startswith('/game /start'):
        registered_dict = dict()
        wolf = None
        await message.channel.send('ゲームを開始するもふ！')

    # start inference
    if message.content.startswith('/game /discuss'):
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

    # Register Word
    if message.content.startswith('/game /register '):
        await register_word(message)

    # Execution
    if message.content.startswith('/game /execution '):
        await execute(message)

    # Bite
    if message.content.startswith('/game /bite '):
        await bite_person(message)


async def register_word(message):
    """
    入力されたワードを登録する
    :param message:
    :return:
    """
    global registered_dict
    if client.user == message.author:
        return

    split_word = message.content.split(' ')
    if len(split_word) < 3:
        await message.channel.send('もう一度試してみてもふ！　半角スペース使ってるか確認してもふ')
        return

    added_word = split_word[2]
    author_name = message.author.name
    registered_dict[author_name] = added_word
    await message.channel.send(f'ワードを受け付けたもふ！:{author_name}:{added_word}')


async def display_survivor(message):
    """
    生存者を表示する
    :param message:
    :return:
    """
    global registered_dict
    num = len(registered_dict)
    people_str = ' '.join(registered_dict.keys())
    await message.channel.send(f'現在の生存者は{num}人({people_str})もふ')


async def execute(message):
    """
    入力された名前の人を吊る
    :param message:
    :return:
    """
    global registered_dict

    if client.user == message.author:
        return

    split_word = message.content.split(' ')
    if len(split_word) < 3:
        await message.channel.send('もう一度試してみてもふ！　半角スペース使ってるか確認してもふ')
        return

    name = split_word[2]
    if name not in registered_dict.keys():
        await message.channel.send('その人はもういないもふ')
        return

    await message.channel.send(f'{name}さんが吊られてしまったもふ…')
    registered_dict.pop(name)
    await display_survivor(message)


async def bite_person(message):
    """
    入力された名前の人を噛む
    :param message:
    :return:
    """
    global registered_dict

    if client.user == message.author:
        return

    split_word = message.content.split(' ')
    if len(split_word) < 3:
        await message.channel.send('もう一度試してみてもふ！　半角スペース使ってるか確認してもふ')
        return

    name = split_word[2]
    if name not in registered_dict.keys():
        await message.channel.send('その人はもういないもふ')
        return

    await message.channel.send(f'{name}さんが嚙まれてしまったもふ…')
    registered_dict.pop(name)
    await display_survivor(message)


client.run('')  # ''の間にトークンを記載
