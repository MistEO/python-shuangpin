from pyshuangpin import shuangpin, Scheme
import pypinyin

hans = '今天天气不错，我喜欢用小鹤双拼'
print(hans)
sp = shuangpin(hans, Scheme.小鹤, style=pypinyin.NORMAL)
print(sp)
