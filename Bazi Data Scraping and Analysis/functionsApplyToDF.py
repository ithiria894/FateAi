from functions import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import string
import nltk

def GetBazi(man_df):
    man_df['bazi_man'] = man_df['Groom_Birth_Date'].apply(lambda x: getBazi(int(x.strftime('%Y')), int(x.strftime('%m')), int(x.strftime('%d')), 0) if not pd.isnull(x) else None)


def getGanzhi(year):
    gan = '甲乙丙丁戊己庚辛壬癸'
    zhi = '子丑寅卯辰巳午未申酉戌亥'
    offset = 4  # the year 庚子 starts in 2020
    stem = gan[(year - offset) % 10]
    branch = zhi[(year - offset) % 12]
    return stem + branch

# man_df['year_ganzi'] = man_df['all_years'].apply(lambda x: getGanzhi(x))

def strongWeak(man_df):
    man_df['強弱得令'] = man_df.apply(lambda row: 強弱得令(row['man日干'], row['man月支']), axis=1)
    man_df['強弱地支三會'] = man_df.apply(lambda row: 強弱地支三會(row['man日干'], row['man日支'], row['man月支'], row['man年支']), axis=1)
    man_df['強弱地支三合'] = man_df.apply(lambda row: 強弱地支三合(row['man日干'], row['man日支'], row['man月支'], row['man年支']), axis=1)
    man_df['強弱得地'] = man_df.apply(lambda row: 強弱得地(row['man日干'], row['man日支'], row['man年支']), axis=1)
    man_df['強弱得勢'] = man_df.apply(lambda row: 強弱得勢(row['man日干'], row['man月干'], row['man年干']), axis=1)
    man_df['強弱地支半三合'] = man_df.apply(lambda row: 強弱地支半三合(row['man日干'], row['man日支'], row['man月支'], row['man年支']), axis=1)
    man_df['強弱地支半三會'] = man_df.apply(lambda row: 強弱地支半三會(row['man日干'], row['man日支'], row['man月支'], row['man年支']), axis=1)

    man_df['強弱印的數量'] = man_df.apply(lambda row: 強弱印的數量(row['man日干'], row['man日支'], row['man月干'], row['man月支'], row['man年干'], row['man年支']), axis=1)
    man_df['身強身弱'] = ''
    for index, row in man_df.iterrows():
        if row['強弱得令']:
            man_df.at[index, '身強身弱'] = '強'
        elif row['強弱地支三會']:
            man_df.at[index, '身強身弱'] = '強'
        elif row['強弱地支三合']:
            man_df.at[index, '身強身弱'] = '強'
        elif 強弱印的數量(row['man日干'], row['man日支'], row['man月干'], row['man月支'], row['man年干'], row['man年支']) == 4:
            man_df.at[index, '身強身弱'] = '強'
        elif row['強弱地支半三會']:
            man_df.at[index, '身強身弱'] = '可能強'
        elif row['強弱地支半三合']:
            man_df.at[index, '身強身弱'] = '可能強'
        elif 強弱印的數量(row['man日干'], row['man日支'], row['man月干'], row['man月支'], row['man年干'], row['man年支']) == 3:
            man_df.at[index, '身強身弱'] = '可能強'
        elif row['強弱得地']:
            man_df.at[index, '身強身弱'] = '可能強'
        elif row['強弱得勢']:
            man_df.at[index, '身強身弱'] = '可能強'
        else:
            man_df.at[index, '身強身弱'] = '弱'

def map_dangpai(value):

    dangpai_mapping = {
        "印": "同黨",
        "比劫": "同黨",
        "官": "異黨",
        "食傷": "異黨",
        "財": "異黨"
    }

    return dangpai_mapping.get(value, "")


def baziwuxingyingyang(man_df):
    columns_to_cross = ['man年干', 'man年支', 'man月干', 'man月支', 'man日干', 'man日支']

    # Create feature cross combinations
    feature_cross_cols = []
    for col1 in columns_to_cross:
        for col2 in ['五行', '阴阳']:
            feature_cross_cols.append(col1 + '_' + col2)

    # Perform feature cross and store the results in new columns
    for col in columns_to_cross:
        man_df[col + '_五行'] = man_df[col].map(wu_xing_dict)
        man_df[col + '_阴阳'] = man_df[col].map(yin_yang_dict)
        man_df[col + '_五行_阴阳'] = man_df[col + '_五行'] + '_' + man_df[col + '_阴阳']

    # Perform feature cross using pandas' get_dummies function
    man_df_features = pd.get_dummies(man_df[feature_cross_cols])

    # Concatenate the original DataFrame with the feature cross DataFrame
    man_df = pd.concat([man_df, man_df_features], axis=1)

