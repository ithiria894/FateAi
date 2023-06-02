import dicts


def check_liuhe(di_zhi1, di_zhi2):
    """
    判斷兩個地支是否六合

    參數:
    di_zhi1 (str): 第一個地支，比如"子"、"丑"等等。
    di_zhi2 (str): 第二個地支，比如"子"、"丑"等等。

    返回:
    bool: 如果兩個地支六合，返回True；否則返回False。
    """
    # 申子辰合水，寅午戌合火，巳酉丑合金，亥卯未合木
    he_dict = {
        "申": ["子", "辰"],
        "子": ["申", "辰"],
        "辰": ["申", "子"],
        "寅": ["午", "戌"],
        "午": ["寅", "戌"],
        "戌": ["寅", "午"],
        "巳": ["酉", "丑"],
        "酉": ["巳", "丑"],
        "丑": ["巳", "酉"],
        "亥": ["卯", "未"],
        "卯": ["亥", "未"],
        "未": ["亥", "卯"]
    }
    
    # 檢查兩個地支是否六合
    if di_zhi2 in he_dict[di_zhi1]:
        return True
    else:
        return False


def count_liuhe(ba_zi):
    """
    計算八字中有幾對六合

    參數:
    ba_zi (str): 八字，由四個地支和四個天干組成，比如"甲子丙寅戊午"。

    返回:
    int: 六合的對數，如果沒有六合，返回0。
    """
    liuhe_count = 0

    # 八字中每兩個相鄰的地支進行六合判斷
    for i in range(0, 8, 2):
        di_zhi1 = ba_zi[i]
        di_zhi2 = ba_zi[i+2] if i < 6 else ba_zi[0]  # 如果到了最後一對，第二個地支要和第一個地支六合
        if check_liuhe(di_zhi1, di_zhi2):
            liuhe_count += 1

    return liuhe_count


def count_liuhe(dizhi_str):
    """
    計算地支字符串中有幾對六合

    參數:
    dizhi_str (str): 包含任意數量地支的字符串，比如"子丑寅卯"。

    返回:
    int: 六合的對數，如果沒有六合，返回0。
    """
    if len(dizhi_str) < 2:  # 如果地支數量小於2，沒有六合
        return 0

    liuhe_count = 0

    # 地支字符串中每兩個相鄰的地支進行六合判斷
    for i in range(len(dizhi_str) - 1):
        di_zhi1 = dizhi_str[i]
        di_zhi2 = dizhi_str[i+1]
        if check_liuhe(di_zhi1, di_zhi2):
            liuhe_count += 1

    # 如果地支數量大於等於2，還要檢查第一個地支和最後一個地支是否六合
    if len(dizhi_str) >= 2 and check_liuhe(dizhi_str[0], dizhi_str[-1]):
        liuhe_count += 1

    return liuhe_count



import sys
sys.path.append(r"C:\Users\TOSHIBA\Documents\Github\FateAi\crystal-bazi")
# import main
import metaphysic


def get_bazi(year,month,day,hour):
    ba=metaphysic.bazi(year,month,day,hour)
    ba=ba.split("-")
    bazi=[]
    for i in ba:
        # print(i.split())
        bazi.append(i[0])
        bazi.append(i[1])
    return bazi


def get_ganzi(year):
    tiangan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
    dizhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

    tiangan_index = (year - 4) % 10
    dizhi_index = (year - 4) % 12

    return f"{tiangan[tiangan_index]}{dizhi[dizhi_index]}"



def is_liuchong(s1, s2):
    liuchong_dict = {
        '子': '午',
        '丑': '未',
        '寅': '申',
        '卯': '酉',
        '辰': '戌',
        '巳': '亥',
        '午': '子',
        '未': '丑',
        '申': '寅',
        '酉': '卯',
        '戌': '辰',
        '亥': '巳'
    }
    
    return liuchong_dict.get(s1) == s2


zodiac_stem_dict = {
    "子": ["癸"],
    "丑": ["癸", "辛", "己"],
    "寅": ["甲", "丙", "戊"],
    "卯": ["乙"],
    "辰": ["乙", "戊", "癸"],
    "巳": ["庚", "丙", "戊"],
    "午": ["丁", "己"],
    "未": ["乙", "己", "丁"],
    "申": ["庚", "壬", "戊"],
    "酉": ["辛"],
    "戌": ["辛", "丁", "戊"],
    "亥": ["壬", "甲"]
}

