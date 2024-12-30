import sys
from PIL import Image, ImageDraw, ImageFont
from math import floor

color_map = {'D2': (255, 106, 0),
             'C2': (190, 0, 0),
             'B':  (146, 0, 108),
             'A#': (13, 152, 240),
             'A':  (0, 0, 153),
             'G#': (51, 204, 204),
             'G':  (0, 205, 200),
             'F#': (6, 250, 99),
             'F':  (0, 152, 0),
             'E':  (255, 192, 0),
             'D#': (250, 120, 74),
             'D':  (255, 106, 0),
             'C#': (223, 52, 92),
             'C':  (238, 0, 0),
             'white': (255, 255, 255),
             'black': (0, 0, 0),
             }  # modified to use the correct RGB values

songs = {
    'christmas_bells': {
        'music': [['B', 'Christ-'], ['B', 'mas'], ['A', 'bells'], ['B', 'are'], ['G', 'ring-'], ['D', 'ing'], ['', ''], ['', ''],
                  ['G', 'Hear'], ['F#', 'what'], ['G', '-'], ['A', 'they'], ['F#', '-'], ['G', 'say'], ['D', 'to'], ['D', 'you'],
                  ['G', 'Je-'], ['F#', 'sus'], ['G', ''], ['A', 'is'], ['F#', ''], ['G', 'born'], ['E', ''], ['', ''],
                  ['C', 'in'], ['D', 'Beth'], ['E', '-'], ['F#', 'le-'], ['G', 'hem'], ['', ''], ['', ''], ['', ''],
                  ['G', 'In'], ['D', 'Beth'], ['E', '-'], ['F#', 'le-'], ['G', 'hem']
                 ],
        'num_lines': 5,
        'beats_per_line': 8,
        'num_verses': 1
    },
    'beautiful_savior': {
        'music': [['D', 'Fair', 'Fair', 'Beau-'],[ '', '', '', ''],
                  ['D', 'is', 'are', 'ti-'],[ 'D', 'the', 'the', 'ful'],[ 'E', 'sun', 'mead', 'Sav-'],
                  ['C#', '-', '-', '-'],[ 'D', 'shine', 'ows', 'ior'],[ '', '', '', ''],
                  ['F#', 'Fair', 'Fair', 'Lord'],[ '', '', '', ''],[ 'F#', '-er', '-er', 'of'],[ 'F#', 'the', 'the', 'the'],
                  ['G', 'moon', 'wood', 'na-'],[ 'E', '-', '-', '-'],[ 'F#', 'light', 'lands', 'tions'],
                  ['A', 'And', 'Robed', 'Son'],[ '', '', '', ''],[ 'D2', 'all', 'in', 'of'],[ 'B', 'the', 'the', ''],[ 'A', 'stars', 'flow-', 'God'],[ '', '', '', ''],
                  ['G', '', 'ers', ''],[ 'F#', 'in', 'of', 'and'],[ 'G', 'heav''n', 'bloom', 'Son'],[ '', '', '', ''],[ 'F#', 'a -', 'ing', 'of'],[ '', '', '', ''],
                  ['E', 'bove', 'spring', 'Man'],[ '', '', '', ''],[ '', '', '', ''],
                  ['A', 'Je-', 'Je-', 'Thee'],[ '', '', '', ''],[ 'B', 'sus', 'sus', 'will'],[ 'A', 'shines', 'is', 'I'],[ 'A', 'bright', 'fair', 'ho-'],[ 'F#', '-', '-', '-'],[ 'G', 'ter', 'er', 'nor'],[ '', '', '', ''],
                  ['G', 'Je-', 'Je-', 'Praise'],[ '', '', '', ''],[ 'A', 'sus', 'sus', 'and'],[ 'G', 'shines', 'is', 'give'],[ 'G', 'pur', 'pur', 'glo-'],[ 'E', '-', '-', '-'],[ 'F#', 'er', 'er', 'ry'],
                  ['F#', 'And', 'He', 'Give'],[ 'F#', 'brings', 'makes', 'praise'],[ 'F#', 'to', 'the', 'and'],[ 'A', 'all', 'sor-', 'glo-'],[ 'G', 'the', 'rowing', 'ry'],
                  ['F#', 'world', 'spir-', 'Ev-'],[ '', '', '', ''],[ 'E', 'his', 'it', 'er'],[ '', '', '', ''],[ 'D', 'love', 'sing', 'more'],[ '', '', '', ''],
                 ],
        'num_lines': 4,
        'beats_per_line': 15,
        'num_verses': 3
    },
    'happy_birthday': {
        'music': [['C', 'Hap'],[ 'C', 'py'],[ 'D', 'Birth'],[ 'C', 'day'],[ 'F', 'to'],[ 'E', 'you'],[ '', ''],
                       ['C', 'Hap'],[ 'C', 'py'],[ 'D', 'Birth'],[ 'C', 'day'],[ 'G', 'to'],[ 'F', 'you'],[ '', ''],
                       ['C', 'Hap'],[ 'C', 'py'],[ 'C2', 'Birth'],[ 'A', 'day'],[ 'F', 'dear'],[ 'E', '___'],[ 'D', '___'],
                       ['A#', 'Hap'],[ 'A#', 'py'],[ 'A', 'Birth'],[ 'F', 'day'],[ 'G', 'to'],[ 'F', 'you'],[ '', ''],
                      ],
        'num_lines': 4,
        'beats_per_line': 7,
        'num_verses': 1
    },
    'samuel_tells': {
        'music': [['G', 'Said', 'A-'],[ 'C', 'Sam-', 'cross'],[ 'A#', '-u-', 'the'],[ 'C', '-el', 'sea'],[ '', '', ''],[ 'D', 'With-', 'in'],[ 'C', 'in', 'Beth-'],[ 'A#', '-', ''],[ 'G', 'five', 'le-'],[ 'G', 'years', 'hem'],[ 'G', 'A', 'Lord'],[ 'F', 'night', 'Je-'],[ 'F', 'will', 'sus'],[ 'F', 'be', 'came'],[ 'D#', 'as', 'to'],[ 'G', 'day', 'earth'],[ '', '', ''],
                     ['G', 'And', 'As'],[ 'C', 'Ba-', 'Sam-'],[ 'A#', '-by', 'u-'],[ 'G', 'Je-', 'el'],[ 'F', '-sus', 'had'],[ 'G', 'will', 'pro-'],[ 'F', '-', '-'],[ 'D#', 'be', 'phe-'],[ 'C', 'born', 'sied'],[ 'C', 'In', 'And'],[ 'D', 'a', ''],[ 'D#', 'land', 'ang-'],[ 'G', 'far', 'els'],[ 'F', 'far', 'sang'],[ 'D#', '', ''],[ 'D', 'a-', 'His'],[ 'C', '-way.', 'birth.'],
                     ['D', 'Ho-', ''],[ 'D#', 'san-', ''],[ '', '', ''],[ 'D#', 'na!', ''],[ 'F', 'Ho-', ''],[ 'G', 'san-', ''],[ 'A#', '', ''],[ 'A#', 'na!', ''],[ '', '', ''],[ 'A#', 'Oh', ''],[ 'C', 'let', ''],[ 'A#', 'us', ''],[ 'G', 'glad-', ''],[ 'A#', 'ly', ''],[ 'F', 'sing', ''],[ '', '', ''],[ '', '', ''],
                     ['F', 'How', ''],[ 'D#', 'bless-', ''],[ 'F', 'ed', ''],[ 'G', 'that', ''],[ 'A#', 'out', ''],[ 'C', 'Lord', ''],[ 'A#', 'was', ''],[ 'G', 'born', ''],[ '', '', ''],[ 'A#', 'Let', ''],[ 'G', 'earth', ''],[ 'F', 're-', ''],[ 'D#', 'ceive', ''],[ 'C', 'her', ''],[ 'D#', 'King!', ''],
                    ],
        'num_lines': 4,
        'beats_per_line': 17,
        'num_verses': 2
    },
    'be_kind': {
        'music': [['C', 'I'],[ 'F', 'want'],[ 'F', 'to'],[ 'F', 'be'],[ 'A', 'kind'],[ 'F', 'to'],[ 'G', 'ev-'],[ 'A#', 'ry-'],[ 'D', 'one,'],
                    ['D', 'For'],[ 'E', 'that'],[ 'G', 'is,'],[ 'A#', 'right,'],[ 'D2', 'you'],[ 'C2', 'see.'],[ '', ''],[ '', ''],[ '', ''],
                    ['C', 'So'],[ 'C', 'I'],[ 'F', 'say'],[ 'F', 'to'],[ 'F', 'my-'],[ 'A', 'self,'],[ 'F', '"Re-'],[ 'G', 'mem'],[ 'A#', 'ber'],[ 'D', 'this:'],
                    ['E', 'Kind-'],[ 'E', 'ness'],[ 'E', 'be-'],[ 'A#', 'gins'],[ 'E', 'with'],[ 'F', 'me."'],
                ],
        'num_lines': 4,
        'beats_per_line': 9,
        'num_verses': 1
    },
    'we_are_different': {
        'music': [['E', 'I'],[ 'C', 'know'],[ 'G', 'you'],[ 'B', 'and'],[ 'B', 'you'],[ 'C', 'know'],[ 'A', 'me.'],[ '', ''],[ '', ''],[ '', ''],[ '', ''],
                         ['B', 'We'],[ 'B', 'are'],[ 'C', 'as'],[ 'D', 'dif-'],[ 'C', 'ferent,'],[ 'B', 'as'],[ 'A', 'the'],[ 'A', 'sun'],[ 'B', 'and'],[ 'A', 'the'],[ 'G', 'sea.'],
                         ['E', 'I'],[ 'C', 'know'],[ 'G', 'you'],[ 'B', 'and'],[ 'B', 'you'],[ 'C', 'know'],[ 'A', 'me.'],[ '', ''],[ '', ''],[ '', ''],[ '', ''],
                         ['B', 'And'],[ 'B', 'that''s,'],[ 'C', 'the'],[ 'D', 'way'],[ 'C', 'that'],[ 'B', 'it''s'],[ 'D', 'sup-'],[ 'D', 'posed'],[ 'C', 'to'],[ 'C', 'be.'],
                        ],
        'num_lines': 4,
        'beats_per_line': 11,
        'num_verses': 1
    },
    'love_one_another': {
        'music': [['F', 'As'],[ 'G', 'I'],[ 'A', 'have'],[ 'C', 'loved'],[ 'C', 'you,'],[ 'D', 'Love'],[ 'E', 'one'],[ 'F', 'an-'],[ 'D', 'oth'],[ 'D', '-er.'], ['', ''],
                         ['G', 'This'],[ 'A', 'new'],[ 'A#', 'com-'],[ 'G', 'man'],[ 'G', '-ment:'],[ 'F', 'Love'],[ 'E', 'one'],[ 'D', 'an-'],[ 'C', 'oth'],[ 'C', '-er.'], ['', ''],
                         ['A', 'By'],[ 'A#', 'this'],[ 'C', 'shall'],[ 'A', 'men'],[ 'D', 'know'],[ 'G', 'Ye'],[ 'G', 'are'],[ 'A', 'my'],[ 'A#', 'dis-'],[ 'G', 'ci-'],[ 'G', 'ples,'],
                         ['F', 'If'],[ 'G', 'ye'],[ 'A', 'have'],[ 'F', 'love'],[ 'D', 'One'],[ 'E', 'to'],[ 'F', 'an-'],[ 'G', 'oth'],[ 'F', '-er.'],
                        ],
        'num_lines': 4,
        'beats_per_line': 11,
        'num_verses': 1
    },
    'be_like_jesus_verse': {
        'music': [['C','I''m'],['D','try-'],['D#','ing'],['F','to'],['F','be'],['C2','like'],['A#','Je-'],['','-'],['D#','sus'],['',''],['',''],
                            ['D#','I''m'],['D','fol-'],['D#','low-'],['F','ing'],['G','in'],['D#','his'],['C','ways.'],['',''],['',''],['',''],['',''],
                            ['C','I''m'],['D','try-'],['D#','ing'],['F','to'],['F','love'],['A#','as'],['A#','he'],['','-'],['D#','did'],['',''],['',''],
                            ['D#','in'],['D','all'],['D#','that'],['F','I'],['G','do'],['G','and'],['A','say.'],['',''],['',''],['',''],['',''],
                            ['A','At'],['A#','times'],['A#','I am'],['A','tempt-'],['F','ed'],['D','to'],['G','make'],['F','a'],['D#','wrong'],['F','choice'],['',''],
                            ['F','But I'],['G','try'],['G','to'],['A','list-'],['F','en'],['F','as the'],['G','still'],['A#','small'],['C2','voice'],['A#','whisp-'],['C2','ers:'],['',''],['',''],['',''],['',''],
                           ],
        'num_lines': 6,
        'beats_per_line': 11,
        'num_verses': 1
    },
    'be_like_jesus_chorus': {
        'music': [['D2','Love'],['D2','one an-'],['D2','other-'],['C2','er'],['A#','as'],['A#','Je-'],['D#','sus'],['G','loves'],['F','you.'],['',''],
                             ['G','Try'],['A','to'],['A#','show'],['F','kind-'],['A#','ness'],['A#','in'],['A#','all'],['C2','that'],['D2','you'],['C2','do.'],
                             ['C2','Be'],['D2','gen-'],['D2','tle and'],['D2','lov-'],['C2','ing'],['A#','in'],['A#','deed'],['A','and'],['G','in'],['F','thought,'],
                             ['D#','For'],['D','these'],['A#','are'],['D','the'],['D#','things'],['C2','Je-'],['A','sus'],['A#','taught.'],
                            ],
        'num_lines': 4,
        'beats_per_line': 10,
        'num_verses': 1
    },
    'be_kind': {
        'music': [['C','I'],['F','want'],['F','to'],['F','be'],['A','kind'],['F','to'],['G','ev-'],['A#','ry-'],['D','one,'],['',''],
                ['D','For'],['E','that'],['G','is,'],['A#','right,'],['D2','you'],['C2','see.'],['',''],['',''],['',''],['',''],
                ['C','So'],['C','I'],['F','say'],['F','to'],['F','my-'],['A','self,'],['F','"Re-'],['G','mem'],['A#','ber'],['D','this:'],
                ['E','Kind-'],['E','ness'],['E','be-'],['A#','gins'],['E','with'],['F','me."'],
               ],
        'num_lines': 4,
        'beats_per_line': 10,
        'num_verses': 1
    },
    'silent_night': {
        'music': [['F', 'Si-'], ['G', '-'], ['F', 'lent'], ['D', 'night'], ['', ''], ['F', 'Ho-'], ['G', '-'], ['F', 'ly'], ['D', 'night'], ['', ''],
                     ['C', 'All'], ['', ''], ['C', 'is'], ['A', 'calm,'], ['', ''], ['A#', 'All'], ['', ''], ['A#', 'is'], ['F', 'bright'], ['', ''],
                     ['G', 'Round'], ['G', 'yon'], ['A#', 'vir-,'], ['A', '-'], ['G', 'gin'], ['F', 'mo-'], ['G', 'ther'], ['F', 'and'], ['D', 'Child'], ['', ''],
                     ['G', 'Ho-'], ['G', 'ly'], ['A#', 'in-,'], ['A', 'fant'], ['G', 'so'], ['F', 'ten-'], ['G', 'der'], ['F', 'and'], ['D', 'mild'], ['', ''],
                     ['C', 'Sleep'], ['C', 'in'], ['D#', 'hea-,'], ['', ''], ['C', 'ven-'], ['A', 'ly'], ['A#', 'pea-'], ['', ''], ['D', 'ce'], ['', ''],
                     ['A#', 'Sle-'], ['F', 'ep'], ['D', 'in'], ['F', 'hea-,'], ['D#', 'ven-'], ['C', 'ly'], ['A#', 'peace']
                    ],
        'num_lines': 6,
        'beats_per_line': 10,
        'num_verses': 1
    },
    'away_in_a_manger': {
        'music': [
                    ['C', 'A-'], ['F', 'way'], ['F', 'in'], ['G', 'a-'], ['A', '-'],
                    ['F', 'man-'], ['F', 'ger'], ['A', 'No-'], ['A#', '-'], ['C', 'crib'],
                    ['C', 'for'], ['D', 'a'], ['A#', 'bed'],
                    ['G', 'The-'], ['A', '-'], ['A#', 'lit-'], ['A#', 'tle'], ['C', 'Lord'],
                    ['A', 'Je-'], ['A', 'sus'], ['F', 'lay-'], ['A', '-'], ['G', 'down'],
                    ['D', 'his'], ['F', 'sweet'], ['E', 'head'],
                    ['C', 'The'], ['F', 'stars'], ['F', 'in'], ['G', 'the-'], ['A', '-'],
                    ['F', 'hea-'], ['F', 'vens'], ['A', 'Looked-'], ['A#', '-'], ['C', 'down'],
                    ['C', 'where'], ['D', 'he'], ['A#', 'lay'],
                    ['G', 'The-'], ['A', '-'], ['A#', 'lit-'], ['A#', 'tle'], ['C', 'Lord'],
                    ['A', 'Je-'], ['A', 'sus'], ['F', 'a-'], ['A', '-'], ['G', 'sleep'],
                    ['D', 'on'], ['E', 'the'], ['F', 'hay']
                ],
        'num_lines': 4,
        'beats_per_line': 13,
        'num_verses': 1
    },
    'hark_the_herald': {
        'music': [
                    ['C', 'Hark'], ['F', 'the'], ['F', 'her-'], ['E', 'ald'], ['F', 'an-'], ['A', 'gels'], ['A', 'sing-'], ['G', '-'],
                    ['C', 'glo,'], ['C', 'ry'], ['C', 'to'], ['A#', 'the'], ['A', 'new-'], ['G', 'born'], ['A', 'king'], ['', ''],
                    ['C', 'Peace'], ['F', 'on'], ['F', 'earth'], ['E', 'and'], ['F', 'mer-'], ['A', 'cy'], ['A', 'mi-'], ['G', 'ld'],
                    ['C', 'God'], ['G', 'and'], ['G', 'sin-'], ['E', 'ners'], ['E', 're,'], ['D', 'con-'], ['C', 'ciled'], ['', ''],
                    ['C', 'Joy-'], ['C', 'ful'], ['C', 'all'], ['F', 'ye'], ['A#', 'na-'],
                    ['A', 'tions'], ['A', 'ri-'], ['G', 'se'],
                    ['C', 'Join'], ['C', 'the'], ['C', 'tri-'], ['F', 'umph'], ['A#', 'of'],
                    ['A', 'the'], ['A', 'ski-'], ['G', 'es'],
                    ['D', 'With'], ['D', 'th an-'], ['D', 'gel-'], ['C', 'ic'], ['A#', 'hosts'],
                    ['A', 'pro-'], ['A#', 'claim'], ['', ''],
                    ['G', 'Christ'], ['A', 'is-'], ['A#', '-'], ['C', 'born'], ['F', 'in'],
                    ['F', 'Beth-'], ['G', 'le-'], ['A', 'hem'],
                    ['D', 'Hark'], ['D', 'the'], ['D', 'her-'], ['C', 'ald'], ['A#', 'an-'],
                    ['A', 'gels'], ['A#', 'sing'], ['', ''],
                    ['G', 'Glo-'], ['A', 'ry'], ['A#', '-'], ['C', 'to'], ['F', 'the'],
                    ['F', 'New-'], ['G', 'born'], ['F', 'King']
                ],
        'num_lines': 4,
        'beats_per_line': 16,
        'num_verses': 1
    },
}