def bazishishen(man_df):
    columns_to_cross = ['man年干', 'man年支', 'man月干', 'man月支', 'man日支']

    # Create feature cross combinations
    feature_cross_cols = []
    for col1 in columns_to_cross:
        for col2 in ['十神']:
            feature_cross_cols.append(col1 + '_' + col2)

    # Perform feature cross and store the results in new columns
    for col in columns_to_cross:
        man_df[col + '_十神'] = man_df.apply(lambda x: shi_shen(x['man日干'], x[col]), axis=1)
        

    # Perform feature cross using pandas' get_dummies function
    man_df_features = pd.get_dummies(man_df[feature_cross_cols])

    # Concatenate the original DataFrame with the feature cross DataFrame
    man_df = pd.concat([man_df, man_df_features], axis=1)


def benming(man_df):
    man_df['本命日支六合'] = man_df.apply(lambda x: 'yes' if is_liuhe(x['man日支'], x['man月支']) or is_liuhe(x['man日支'], x['man年支']) else 'no', axis=1)

    # check_sanhe
    man_df['本命日支三合'] = man_df.apply(lambda x: 'yes' if check_sanhe(x['man日支'], x['man月支'],x['man年支']) else 'no', axis=1)
    man_df['本命日支三合屬性'] = man_df.apply(lambda x: check_fullsanhe(x['man日支'], x['man月支'], x['man年支']), axis=1)

