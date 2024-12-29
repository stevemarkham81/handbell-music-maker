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
    'silent_night': [['F', 'Si-'], ['G', '-'], ['F', 'lent'], ['D', 'night'], ['', ''], ['F', 'Ho-'], ['G', '-'], ['F', 'ly'], ['D', 'night'], ['', ''],
                     ['C', 'All'], ['', ''], ['C', 'is'], ['A', 'calm,'], ['', ''], ['A#', 'All'], ['', ''], ['A#', 'is'], ['F', 'bright'], ['', ''],
                     ['G', 'Round'], ['G', 'yon'], ['A#', 'vir-,'], ['A', '-'], ['G', 'gin'], ['F', 'mo-'], ['G', 'ther'], ['F', 'and'], ['D', 'Child'], ['', ''],
                     ['G', 'Ho-'], ['G', 'ly'], ['A#', 'in-,'], ['A', 'fant'], ['G', 'so'], ['F', 'ten-'], ['G', 'der'], ['F', 'and'], ['D', 'mild'], ['', ''],
                     ['C', 'Sleep'], ['C', 'in'], ['D#', 'hea-,'], ['', ''], ['C', 'ven-'], ['A', 'ly'], ['A#', 'pea-'], ['', ''], ['D', 'ce'], ['', ''],
                     ['A#', 'Sle-'], ['F', 'ep'], ['D', 'in'], ['F', 'hea-,'], ['D#', 'ven-'], ['C', 'ly'], ['A#', 'peace']
                    ],

    'away_in_a_manger': [
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

    'hark_the_herald': [
        ['C', 'Hark'], ['F', 'the'], ['F', 'her-'], ['E', 'ald'], ['F', 'an-'], ['A', 'gels'], ['A', 'sing-'], ['G', '-'],

        ['C', 'glo,'], ['C', 'ry'], ['C', 'to'], ['A#', 'the'], ['A', 'new-'], ['G', 'born'], ['A', 'king'], ['', ''],

        ['C', 'Peace'], ['F', 'on'], ['F', 'earth'], ['E', 'and'], ['F', 'mer-'], ['A', 'cy'], ['A', 'mi-'], ['G', 'ld'],

        ['C', 'God'], ['G', 'and'], ['G', 'sin-'], ['E', 'ners'], ['E', 're,'], ['D', 'con-'], ['C', 'ciled'], ['', ''],

        ['C', 'Joy-'], ['C', 'ful'], ['C', 'all'], ['F', 'ye'], ['A#', 'na-'],
        ['A', 'tions'], ['A', 'ri-'], ['G', 'se'],

        ['C', 'Join'], ['C', 'the'], ['C', 'tri-'], ['F', 'umph'], ['A#', 'of'],
        ['A', 'the'], ['A', 'ski-'], ['G', 'es'],

        ['D', 'With'], ['D', 'th an-'], ['D', 'gel-'], ['C', 'ic'], ['A#', 'hosts'],
        ['A', 'pro-'], ['A#', 'claim'],

        ['G', 'Christ'], ['A', 'is-'], ['A#', '-'], ['C', 'born'], ['F', 'in'],
        ['F', 'Beth-'], ['G', 'le-'], ['A', 'hem'],

        ['D', 'Hark'], ['D', 'the'], ['D', 'her-'], ['C', 'ald'], ['A#', 'an-'],
        ['A', 'gels'], ['A#', 'sing'],

        ['G', 'Christ'], ['A', 'is-'], ['A#', '-'], ['C', 'born'], ['F', 'in'],
        ['F', 'Beth-'], ['G', 'le-'], ['F', 'hem']
    ]
}

def draw_note(draw: ImageDraw, x: int, y: int, color: tuple[int, int, int], ring: bool) -> tuple[int, int]:
    if ring:
        print(f'Black circle for {color}')
        draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=color_map['black'])
        draw.ellipse((x-radius+ring_thinkness, y-radius+ring_thinkness, x+radius-ring_thinkness, y+radius-ring_thinkness), fill=color)
    else:    
        draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=color)

img_resolution = (1920, 1080)
image = Image.new('RGB', img_resolution, color=color_map['white'])
draw = ImageDraw.Draw(image)

beats_per_line = 10
num_lines = 10
num_verses = 1

radius = floor(min(img_resolution[0]/(beats_per_line*3+1), img_resolution[1]/(2+num_lines*(3+num_verses))))

x_step = floor(img_resolution[0]/beats_per_line)
y_step = floor(img_resolution[1]/num_lines)


ring_thinkness = max(radius//5, 5)

print(f'radius: {radius}')

x = radius*2
y = radius*2

font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf', size=radius)

for beat in songs['silent_night']:
    note, *lyrics = beat

    if note in color_map:
        draw_note(draw, x, y, color_map[note], '#' in note)
    
    if lyrics:
        for verse,words in enumerate(lyrics):
            w = font.getbbox(words)[2]
            draw.text((x-w/2, y+(radius*(verse+2))), words, fill='black', font=font)
    
    x += x_step
    
    if x > img_resolution[0]:
        x = radius*2
        y += y_step

print(font.size)
image.save('pil_test.png')

exit()


x_max = 12

fig, ax = plt.subplots(figsize=(15, 220))
titleh = plt.title('Silent Night', fontsize=20, va='bottom')
ax.set_xlim(-1, x_max+1)
ax.set_ylim(0, 12)
ax.set_xticks([])
ax.set_yticks([])

start_position = 0
if len(songs['silent_night'][0]) == 2:
    delta_y = 1.8
elif len(songs['silent_night'][0]) == 3:
    delta_y = 2.3
elif len(songs['silent_night'][0]) == 4:
    delta_y = 2.35
else:
    print("Too many verses?")

y = 11.2 - delta_y
note_dy = 0.2 + 0.3 * (len(songs['silent_night'][0]) - 1)

for beat in songs['silent_night']:
    note = beat[0]
    if not note:
        start_position += 1.25
        if start_position > x_max-1:
            start_position = 0
            y -= delta_y
        continue

    if len(note) == 2:  # accidentals get black rings around the note
        rh = plt.Rectangle((start_position, y+note_dy), 1, 1,
                           color=note_color_map[note][0]/255)
        txt_offset = 0.25
    else:
        rh = plt.Rectangle((start_position, y+note_dy), 1, 1,
                           color=note_color_map[note][0]/255)
        txt_offset = 0.32

    th = ax.text(start_position, y+note_dy/2,
                 songs['silent_night'][1][i+1], ha='center', va='bottom')

    e = th.get_window_extent()
    over = (e.xmin + e.width/2) - (start_position + 0.5)
    if over >= 0:
        plt.setp(rh, xy=(start_position+over, y+note_dy))
    else:
        plt.setp(th, xy=(start_position-over, 0))

    rpos = plt.gca().get_window_extent()[1]
    ax.text(rpos[1]+txt_offset, (rpos[2]+note_dy) /
            2, note, color='white', ha='center')

    start_position += 1 + e.width/2
    if start_position > x_max-1:
        start_position = 0
        y -= delta_y

plt.show()
