from .util import Choices


areamap = {
    '010': '札幌',
    '011': '函館',
    '012': '旭川',
    '013': '帯広',
    '014': '釧路',
    '015': '北見',
    '016': '室蘭',
    '020': '青森',
    '030': '盛岡',
    '040': '仙台',
    '050': '秋田',
    '060': '山形',
    '070': '福島',
    '080': '水戸',
    '090': '宇都宮',
    '100': '前橋',
    '110': 'さいたま',
    '120': '千葉',
    '130': '東京',
    '140': '横浜',
    '150': '新潟',
    '160': '富山',
    '170': '金沢',
    '180': '福井',
    '190': '甲府',
    '200': '長野',
    '210': '岐阜',
    '220': '静岡',
    '230': '名古屋',
    '240': '津',
    '250': '大津',
    '260': '京都',
    '270': '大阪',
    '280': '神戸',
    '290': '奈良',
    '300': '和歌山',
    '310': '鳥取',
    '320': '松江',
    '330': '岡山',
    '340': '広島',
    '350': '山口',
    '360': '徳島',
    '370': '高松',
    '380': '松山',
    '390': '高知',
    '400': '福岡',
    '401': '北九州',
    '410': '佐賀',
    '420': '長崎',
    '430': '熊本',
    '440': '大分',
    '450': '宮崎',
    '460': '鹿児島',
    '470': '沖縄'}


class Area(object):
    def __init__(self, code, name):
        self.code = code
        self.name = name

code_map = {}
name_map = {}
for code, name in areamap.items():
    area = Area(code, name)
    code_map[code] = area
    name_map[name] = area

AreaChoices = Choices(Area, code_map, name_map)