def printBazi(df):
    for index, row in df.iterrows():
        print(f"{row['man日干']}{row['man月干']}{row['man年干']}|{row['dayun'][0]}{row['Year_marriage_ganzhi'][0]}")
        print(f"{row['man日支']}{row['man月支']}{row['man年支']}|{row['dayun'][1]}{row['Year_marriage_ganzhi'][1]}")
        collist=[]
        for col in row.columns:
            if col.type == "bool":
                if row[col]==True:
                    collist.append(col)


        print(collist)
        print()

#check 日支 和 流年支 is 暗合
def check_anhe(di_zhi1, di_zhi2):
    """
    判斷兩個地支是否暗合

    參數:
    di_zhi1 (str): 第一個地支，比如"子"、"申"等等。
    di_zhi2 (str): 第二個地支，比如"子"、"申"等等。

    返回:
    bool: 如果兩個地支暗合，返回True；否則返回False。
    """
    # 子巳暗合、寅午暗合、巳酉暗合、卯申暗合、亥午暗合，共五组

    anhe_dict = {
    
        "寅": ["丑"],
        "丑": ["寅"],
        "卯": ["申"],
        "申": ["卯"],
        "亥": ["午"],
        "午": ["亥"]
    }

    # 檢查兩個地支是否在暗合字典的key中
    if di_zhi1 not in anhe_dict.keys():
        return False
    if di_zhi2 not in anhe_dict.keys():
        return False
    
    
    # 檢查兩個地支是否暗合
    if di_zhi2 in anhe_dict[di_zhi1]:
        return True
    else:
        return False
    

# def check_halfsanhuì(di_zhi1, di_zhi2):
#     """
#     判斷兩個地支是否半三會局

#     參數:
#     di_zhi1 (str): 第一個地支，比如"子"、"申"等等。
#     di_zhi2 (str): 第二個地支，比如"子"、"申"等等。

#     返回:
#     bool: 如果兩個地支半三會局，返回True；否則返回False。
#     """

#     # 申子辰會局，寅午戌會局，巳酉丑會局，亥卯未會局
#     sanhuiju_dict = {
#         "寅": ["卯", "辰"],
#         "卯": ["寅", "辰"],
#         "辰": ["寅", "卯"],
#         "巳": ["午", "未"],
#         "午": ["巳", "未"],
#         "未": ["巳", "午"],
#         "申": ["酉", "戌"],
#         "酉": ["申", "戌"],
#         "戌": ["申", "酉"],
#         "亥": ["子", "丑"],
#         "子": ["亥", "丑"],
#         "丑": ["亥", "子"]
#     }
    
#     # 檢查兩個地支是否半三會局
#     if di_zhi2 in sanhuiju_dict[di_zhi1]:
#         return True
#     else:
#         return False
    
def check_halfsanhuì(di_zhi1, di_zhi2):
    """
    判斷兩個地支是否半三會局

    參數:
    di_zhi1 (str): 第一個地支，比如"子"、"申"等等。
    di_zhi2 (str): 第二個地支，比如"子"、"申"等等。

    返回:
    bool: 如果兩個地支半三會局，返回True；否則返回False。
    """

    # 申子辰會局，寅午戌會局，巳酉丑會局，亥卯未會局
    sanhuiju_dict = {
        "寅": ["卯", "辰"],
        "卯": ["寅", "辰"],
        "辰": ["寅", "卯"],
        "巳": ["午", "未"],
        "午": ["巳", "未"],
        "未": ["巳", "午"],
        "申": ["酉", "戌"],
        "酉": ["申", "戌"],
        "戌": ["申", "酉"],
        "亥": ["子", "丑"],
        "子": ["亥", "丑"],
        "丑": ["亥", "子"]
    }
    
    # 檢查兩個地支是否半三會局
    if di_zhi2 in sanhuiju_dict[di_zhi1]:
        return True
    else:
        return False


#     #日支 和 流年支 is 半三合 
# def check_halfsanhe(di_zhi1, di_zhi2):
#     """
#     判斷兩個地支是否半三合

