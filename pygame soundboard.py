import pygame

pygame.init()

############## Intro Page ##############

# Screen
screen = pygame.display.set_mode((520,700))
screen.fill((200,250,250))
pygame.display.set_caption('Majora\'s Mask: Instrument Soundboard')

# Titles
zelda_font = pygame.font.Font('HyliaSerifBeta-Regular.otf', 30)
zelda_font2 = pygame.font.Font('HyliaSerifBeta-Regular.otf', 25)
title = zelda_font.render('Majora\'s Mask', True, (150,0,255))
song_list_title = zelda_font2.render('Song List', True, (0,0,0))
screen.blit(title, (10,0))
screen.blit(song_list_title, (20,250))

# Images
intro_image = pygame.image.load('Majora\'s_Mask.png')
screen.blit(intro_image, (175, 50))
pygame.display.set_icon(intro_image)

staff = pygame.image.load('oot_staff.png')
screen.blit(staff, (25, 500))

############## Rectangle Button Creation ##############

def rec_buttons(size, font, x, y, title_list, button_list):
    ''' (tup, Font, int, int, list of str) -> None
    Creates a column of rectangular buttons with a height and width
    described in size at position (x,y). Places each title text from title_list
    into the corresponding buttons with the specified font.
    '''
    for title in title_list:
        button_rec = pygame.Rect((x, y), size)
        button = pygame.draw.rect(screen, (0,0,0), button_rec)
        button_list.append((button, title))
        text = font.render(title, True, (255,255,255))
        if len(title) < 8:
            screen.blit(text, (x + 12, y))
        else:
            screen.blit(text, (x + 2, y + 7))
        y += 40


############## Instrument Selection ##############

instrument = 'OCARINA'

# Instrument Button Features
button_size = (120, 30)
button_font = pygame.font.Font('FRABK_0.TTF', 25)

button_x = 25
button_y = 60

instrument_titles = ['OCARINA', 'PIPES', 'DRUMS', 'GUITAR']
instrument_buttons = []

rec_buttons(button_size, button_font, button_x, button_y,
            instrument_titles, instrument_buttons)

# Instrument Pictures

def instrument_pic(instrument):
    replacement_rec = pygame.Rect((175, 50), (160, 140))
    replacement = pygame.draw.rect(screen, (200,250,250), replacement_rec)
    if instrument == 'OCARINA':
        image = pygame.image.load('ocarina.png')
    elif instrument == 'PIPES':
        image = pygame.image.load('Pipes_of_Awakening.png')
    elif instrument == 'DRUMS':
        image = pygame.image.load('drums goron.png')
    elif instrument == 'GUITAR':
        image = pygame.image.load('Guitar_of_Waves.png')
    screen.blit(image, (175, 50))
    pygame.display.update()


########### Music Buttons ############

# Controller Music Buttons

a_button_pic = pygame.image.load('a_button.png')
c_left_pic = pygame.image.load('l_c.png')
c_right_pic = pygame.image.load('r_c.png')
c_down_pic = pygame.image.load('d_c.png')
c_up_pic = pygame.image.load('u_c.png')

button_pics = {a_button_pic: (345, 135) , c_left_pic: (350, 57),
               c_right_pic: (450, 60), c_down_pic: (400, 100),
               c_up_pic:(403, 15)} 
buttons = []

for (pic, pos) in button_pics.items():
    button = screen.blit(pic, pos)
    buttons.append(button)

a_button = buttons[0] #D1
c_left = buttons[1] #B
c_right = buttons[2] #A
c_down = buttons[3] #F
c_up = buttons[4] #D2


# Note Sound Functions

def note_D1(instrument):
    ''' (str) -> None
    Plays the low D note sound with the instrument specified.
    Note D1 plays when the a_button is pressed.
    '''
    if instrument == 'OCARINA':
        sound = pygame.mixer.Sound('OOT_Notes_Ocarina_D_med.wav')
    elif instrument == 'PIPES':
        sound = pygame.mixer.Sound('MM_Notes_Pipes_D_med.wav')
    elif instrument == 'DRUMS':
        sound = pygame.mixer.Sound('MM_Notes_Drums_D_long.wav')
    elif instrument == 'GUITAR':
        sound = pygame.mixer.Sound('MM_Notes_Guitar_D_med.wav')
    sound.play()
    
