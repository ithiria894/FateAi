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