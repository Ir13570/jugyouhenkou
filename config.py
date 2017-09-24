from schedule import Schedule

mon = Schedule()
tue = Schedule()
wed = Schedule()
thu = Schedule()
fri = Schedule()

mon.classes = [
        'プログラミング',
        'プログラミング',
        '体育',
        '体育',
        '物理',
        '物理',
        '数学B',
        ' '
        ]
tue.classes = [
        '論理回路',
        '論理回路',
        '数学A',
        '国語',
        '創造工学',
        '創造工学',
        'HR',
        ' '
        ]
wed.classes = [
        '英語B',
        '英語B',
        'プログラミング',
        'プログラミング',
        '情報科学工学実験',
        '情報科学工学実験',
        '情報科学工学実験',
        ' '
        ]
thu.classes = [
        '国語',
        '国語',
        '英語A',
        '英語A',
        '化学',
        '化学',
        '数学A',
        '数学A'
        ]
fri.classes = [
        '数学B',
        '数学B',
        '倫理・社会',
        '倫理・社会',
        '歴史',
        '歴史',
        '英語A',
        ' '
        ]


def get_url():
    url = 'http://jyugyou.tomakomai-ct.ac.jp/jyugyou.php?class=J2'
    return url
