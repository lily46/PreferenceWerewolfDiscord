# PreferenceWerewolfDiscord
## これは何？
性癖人狼というゲームを考えたので，Discord上で遊べるようにしました．\\
ルールは簡単，皆で性癖を出し合って，ランダムに選ばれた性癖について皆で語ります．\\
性癖がバレないように上手く誤魔化したり，逆に知ったかぶりしたり自由に議論しながら誰の性癖か当てましょう！
## 準備
1. コンソール上で`pip install discord.py`を実行
2. [Discord公式](https://discordpy.readthedocs.io/ja/latest/discord.html#discord-intro)に従ってbotを作成し，トークンをゲット
3. `main.py`の最後の行の`""`の中にトークンを記載
## botの実行
コンソール上で`python main.py`を実行\\
(Herokuなどでbotを常時起動することもできます)
## 遊び方
1. ゲーム用のチャンネルで`/game /start`を誰かが送信
2. bot宛にDMで`/game /register 性癖の名前`を送信
3. ゲーム用のチャンネルで`/game /discuss`を誰かが送信
4. 募集されたお題がランダムに一つ出てくるので，一人ずつそのお題について語る
5. 話を聞いて，誰がお題を出した人か当てる
6. ゲーム用のチャンネルで`/game /answer`を誰かが送信
7. 誰の性癖か開示されるので，もう一度1.の手順から繰り返そう！