#     參數:
#     di_zhi1 (str): 第一個地支，比如"子"、"申"等等。
#     di_zhi2 (str): 第二個地支，比如"子"、"申"等等。

#     返回:
#     bool: 如果兩個地支六合，返回True；否則返回False。
#     """
#     # 申子辰合水，寅午戌合火，巳酉丑合金，亥卯未合木
#     he_dict = {
#         "申": ["子", "辰"],
#         "子": ["申", "辰"],
#         "辰": ["申", "子"],
#         "寅": ["午", "戌"],
#         "午": ["寅", "戌"],
#         "戌": ["寅", "午"],
#         "巳": ["酉", "丑"],
#         "酉": ["巳", "丑"],
#         "丑": ["巳", "酉"],
#         "亥": ["卯", "未"],
#         "卯": ["亥", "未"],
#         "未": ["亥", "卯"]
#     }
    
#     # 檢查兩個地支是否半三合
#     if di_zhi2 in he_dict[di_zhi1]:
#         return True
#     else:
#         return False
    
    #日支 和 流年支 is 半三合 
def check_halfsanhe(di_zhi1, di_zhi2):
    """
    判斷兩個地支是否半三合

    參數:
    di_zhi1 (str): 第一個地支，比如"子"、"申"等等。
    di_zhi2 (str): 第二個地支，比如"子"、"申"等等。

    返回:
    bool: 如果兩個地支六合，返回True；否則返回False。
    """
    # 申子辰合水，寅午戌合火，巳酉丑合金，亥卯未合木
    he_dict = {
        "申": ["子"],
        "子": ["申","辰"],
        "辰": ["子"],

        "寅": ["午"],
        "午": ["寅","戌"],
        "戌": ["午"],
        
        "巳": ["酉"],
        "酉": ["巳","丑"],
        "丑": ["酉"],

        "亥": ["卯"],
        "卯": ["亥","未"],
        "未": ["卯"]
    }
    
    # 檢查兩個地支是否半三合
    if di_zhi2 in he_dict[di_zhi1]:
        return True
    else:
        return False

def check_sanhe(di_zhi1, di_zhi2, di_zhi3):
    """
    判斷三個地支是否三合

    參數:
    di_zhi1 (str): 第一個地支，比如"子"、"申"等等。
    di_zhi2 (str): 第二個地支，比如"子"、"申"等等。
    di_zhi3 (str): 第三個地支，比如"子"、"申"等等。

    返回:
    bool: 如果三個地支三合，返回True；否則返回False。
    """
    # 申子辰合水，寅午戌合火，巳酉丑合金，亥卯未合木
    he_dict = {
        "申": ["子", "辰"],
        "子": ["申", "辰"],
        "辰": ["申", "子"],
        "寅": ["午", "戌"],
        "午": ["寅", "戌"],
        "戌": ["寅", "午"],
        "巳": ["酉", "丑"],
        "酉": ["巳", "丑"],
        "丑": ["巳", "酉"],
        "亥": ["卯", "未"],
        "卯": ["亥", "未"],
        "未": ["亥", "卯"]
    }

    # 檢查三個地支是否三合且不相同
    if di_zhi2 in he_dict[di_zhi1] and di_zhi3 in he_dict[di_zhi1] and di_zhi2 != di_zhi3:
        return True
    else:
        return False



def gan_zhi_relation(日干, 日支):
    日干屬性 = wu_xing_dict[日干]
    日支屬性 = wu_xing_dict[日支]
    if 日干屬性 in sheng_dict[日支屬性]:
        return "日支生日干"
    elif 日干屬性 in ke_dict[日支屬性]:
        return "日支剋日干"
    elif 日干屬性 == 日支屬性:
        return "比和"
    elif 日支屬性 in ke_dict[日干屬性]:
        return "日干剋日支"
    elif 日支屬性 in sheng_dict[日干屬性]:
        return "日干生日支"
    



