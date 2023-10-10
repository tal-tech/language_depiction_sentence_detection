import sys
from module.description import Description

if __name__ == "__main__":
    desc = Description()
    state, description = desc.init()
    print(state, description)
    if state < 0:
        sys.exit(0)

    sentence_list = [

        '我的妈妈先推开门，再xiān开被子接着说：“起床了起床了。”妈妈走出了房门。' # 语言

    ]
    state, desc_info = desc.get_all_descriptions(sentence_list)
    if desc_info['num'] == 1:
        print("是语言描写")
    else:
        print("不是语言描写")
    # print('描写数目', desc_info['num'])
    # for k,v in desc_info['info'].items():
    #     print(k)
    #     print(v)
    #     print()
    # print(desc_info)
