from tkinter import *
from tkinter import colorchooser
from PIL import Image, ImageDraw
import PIL

WIDTH,HEIGHT = 500, 500
WHITE = (255, 255, 255)

class PaintGUI:

    def __init__(self):

        # langa darom
        self.root = Tk()
        self.root.title("Paint")

        # piestuka darom
        self.brush_width = 15
        self.current_color = "#000000"

        # piesimo lapa darom
        self.cnv = Canvas(self.root, width=WIDTH-10, height=HEIGHT-10, bg="white")
        self.cnv.pack()
        self.cnv.bind("<B1-Motion>", self.paint) # darom, kad reaguotu i left click'a, kad piestu piestukas

        self.image = PIL.Image.new("RGB", (WIDTH, HEIGHT), WHITE)
        self.draw = ImageDraw.Draw(self.image)

        # randam frame mygtukams
        self.btn_frame = Frame(self.root)
        self.btn_frame.pack(fill=X) # pildome mygtukus per visa x asi

        # darom stulpelius mygtukams
        self.btn_frame.columnconfigure(0, weight=1)
        self.btn_frame.columnconfigure(1, weight=1)
        self.btn_frame.columnconfigure(2, weight=1)

        # darom visus mygtukus
        # "sticky = W+E" reiskia, kad mygtukas bus istemptas nuo west (kaires) iki east (desines), tai yra tkinter'io konstantos

        self.clear_btn = Button(self.btn_frame, text="Clear", command = self.clear)
        self.clear_btn.grid(row=1, column=0, sticky = W+E)

        self.erase_btn = Button(self.btn_frame, text="Erase", command=self.erase)
        self.erase_btn.grid(row=0, column=0, sticky=W + E)

        self.bplus_btn = Button(self.btn_frame, text="B+", command=self.brush_plus)
        self.bplus_btn.grid(row=0, column=2, sticky=W + E)

        self.bminus_btn = Button(self.btn_frame, text="B-", command=self.brush_minus)
        self.bminus_btn.grid(row=1, column=2, sticky=W + E)

        self.color_btn = Button(self.btn_frame, text="Change Color", command=self.change_color)
        self.color_btn.grid(row=1, column=1, sticky=W + E)

        self.brush_btn = Button(self.btn_frame, text="Brush", command=self.brush)
        self.brush_btn.grid(row=0, column=1, sticky=W + E)

        # uzdarome langa
        self.root.mainloop()

        # visos komandos, kurios bus naudojamos mygtukuose

    def paint(self, event): # event is the motion of the mouse
        # x ir y koordinates musu staciakampio
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.cnv.create_rectangle(x1, y1, x2, y2, outline=self.current_color, fill=self.current_color, width=self.brush_width)
        self.draw.rectangle([x1, y1, x2 + self.brush_width, y2 + self.brush_width], outline=self.current_color, fill=self.current_color, width=self.brush_width)

    def clear(self):
        self.cnv.delete("all")

    def brush_plus(self):
        self.brush_width += 1

    def brush_minus(self):
        if self.brush_width > 1:
            self.brush_width -= 1

    def change_color(self):
        _, self.current_color = colorchooser.askcolor(title ="Choose color")

    def erase(self):
        self.current_color = "#FFFFFF"

    def brush(self):
        self.current_color = "#000000"

PaintGUI()