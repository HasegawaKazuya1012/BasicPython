text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

#type(text) = str

# TODO
#text.splitdeで半角スペースで英文を区切り,.をstrip(',.')でカウントしないようにする
words = [word.strip(',.') for word in text.split()]
#map関数でlen関数をwordsに適用する
lengths = list(map(len , words))
#join関数を用いて文字数を連結させる
answer = """""".join(map(str, lengths))

print(answer)