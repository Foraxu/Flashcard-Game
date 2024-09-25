from tkinter import *
import data


BACKGROUND_COLOR = "#B1DDC6"

DATA_FILE = 'data/english_words.csv'
RIGHT_IMG = 'images/right.png'
WRONG_IMG = 'images/wrong.png'
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 750
FLASH_CARD_X = 515
FLASH_CARD_Y = 300
CARD_BACK_IMG = 'images/card_back.png'
CARD_FRONT_IMG = 'images/card_front.png'
BACKGROUND_COLOR = "#B1DDC6"

# --------------------- Setup UI

# Window

root = Tk()
root.title('Flash Card')
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Images

cardback_img = PhotoImage(file=CARD_BACK_IMG)
cardfront_img = PhotoImage(file=CARD_FRONT_IMG)
cards = {
    0: {
        'text': 'English',
        'image': cardback_img
    },
    1: {
        'text': 'Portuguese',
        'image': cardfront_img
    }
}
right_img = PhotoImage(file=RIGHT_IMG)
wrong_img = PhotoImage(file=WRONG_IMG)


# Canvas

canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, highlightthickness=0, bg=BACKGROUND_COLOR) # Create a canvas that holds all the images
flash_card = canvas.create_image(FLASH_CARD_X, FLASH_CARD_Y, image=cardback_img)
canvas.grid(column=1, row=1)
# canvas.itemconfig(flash_card, image=cardfront_img)

top_text = canvas.create_text(500, 100, text='', font=('Arial', 30, 'italic'))
central_text = canvas.create_text(500, 280, text='', font=('Arial', 30, 'bold'))

# Buttons

right_button = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, border=0)
wrong_button = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, border=0)
right_button.place(x=700, y=650)
wrong_button.place(x=270, y=650)

index = 0

def regressive_counting(times):
    canvas.itemconfig(central_text, text=f'{times}')
    if times > 0:
        root.after(1000, regressive_counting, times-1)
    else:
        start()

# TODO 
def start():

    first_language_word = data.get_random_word()
    second_language_word = data.df_dict[first_language_word]

    canvas.itemconfig(central_text, text=first_language_word)
    
    root.after(3000, flipcard)

    canvas.itemconfig(central_text, text=second_language_word)




def flipcard():
    global index
    index += 1
    if index > 1:
        index = 0
    canvas.itemconfig(flash_card, image=cards[index]['image'])
    canvas.itemconfig(top_text, text=cards[index]['text'])

regressive_counting(3)

right_button.config(command=flipcard)

root.mainloop()
