from .util import Choices


servicemap = {
    'g1': 'ＮＨＫ総合１',
    'g2': 'ＮＨＫ総合２',
    'e1': 'ＮＨＫＥテレ１',
    'e2': 'ＮＨＫＥテレ２',
    'e3': 'ＮＨＫＥテレ３',
    'e4': 'ＮＨＫワンセグ２',
    's1': 'ＮＨＫＢＳ１',
    's2': 'ＮＨＫＢＳ１(１０２ｃｈ)',
    's3': 'ＮＨＫＢＳプレミアム',
    's4': 'ＮＨＫＢＳプレミアム(１０４ｃｈ)',
    'r1': 'ＮＨＫラジオ第1',
    'r2': 'ＮＨＫラジオ第2',
    'r3': 'ＮＨＫＦＭ',
    'n1': 'ＮＨＫネットラジオ第1',
    'n2': 'ＮＨＫネットラジオ第2',
    'n3': 'ＮＨＫネットラジオＦＭ',
    'tv': 'テレビ全て',
    'radio': 'ラジオ全て',
    'netradio': 'ネットラジオ全て'}


class Service(object):
    def __init__(self, code, name):
        self.code = code
        self.name = name

code_map = {}
name_map = {}
for code, name in servicemap.items():
    area = Service(code, name)
    code_map[code] = area
    name_map[name] = area

ServiceChoices = Choices(Service, code_map, name_map)