def shi_shen(日主,天干或地支):
    日主屬性 = wu_xing_dict[日主]
    日主陰陽 = yin_yang_dict[日主]
    屬性 = wu_xing_dict[天干或地支]
    陰陽 = yin_yang_dict[天干或地支]

    if 日主陰陽 == 陰陽: 
        if 日主屬性 == 屬性:
            return "比肩"
        elif 屬性 in ke_dict[日主屬性]:
            return "偏財"
        elif 屬性 in sheng_dict[日主屬性]:
            return "食神"
        elif 日主屬性 in ke_dict[屬性]:
            return "七殺"
        elif 日主屬性 in sheng_dict[屬性]:
            return "偏印"
    else:
        if 日主屬性 == 屬性:
            return "劫財"
        elif 屬性 in ke_dict[日主屬性]:
            return "正財"
        elif 屬性 in sheng_dict[日主屬性]:
            return "傷官"
        elif 日主屬性 in ke_dict[屬性]:
            return "正官"
        elif 日主屬性 in sheng_dict[屬性]:
            return "正印"
        


def is_liuchong(s1, s2):
    liuchong_dict = {
        '子': '午',
        '丑': '未',
        '寅': '申',
        '卯': '酉',
        '辰': '戌',
        '巳': '亥',
        '午': '子',
        '未': '丑',
        '申': '寅',
        '酉': '卯',
        '戌': '辰',
        '亥': '巳'
    }
    
    return liuchong_dict.get(s1) == s2

def is_liuhe(str1, str2):
    liuhe_dict = {
        '子': '丑',
        '丑': '子',
        '寅': '亥',
        '卯': '戌',
        '辰': '酉',
        '巳': '申',
        '午': '未',
        '未': '午',
        '申': '巳',
        '酉': '辰',
        '戌': '卯',
        '亥': '寅'
    }
    
    if liuhe_dict.get(str1) == str2:
        return True
    else:
        return False
    
def is_wuhe(str1, str2):
    wuhe_pairs = ['甲己', '乙庚', '丙辛', '丁壬', '戊癸']
    if str1 + str2 in wuhe_pairs or str2 + str1 in wuhe_pairs:
        return True
    else:
        return False
shishen_dict = {
    '甲': {'甲': '比肩', '乙': '劫財', '丙': '食神', '丁': '傷官', '戊': '偏財', '己': '正財', '庚': '七殺', '辛': '正官', '壬': '偏印', '癸': '正印'},
    '乙': {'甲': '劫財', '乙': '比肩', '丙': '傷官', '丁': '食神', '戊': '正財', '己': '偏財', '庚': '正官', '辛': '七殺', '壬': '正印', '癸': '偏印'},
    '丙': {'甲': '偏印', '乙': '正印', '丙': '比肩', '丁': '劫財', '戊': '食神', '己': '傷官', '庚': '偏財', '辛': '正財', '壬': '七殺', '癸': '正官'},
    '丁': {'甲': '正印', '乙': '偏印', '丙': '劫財', '丁': '比肩', '戊': '傷官', '己': '食神', '庚': '正財', '辛': '偏財', '壬': '正官', '癸': '七殺'},
    
    '戊': {'甲': '七殺', '乙': '正官', '丙': '偏印', '丁': '正印', '戊': '比肩', '己': '劫財', '庚': '食神', '辛': '傷官', '壬': '偏財', '癸': '正財'},
    
    '己': {'甲': '正官', '乙': '七殺', '丙': '正印', '丁': '偏印', '戊': '劫財', '己': '比肩', '庚': '傷官', '辛': '食神', '壬': '正財', '癸': '偏財'},
    
    '庚': {'甲': '偏財', '乙': '正財', '丙': '七殺', '丁': '正官', '戊': '偏印', '己': '正印', '庚': '比肩', '辛': '劫財', '壬': '食神', '癸': '傷官'},
    
    '辛': {'甲': '正財','乙': '偏財','丙': '正官','丁': '七殺','戊': '正印','己': '偏印','庚': '劫財','辛': '比肩','壬': '傷官','癸': '食神'},
    
    '壬': {'甲': '食神','乙': '傷官','丙': '偏財','丁': '正財','戊': '七殺','己': '正官','庚': '偏印','辛': '正印','壬': '比肩','癸': '劫財'},
    
    '癸': {'甲': '傷官','乙': '食神','丙': '正財','丁': '偏財','戊': '正官','己': '七殺','庚': '正印','辛': '偏印','壬': '劫財','癸': '比肩'}
    }

