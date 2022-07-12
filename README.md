# python-shuangpin

汉字转双拼 (pyshuangpin)

## 用法

```python
# from samply.py

from pyshuangpin import shuangpin, Scheme
import pypinyin

hans = '今天天气不错，我喜欢小鹤双拼'
print(hans)
sp = shuangpin(hans, Scheme.小鹤, style=pypinyin.NORMAL)
print(sp)
```

## 双拼支持

目前支持的双拼方案:

- 小鹤
- 自然码
- 搜狗
- 微软
- 智能 ABC