def draw_note(draw: ImageDraw, x: int, y: int, note: str, radius, font) -> tuple[int, int]:
    color = color_map[note]
    ring_thinkness = max(radius//5, 5)
    if '#' in note:
        draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=color_map['black'])
        draw.ellipse((x-radius+ring_thinkness, y-radius+ring_thinkness, x+radius-ring_thinkness, y+radius-ring_thinkness), fill=color)
    else:    
        draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=color)
    w,h = font.getbbox(note)[2:4]
    draw.text((x-w/2, y-h/2), note, fill='white', font=font)

def make_music(song):
    img_resolution = (1920, 1080)
    image = Image.new('RGB', img_resolution, color=color_map['white'])
    draw = ImageDraw.Draw(image)

    if 'music' in songs[song]:
        music = songs[song]['music']
        num_lines = songs[song]['num_lines']
        num_verses = songs[song]['num_verses']
        beats_per_line = songs[song]['beats_per_line']
    else:
        music = songs[song]
        beats_per_line = 10
        num_lines = 10
        num_verses = 1

    radius = floor(min(img_resolution[0]/(beats_per_line*3+1), img_resolution[1]/(2+num_lines*(3+num_verses))))

    x_start = radius*2
    y_start = radius*2
    x_step = radius*3
    y_step = radius*(3+num_verses)

    x = x_start
    y = y_start

    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf', size=radius)

    for beat in music:
        note, *lyrics = beat

        if note in color_map:
            draw_note(draw, x, y, note, radius, font)
        
        if lyrics:
            for verse,words in enumerate(lyrics):
                w,h = font.getbbox(words)[2:4]
                draw.text((x-w/2, y+(radius*(verse+2))-h/2), words, fill='black', font=font)
        
        x += x_step
        
        if x >= x_start + (beats_per_line*x_step) - radius:
            x = x_start
            y += y_step

    image.save(f'{song}.png')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        song = sys.argv[1]
        make_music(song)
    else:
        for song in songs:
            make_music(song)