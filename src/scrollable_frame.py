from tkinter import *
from tkinter import ttk


class ScrollableFrame:

    root = Tk()
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)
    # Create A Canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=TOP, fill=BOTH, expand=1)
    # Add A Scrollbar To the Canvas
    my_scrollbar = ttk.Scrollbar(main_frame, orient=HORIZONTAL,command=my_canvas.xview)
    my_scrollbar.pack(side=BOTTOM, fill=X)
    # Configure The Canvas
    my_canvas.configure(xscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: ScrollableFrame.my_canvas.configure(scrollregion = ScrollableFrame.my_canvas.bbox("all")))
    # Create Another Frame Inside the Canvas
    second_frame = Frame(my_canvas)

    def get_second_frame(self):
        return self.second_frame

    # Add that New Frame To A Window In The Canvas
    my_canvas.create_window((0,0), window=second_frame, anchor="nw")