wuxingDicForTiangan = {
    "甲": "木",
    "乙": "木",
    "丙": "火",
    "丁": "火",
    "戊": "土",
    "己": "土",
    "庚": "金",
    "辛": "金",
    "壬": "水",
    "癸": "水"
}
wuxingDicForDizhi = {
    "子": "水",
    "丑": "土",
    "寅": "木",
    "卯": "木",
    "辰": "土",
    "巳": "火",
    "午": "火",
    "未": "土",
    "申": "金",
    "酉": "金",
    "戌": "土",
    "亥": "水"
}

yin_yang_dict = {
    '甲': '陽',
    '乙': '陰',
    '丙': '陽',
    '丁': '陰',
    '戊': '陽',
    '己': '陰',
    '庚': '陽',
    '辛': '陰',
    '壬': '陽',
    '癸': '陰',
    '子': '陰',
    '丑': '陰',
    '寅': '陽',
    '卯': '陰',
    '辰': '陽',
    '巳': '陰',
    '午': '陽',
    '未': '陰',
    '申': '陽',
    '酉': '陰',
    '戌': '陽',
    '亥': '陽'
}

wu_xing_dict = {
    "甲": "木",
    "乙": "木",
    "丙": "火",
    "丁": "火",
    "戊": "土",
    "己": "土",
    "庚": "金",
    "辛": "金",
    "壬": "水",
    "癸": "水",
    "子": "水",
    "丑": "土",
    "寅": "木",
    "卯": "木",
    "辰": "土",
    "巳": "火",
    "午": "火",
    "未": "土",
    "申": "金",
    "酉": "金",
    "戌": "土",
    "亥": "水"
}

tianganwuhe = {
    '甲': '木',
    '乙': '木',
    '丙': '火',
    '丁': '火',
    '戊': '土',
    '己': '土',
    '庚': '金',
    '辛': '金',
    '壬': '水',
    '癸': '水'
}

ke_dict = {
    '金': ['木'],
    '木': ['土'],
    '水': ['火'],
    '火': ['金'],
    '土': ['水']
}

sheng_dict = {
    '金': ['水'],
    '木': ['火'],
    '水': ['木'],
    '火': ['土'],
    '土': ['金']
}

shenke = {
    '木': {'水': '印', '火': '食傷', '金': '官', '土': '財', '木': '比劫'},
    '火': {'木': '印', '土': '食傷', '金': '財', '水': '官', '火': '比劫'},
    '土': {'金': '食傷', '水': '財', '火': '印', '木': '官', '土': '比劫'},
    '金': {'土': '印', '火': '官', '水': '食傷', '木': '財', '金': '比劫'},
    '水': {'火': '財', '木': '食傷', '土': '官', '金': '印', '水': '比劫'}
}


#日干五沖
def check_clash(gan1, gan2):
    """
    Determines if there is a clash (相衝) between two heavenly stems (日干).

    Arguments:
    gan1 (str): The first heavenly stem.
    gan2 (str): The second heavenly stem.

    Returns:
    bool: True if there is a clash, False otherwise.
    """
    clashes = {
        "甲": "庚",
        "庚": "甲",
        "乙": "辛",
        "辛": "乙",
        "壬": "丙",
        "丙": "壬",
        "癸": "丁",
        "丁": "癸"
    }

    return clashes.get(gan1, False) == gan2


def check_semi_triple_punishment(zhi1, zhi2):
    """
    Determines if there is a "半三刑" (semi-triple punishment) between two zodiac signs.

    Arguments:
    zhi1 (str): The first zodiac sign.
    zhi2 (str): The second zodiac sign.

    Returns:
    bool: True if there is a "半三刑", False otherwise.丑未戌三刑
    """
    semi_triple_punishment = {
        "寅": ["巳", "申"],
        "巳": ["寅", "申"],
        "申": ["寅", "巳"],
        "丑": ["未", "戌"],
        "未": ["丑", "戌"],
        "戌": ["丑", "未"]
    }

    if zhi1 in semi_triple_punishment and zhi2 in semi_triple_punishment[zhi1]:
        return True
    else:
        return False


