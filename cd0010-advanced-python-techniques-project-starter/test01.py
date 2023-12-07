import csv

def test001():
    with open('data/neos.csv', "r") as f:
        reader = csv.DictReader(f)
        cnt = 0
        cntN = 0 
        cntND = 0
        for line in reader:
            if cnt < 1:
                print(line['pdes'])
            if line['name'] == 'Apollo':
                print(line['diameter'])
            if len(line['name']) == 0:
                cntN += 1
            if len(line['diameter']) == 0:
                cntND += 1
            cnt += 1
            
        print(cnt)
        print(cnt - cntN)
        print(cnt - cntND)
        
#test001()

import json

def test002():
    with open('data/cad.json') as f:
        reader = json.load(f)
        print(reader['count'])
        # key signature   count    fields    data    
        
        # "signature":{"source":"NASA/JPL SBDB Close Approach Data API","version":"1.1"}
        # "count":"406785"
        #  "fields":["des","orbit_id","jd","cd","dist","dist_min","dist_max","v_rel","v_inf","t_sigma_f","h"]
        
        # des - 小惑星または彗星の主な名称 (例: 443、2000 SG344)
        # orbit_id - 軌道ID
        # jd - 大接近時刻 (JD エフェメリス時刻)
        # cd - 接近時刻 (フォーマットされたカレンダー日付/時刻、UTC)
        # dist - 公称接近距離 (au)
        # dist_min - 最小 (3 シグマ) 接近距離 (au)
        # dist_max - 最大 (3 シグマ) 接近距離 (au)
        # v_rel - 接近時の接近本体に対する相対速度 (km/s)
        # v_inf - 無質量体に対する相対速度 (km/s)
        # t_sigma_f - 最接近時間の 3 シグマの不確実性 (日、時間、分でフォーマットされます。ゼロの場合、日数は含まれません。例「13:02」は 13 時間 2 分です。例「2_09:08」は 2)日9時間8分）
        # h - 絶対等級 H (mag)
        
        des = 0
        cd = 3
        dist = 4
        v_rel = 7
        
        data = reader['data']
        print(data[0][3])
        flag = '1900-Jan-01' in data[0][3]
        print(flag)
        cnt = 0
        for list in data:
            if '2000-Jan-01' in list[3]:
                if list[0] == '2015 CL':
                    print('2015 CL', " ", list[4])
                if list[0] == '2002 PB':
                    print('2002 PB',  ' ', list[7])
       
        
#test002()

def test003():
    with open('data/neos.csv') as cf:
        reader = csv.DictReader(cf)
        pset = set()
        for line in reader:
            a = line['name']
            if a == "":
                print("[]") 
            else:
                print(a)
            #pset.add(line['pha'])
        #print(pset)
        
#test003()

des = 0
cd = 3
dist = 4
v_rel = 7



def test004():
    with open('data/cad.json') as jf:
        reader = json.load(jf)
        for line in reader['data']:
            num = float(line[dist])
            print(num)

#test004()
