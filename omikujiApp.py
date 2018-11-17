import random

omikuji = ["大吉", "吉", "凶"]

# 配列0~2
key = random.randint(0, 2)

print("今日の運勢は " + omikuji[key] + " です。")