def check_six_harms(zhi1, zhi2):
    """
    Determines if there is a "六害" (six harms) relationship between two zodiac signs.

    Arguments:
    zhi1 (str): The first zodiac sign.
    zhi2 (str): The second zodiac sign.

    Returns:
    bool: True if there is a "六害", False otherwise.
    """
    six_harms = {
        "子": "未",
        "未": "子",
        "丑": "午",
        "午": "丑",
        "寅": "巳",
        "巳": "寅",
        # "卯": "辰",
        # "辰": "卯",
        "申": "亥",
        "亥": "申",
        "酉": "戌",
        "戌": "酉"
    }

    if six_harms.get(zhi1) == zhi2:
        return True
    else:
        return False
def map_wushen(value):
    """
    Maps the values of 'man流年天干十神' to the corresponding 'man流年天干五神'.

    Arguments:
    value (str): The value of 'man流年天干十神'.

    Returns:
    str: The mapped value of 'man流年天干五神'.
    """
    wushen_mapping = {
        "偏財": "財",
        "正財": "財",
        "七殺": "官",
        "偏官": "官",
        "正官": "官",
        "偏印": "印",
        "正印": "印",
        "比肩": "比劫",
        "劫財": "比劫",
        "食神": "食傷",
        "傷官": "食傷"
    }

    return wushen_mapping.get(value, "")






#定身強弱
sanhui = {
    '木': ['寅', '卯', '辰'],
    '火': ['巳', '午', '未'],
    '金': ['申', '酉', '戌'],
    '水': ['亥', '子', '丑'],
    '土': ['辰','戌','丑','未' ]
}

sanhe = {
    '火': ['寅', '午', '戌'],
    '水': ['申', '子', '辰'],
    '金': ['巳', '酉', '丑'],
    '木': ['亥', '卯', '未'],
    '土': [ '辰','戌','丑','未' ]
}

def 強弱得令(man日干,man月支):
    if man月支 in sanhui[wu_xing_dict[man日干]]:
        return True
    else:
        return False
    
def 強弱得地(man日干,man日支,man年支):
    wx=wu_xing_dict[man日干]
    if wx==wu_xing_dict[man日支] and wx==wu_xing_dict[man年支]:
        return True
    else:
        return False

def 強弱得勢(man日干,man月干,man年干):
    wx=wu_xing_dict[man日干]
    if wx==wu_xing_dict[man月干] or wx==wu_xing_dict[man年干]:
        return True
    else:
        return False

# def 地支半三合(man日干,man日支,man月支,man年支):
    # wx=wu_xing_dict[man日干]
    # if any of two from (man日支,man月支,man年支) are distinct and in sanhui[wx], then true


# def 地支三合(man日干,man日支,man月支,man年支):
#     wx=wu_xing_dict[man日干]
    # if all man日支,man月支,man年支 are distinct and in sanhui[wx], then true


def 強弱地支半三合(man日干, man日支, man月支, man年支):
    wx = wu_xing_dict[man日干]
    zodiacs = sanhe[wx]
    distinct_zodiacs = {man日支, man月支, man年支}
    common_zodiacs = set(zodiacs).intersection(distinct_zodiacs)
    return len(common_zodiacs) >= 2


def 強弱地支三合(man日干, man日支, man月支, man年支):
    wx = wu_xing_dict[man日干]
    zodiacs = sanhe[wx]
    distinct_zodiacs = {man日支, man月支, man年支}
    return distinct_zodiacs.issubset(zodiacs) and len(distinct_zodiacs) == 3

def 強弱地支半三會(man日干, man日支, man月支, man年支):
    wx = wu_xing_dict[man日干]
    zodiacs = sanhui[wx]
    distinct_zodiacs = {man日支, man月支, man年支}
    common_zodiacs = set(zodiacs).intersection(distinct_zodiacs)
    return len(common_zodiacs) >= 2


def 強弱地支三會(man日干, man日支, man月支, man年支):
    wx = wu_xing_dict[man日干]
    zodiacs = sanhui[wx]
    distinct_zodiacs = {man日支, man月支, man年支}
    return distinct_zodiacs.issubset(zodiacs) and len(distinct_zodiacs) == 3

sheng_dict = {
    '金': ['水'],
    '木': ['火'],
    '水': ['木'],
    '火': ['土'],
    '土': ['金']
}
# def 印的數量(man日干, man日支, man月干,man月支, man年干,man年支):
    # if man日支, man月干,man月支, man年干,man年支 are 印 of man日干, then return 5
    # if sheng_dict[man日支] == wu_xing_dict[man日干], then it is 印

