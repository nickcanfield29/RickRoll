from tkinter import *
import webbrowser
from PIL import ImageTk, Image
import matplotlib.pyplot as plt


def on_click():
    global click_count
    click_count += 1
    second_window = Toplevel()
    second_window.geometry("500x500")
    second_window.title(("Click Count: " + str(click_count) + ". You Positive?!"))
    canvas2 = Canvas(second_window, width=300, height=300)
    canvas2.pack()
    img2 = foo(path='Rickdancing.jpg')
    canvas2.create_image(20, 20, anchor=NW, image=img2)
    button2 = Button(second_window, text="Yes. Duh", command=on_click2)
    button2.pack()
    second_window.mainloop()


def on_click2():
    global click_count
    click_count += 1
    third_window = Toplevel()
    third_window.title(("Click Count: " + str(click_count) + ". 100% Positive!"))
    third_window.geometry("500x500")
    canvas3 = Canvas(third_window, width=300, height=300)
    canvas3.pack()
    img2 = foo(path='secondchance.jpg')
    canvas3.create_image(20, 20, anchor=NW, image=img2)
    button3 = Button(third_window, text="Yes, for Fuck's Sake. Just Rick Roll Me!", command=on_click3)
    button3.pack()
    third_window.mainloop()


def on_click3():
    global click_count
    click_count += 1
    fourth_window = Toplevel()
    fourth_window.geometry("500x500")
    fourth_window.title(("Click Count: " + str(click_count) + ". Last Chance! You sure!").__str__())
    canvas4 = Canvas(fourth_window, width=300, height=300)
    canvas4.pack()
    img2 = foo(path='Ricktheman.jpg')
    canvas4.create_image(20, 20, anchor=NW, image=img2)
    button4 = Button(fourth_window, text="Yes. Rick Roll Me Baby!", command=on_click4)
    button4.pack()
    fourth_window.mainloop()


def on_click4():
    global click_count
    click_count += 1
    url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    webbrowser.register('chrome',
                        None,
                        webbrowser.BackgroundBrowser(
                            "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(url)

    if click_count > 5:
        print("Okay, that's enough Rick Rolling!")
        print("You're a Master Roller!")
        plt.close("all")
        exit()


def start_program():
    global click_count
    click_count += 1
    root = Tk()
    title = str("Click Count: " + str(click_count) + ". Rick Rolling!")
    root.title(title)
    root.geometry("500x500")
    canvas = Canvas(root, width=300, height=300)
    canvas.pack()
    img2 = foo(path='Ricktheman.jpg')
    canvas.create_image(20, 20, anchor=NW, image=img2)
    button = Button(root, text="Rick Roll it?", command=on_click)
    button.pack()
    root.mainloop()


def foo(path):
    img = ImageTk.PhotoImage(Image.open(path))
    return img


click_count = 0
start_program()
