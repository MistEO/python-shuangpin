from pyshuangpin.scheme import Scheme, xiaohe

import pypinyin


def shuangpin(hans, scheme: Scheme, **kwargs):
    pinyin = pypinyin.pinyin(hans, **kwargs)
    if scheme == Scheme.Xiaohe:
        scheme_dict = xiaohe.scheme
    else:
        raise NotImplementedError('scheme not implemented')

    for key, value in scheme_dict.items():
        for item in pinyin:
            for index in range(len(item)):
                item[index] = item[index].replace(key, value)

    return pinyin