def 強弱印的數量(man日干, man日支, man月干, man月支, man年干, man年支):

    count = 0
    if sheng_dict[wu_xing_dict[man日支]] == wu_xing_dict[man日干]:
        count += 1
    if sheng_dict[wu_xing_dict[man月干]] == wu_xing_dict[man日干]:
        count += 1
    if sheng_dict[wu_xing_dict[man月支]] == wu_xing_dict[man日干]:
        count += 1
    if sheng_dict[wu_xing_dict[man年干]] == wu_xing_dict[man日干]:
        count += 1
    if sheng_dict[wu_xing_dict[man年支]] == wu_xing_dict[man日干]:
        count += 1
    return count

def printBazi(df):
    for index, row in df.iterrows():
        print(f"{row['man日干']}{row['man月干']}{row['man年干']}|{row['dayun'][0]}{row['Year_marriage_ganzhi'][0]}")
        print(f"{row['man日支']}{row['man月支']}{row['man年支']}|{row['dayun'][1]}{row['Year_marriage_ganzhi'][1]}")
        collist = [col for col in row.index if row[col] and df[col].dtype == 'bool']
        print(collist)
        print()


# def check_sanhe(di_zhi1, di_zhi2, di_zhi3):
#     """
#     判斷三個地支是否三合

#     參數:
#     di_zhi1 (str): 第一個地支，比如"子"、"申"等等。
#     di_zhi2 (str): 第二個地支，比如"子"、"申"等等。
#     di_zhi3 (str): 第三個地支，比如"子"、"申"等等。

#     返回:
#     bool: 如果三個地支三合，返回True；否則返回False。
#     """
#     # 申子辰合水，寅午戌合火，巳酉丑合金，亥卯未合木
#     he_dict = {
#         "申": ["子", "辰"],
#         "子": ["申", "辰"],
#         "辰": ["申", "子"],
#         "寅": ["午", "戌"],
#         "午": ["寅", "戌"],
#         "戌": ["寅", "午"],
#         "巳": ["酉", "丑"],
#         "酉": ["巳", "丑"],
#         "丑": ["巳", "酉"],
#         "亥": ["卯", "未"],
#         "卯": ["亥", "未"],
#         "未": ["亥", "卯"]
#     }

#     # 檢查三個地支是否三合且不相同
#     if di_zhi2 in he_dict[di_zhi1] and di_zhi3 in he_dict[di_zhi1] and di_zhi2 != di_zhi3:
#         return True
#     else:
#         return False
    



def check_fullsanhe(s1, s2, s3):
    if s1 == s2 or s1 == s3 or s2 == s3:
        return None

    sanhe = {
        '火': ['寅', '午', '戌'],
        '水': ['申', '子', '辰'],
        '金': ['巳', '酉', '丑'],
        '木': ['亥', '卯', '未'],
    }

    for key, values in sanhe.items():
        if s1 in values and s2 in values and s3 in values:
            return key
    
    return None


def get_shenke_interaction(key, value):
    shenke = {
        '木': {'水': '印', '火': '食傷', '金': '官', '土': '財', '木': '比劫'},
        '火': {'木': '印', '土': '食傷', '金': '財', '水': '官', '火': '比劫'},
        '土': {'金': '食傷', '水': '財', '火': '印', '木': '官', '土': '比劫'},
        '金': {'土': '印', '火': '官', '水': '食傷', '木': '財', '金': '比劫'},
        '水': {'火': '財', '木': '食傷', '土': '官', '金': '印', '水': '比劫'}
    }

    if key in shenke and value in shenke[key]:
        return shenke[key][value]
    else:
        return None


def check_fullsanhui(s1, s2, s3):
    if s1 == s2 or s1 == s3 or s2 == s3:
        return None

    sanhui = {
    '木': ['寅', '卯', '辰'],
    '火': ['巳', '午', '未'],
    '金': ['申', '酉', '戌'],
    '水': ['亥', '子', '丑'],
    # '土': ['辰','戌','丑','未' ]
    }

    for key, values in sanhui.items():
        if s1 in values and s2 in values and s3 in values:
            return key
    
    return None