def note_F(instrument):
    ''' (str) -> None
    Plays the F note sound with the instrument specified.
    Note F plays when the c_down button is pressed.
    '''
    if instrument == 'OCARINA':
        sound = pygame.mixer.Sound('OOT_Notes_Ocarina_F_med.wav')
    elif instrument == 'PIPES':
        sound = pygame.mixer.Sound('MM_Notes_Pipes_F_med.wav')
    elif instrument == 'DRUMS':
        sound = pygame.mixer.Sound('MM_Notes_Drums_F_long.wav')
    elif instrument == 'GUITAR':
        sound = pygame.mixer.Sound('MM_Notes_Guitar_F_med.wav')
    sound.play()


def note_A(instrument):
    ''' (str) -> None
    Plays the A note sound with the instrument specified.
    Note A plays when the c_right button is pressed.
    '''
    if instrument == 'OCARINA':
        sound = pygame.mixer.Sound('OOT_Notes_Ocarina_A_med.wav')
    elif instrument == 'PIPES':
        sound = pygame.mixer.Sound('MM_Notes_Pipes_A_med.wav')
    elif instrument == 'DRUMS':
        sound = pygame.mixer.Sound('MM_Notes_Drums_A_long.wav')
    elif instrument == 'GUITAR':
        sound = pygame.mixer.Sound('MM_Notes_Guitar_A_med.wav')
    sound.play()

def note_B(instrument):
    ''' (str) -> None
    Plays the B note sound with the instrument specified.
    Note B plays when the c_left button is pressed.
    '''
    if instrument == 'OCARINA':
        sound = pygame.mixer.Sound('OOT_Notes_Ocarina_B_med.wav')
    elif instrument == 'PIPES':
        sound = pygame.mixer.Sound('MM_Notes_Pipes_B_med.wav')
    elif instrument == 'DRUMS':
        sound = pygame.mixer.Sound('MM_Notes_Drums_B_long.wav')
    elif instrument == 'GUITAR':
        sound = pygame.mixer.Sound('MM_Notes_Guitar_B_med.wav')
    sound.play()

def note_D2(instrument):
    ''' (str) -> None
    Plays the high D note sound with the instrument specified.
    Note D2 plays when the a_button is pressed.
    '''
    if instrument == 'OCARINA':
        sound = pygame.mixer.Sound('OOT_Notes_Ocarina_D2_med.wav')
    elif instrument == 'PIPES':
        sound = pygame.mixer.Sound('MM_Notes_Pipes_D2_med.wav')
    elif instrument == 'DRUMS':
        sound = pygame.mixer.Sound('MM_Notes_Drums_D2_long.wav')
    elif instrument == 'GUITAR':
        sound = pygame.mixer.Sound('MM_Notes_Guitar_D2_med.wav')
    sound.play()


# Play Sound Button Function

def play_note(mouse_position=(0,0), note_pic=None):
    ''' (tup, Surface) -> None
    Plays the note corresponding to the music button that was pressed.
    Otherwise, plays the note corresponding to note_pic.
    '''
    if a_button.collidepoint(mouse_position) or note_pic == a_button_pic:
        note_D1(instrument)
    elif c_left.collidepoint(mouse_position) or note_pic == c_left_pic:
        note_B(instrument)
    elif c_right.collidepoint(mouse_position) or note_pic == c_right_pic:
        note_A(instrument)
    elif c_down.collidepoint(mouse_position) or note_pic == c_down_pic:
        note_F(instrument)
    elif c_up.collidepoint(mouse_position) or note_pic == c_up_pic:
        note_D2(instrument)
    

########### Song List ############

song = None

# Song Button Features
button_size = (140, 30)
button_x, button_y = 25, 300
button_font = pygame.font.Font('FRABK_0.TTF', 13)

song_titles = ['Song of Time', 'Song of Double Time', 'Inverted Song of Time',
               'Song of Healing', 'Song of Storms', 'Epona\'s Song',
               'Song of Soaring', 'Sonata of Awakening', 'Goron Lullaby',
               'New Wave Bossa Nova', 'Elegy of Emptiness', 'Oath to Order']
song_buttons = []

rec_buttons(button_size, button_font, button_x, button_y, song_titles[:4],
            song_buttons)