def generateFeatures(man_df):
    man_df['流年天干'] = man_df['year_ganzi'].str[0]
    man_df['流年地支'] = man_df['year_ganzi'].str[1]

    # 流年地支=year_ganzi[1]
    # 流年天干=year_ganzi[0]
    #日支伏吟
    #if year_ganzi[1] equal man日支, then True, else False, and create new column named man日支同年支
    man_df['man日支同年支'] = man_df.apply(lambda row: True if row['man日支'] == row['year_ganzi'][1] else False, axis=1)
    #日支六沖
    #if man日支 and 流年支 is liuchong, then True, else False, and create new column named man日支六沖
    man_df['man日支六沖'] = man_df.apply(lambda row: is_liuchong(row['man日支'], row['year_ganzi'][1]), axis=1)


    #日支六合
    #if man日支 and 流年支 is_liuhe, then True, else False, and create new column named man日支六合
    man_df['man日支六合'] = man_df.apply(lambda row: is_liuhe(row['man日支'], row['year_ganzi'][1]), axis=1)

    # 流年天干十神
    # create new column named man流年天干十神 using shi_shen function, and pass in col man日主 and col ['year_ganzi'][0]
    man_df['man流年天干十神'] = man_df.apply(lambda x: shi_shen(x['man日干'], x['year_ganzi'][0]), axis=1)

    # 流年地支十神
    man_df['man流年地支十神'] = man_df.apply(lambda x: shi_shen(x['man日干'], x['year_ganzi'][1]), axis=1)


    #財透干
    #create new column named man財透干, if man流年天干十神 is 偏財 or 正財, then True, else False
    man_df['man財透干'] = man_df['man流年天干十神'].apply(lambda x: True if x in ['偏財', '正財'] else False)
    # man_df['man財透干2'] = man_df['man流年天干十神'].apply(lambda x: True if x in ['偏財', '正財'] else False)
    #財得地
    #create new column named man財得地, if man流年地支十神 is 偏財 or 正財, then True, else False
    man_df['man財得地'] = man_df['man流年地支十神'].apply(lambda x: True if x in ['偏財', '正財'] else False)
    # man_df['man財得地2'] = man_df['man流年地支十神'].apply(lambda x: True if x in ['偏財', '正財'] else False)
    #大運流年天地合


    #流年有傷官

    #日干五合
    # create new column named man日干五合, if man日干 and 流年天干 is is_wuhe, then True, else False
    man_df['man日干五合'] = man_df.apply(lambda row: is_wuhe(row['man日干'], row['year_ganzi'][0]), axis=1)



    #流年日柱天地合
    #if man日支六合 is True and man日干五合 is true, then True, else False
    man_df['man日柱天地合'] = man_df.apply(lambda row: True if row['man日支六合'] and row['man日干五合'] else False, axis=1)

    #流年雙體財
    man_df['man流年雙體財'] = man_df.apply(lambda row: True if row['man財透干'] and row['man財得地'] else False, axis=1)


    # man_df['man日干支關係'] = man_df.apply(lambda row: gan_zhi_relation(row['man日干'], row['man日支']), axis=1)


    #create new col named man日支半三合, if man日支 和 流年支 is 半三合, then True, else False
    

    man_df['流年日支三合屬性'] = man_df.apply(lambda x: check_fullsanhe(x['man日支'], x['man月支'], x['year_ganzi'][1]) or check_fullsanhe(x['man日支'], x['man年支'], x['year_ganzi'][1]), axis=1)
    man_df['流年本命三合屬性'] = man_df.apply(lambda x: check_fullsanhe(x['man月支'], x['man年支'], x['year_ganzi'][1]), axis=1)
    man_df['流年日支三合五神'] = man_df.apply(lambda x: get_shenke_interaction(x['man日干'], x['流年日支三合屬性']), axis=1)
    man_df['流年本命三合五神'] = man_df.apply(lambda x: get_shenke_interaction(x['man日干'], x['流年本命三合屬性']), axis=1)


    # man_df['man日支半三合'] = man_df.apply(lambda row: check_halfsanhe(row['man日支'], row['year_ganzi'][1]) if row['流年日支三合屬性'] is None else None, axis=1)

    man_df['日支流年三合出財'] = man_df['流年日支三合五神'].apply(lambda x: True if x in ['財'] else False)
    man_df['日支流年三合出食傷'] = man_df['流年日支三合五神'].apply(lambda x: True if x in ['食傷'] else False)

    man_df['本命流年三合出財'] = man_df['流年本命三合五神'].apply(lambda x: True if x in ['財'] else False)
    man_df['本命流年三合出食傷'] = man_df['流年本命三合五神'].apply(lambda x: True if x in ['食傷'] else False)
    #create new col named man日支半三合, if man日支 和 流年支 is 半三合, then True, else False


    man_df['流年日支三會屬性'] = man_df.apply(lambda x: check_fullsanhui(x['man日支'], x['man月支'], x['year_ganzi'][1]) or check_fullsanhui(x['man日支'], x['man年支'], x['year_ganzi'][1]), axis=1)
    man_df['流年本命三會屬性'] = man_df.apply(lambda x: check_fullsanhui(x['man月支'], x['man年支'], x['year_ganzi'][1]), axis=1)
    man_df['流年日支三會五神'] = man_df.apply(lambda x: get_shenke_interaction(x['man日干'], x['流年日支三會屬性']), axis=1)
    man_df['流年本命三會五神'] = man_df.apply(lambda x: get_shenke_interaction(x['man日干'], x['流年本命三會屬性']), axis=1)

    # man_df['man日支半三會局'] = man_df.apply(lambda row: check_halfsanhuì(row['man日支'], row['year_ganzi'][1]) if row['流年日支三會屬性'] is None else None, axis=1)


    #日支六合
    #if man日支 and 流年支 is_liuhe, then True, else False, and create new column named man日支六合
    man_df['man日支暗合'] = man_df.apply(lambda row: check_anhe(row['man日支'], row['year_ganzi'][1]), axis=1)


    #日干五沖

    man_df['man日干五沖'] = man_df.apply(lambda row: check_clash(row['man日干'], row['year_ganzi'][0]), axis=1)

    #半三刑
    man_df['man半三刑'] = man_df.apply(lambda row: check_semi_triple_punishment(row['man日支'], row['year_ganzi'][1]), axis=1)

    #六害
    man_df['man六害'] = man_df.apply(lambda row: check_six_harms(row['man日支'], row['year_ganzi'][1]), axis=1)

    man_df['man流年天干五神'] = man_df['man流年天干十神'].apply(map_wushen)
    man_df['man流年地支五神'] = man_df['man流年地支十神'].apply(map_wushen)

    man_df['man流年天干黨派'] = man_df['man流年天干五神'].apply(map_dangpai)
    man_df['man流年地支黨派'] = man_df['man流年地支五神'].apply(map_dangpai)

    
    # check_sanhuì



def CountTenGod(man_df):
    wealth_characters = ['偏財', '正財']
    man_df['年月有多少財'] = man_df[['man年干_十神', 'man年支_十神', 'man月干_十神', 'man月支_十神']].apply(lambda x: sum(1 for char in x if char in wealth_characters), axis=1)

    guan_characters =['正官', '七殺']
    man_df['年月有多少官'] = man_df[['man年干_十神', 'man年支_十神', 'man月干_十神', 'man月支_十神']].apply(lambda x: sum(1 for char in x if char in guan_characters), axis=1)