button_x += 165
rec_buttons(button_size, button_font, button_x, button_y,
            song_titles[4:8], song_buttons)

button_x += 165
rec_buttons(button_size, button_font, button_x, button_y,
            song_titles[8:], song_buttons)


# Staff Note Placement

staff_heights = []

note_x = 100
note_separation = 50

note_y = {a_button_pic: 615, c_left_pic: 555, c_right_pic: 570,
          c_down_pic: 590, c_up_pic: 535}


def note_placement(note_order, x, separation):
    ''' (list, int, int) -> None
    Places the music note pictures in the order note_order on the music staff,
    starting at position x with a note spearation of separation. Plays each note's
    corresponding sound.
    '''
    screen.blit(staff, (25, 500))
    for note in note_order:
        play_note(note_pic=note)
        screen.blit(note, (x, note_y[note]))
        pygame.display.update()
        pygame.time.delay(550)
        x += separation


# Song Functions

def Song_of_Time():
    order = [c_right_pic, a_button_pic, c_down_pic, c_right_pic,
             a_button_pic, c_down_pic]
    note_placement(order, note_x, note_separation)
def Song_of_DTime():
    order = [c_right_pic, c_right_pic, a_button_pic, a_button_pic,
             c_down_pic, c_down_pic]
    note_placement(order, note_x, note_separation)
def Inv_Song_of_Time():
    order = [c_down_pic, a_button_pic, c_right_pic, c_down_pic,
             a_button_pic, c_right_pic]
    note_placement(order, note_x, note_separation)
def Song_of_Healing():
    order = [c_left_pic, c_right_pic, c_down_pic, c_left_pic,
             c_right_pic, c_down_pic]
    note_placement(order, note_x, note_separation)
def Song_of_Storms():
    order = [a_button_pic, c_down_pic, c_up_pic, a_button_pic,
             c_down_pic, c_up_pic]
    note_placement(order, note_x, note_separation)
def Epona_Song():
    order = [c_up_pic, c_left_pic, c_right_pic, c_up_pic,
             c_left_pic, c_right_pic]
    note_placement(order, note_x, note_separation)
def Song_of_Soaring():
    order = [c_down_pic, c_left_pic, c_up_pic, c_down_pic,
             c_left_pic, c_up_pic]
    note_placement(order, note_x, note_separation)
def Sonata_Awakening():
    order = [c_up_pic, c_left_pic, c_up_pic, c_left_pic,
             a_button_pic, c_right_pic, a_button_pic]
    note_placement(order, note_x, note_separation)
def Goron_Lullaby():
    order = [a_button_pic, c_right_pic, c_left_pic, a_button_pic,
             c_right_pic, c_left_pic, c_right_pic, a_button_pic]
    note_placement(order, note_x, note_separation)
def NW_Bossa_Nova():
    order = [c_left_pic, c_up_pic, c_left_pic, c_right_pic,
             c_down_pic, c_left_pic, c_right_pic]
    note_placement(order, note_x, note_separation)
def Elegy_of_Emptiness():
    order = [c_right_pic, c_left_pic, c_right_pic, c_down_pic,
             c_right_pic, c_up_pic, c_left_pic]
    note_placement(order, note_x, note_separation)
def Oath_to_Order():
    order = [c_right_pic, c_down_pic, a_button_pic, c_down_pic,
             c_right_pic, c_up_pic]
    note_placement(order, note_x, note_separation)
    

# Play Song Button Function
def play_song(mouse_pos):
    song_functions = [Song_of_Time, Song_of_DTime, Inv_Song_of_Time,
                      Song_of_Healing, Song_of_Storms, Epona_Song,
                      Song_of_Soaring, Sonata_Awakening, Goron_Lullaby,
                      NW_Bossa_Nova, Elegy_of_Emptiness, Oath_to_Order]
    for (button, title) in song_buttons:
        index = song_buttons.index((button, title))
        if button.collidepoint(mouse_pos):
            song_functions[index]()




pygame.display.update()


if __name__ == '__main__':
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for (button, title) in instrument_buttons:
                    if button.collidepoint(mouse_pos):
                        instrument = title
                        instrument_pic(instrument)
                play_note(mouse_pos)
                play_song(mouse_pos)
            if event.type == pygame.QUIT:
                pygame.quit()

