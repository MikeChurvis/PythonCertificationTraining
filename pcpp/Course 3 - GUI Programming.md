# Module 1 - TkInter Essentials

TkInter has been in development since 1991.

`window = Tk()` represents the main app window instance.

`window.mainloop()` is a blocking call that runs the window's event loop.

Elements are placed in a window via one of three geometry managers:
- `.place(x, y, width, height)` puts an element at an exact pixel coordinate location.
- `.grid(r, c, rowspan, colspan)` puts an element in a given row and column of an automatically-sized grid.
- `.pack(fill)` puts an element in the app in the next space it will fit, flowing left-to-right, top-to-bottom. One could say it's vaguely flexbox-esque, but much more limited.

Each geometry manager is designed to be used to the exclusion of any of the others; mixing geometry managers within the same app causes undefined behavior.

`Label` is a static element that contains text.

`Frame` is used to group widgets.

`IntVar` is used to hold an integer value. This value can be consumed by UI elements to enable 2-way reactivity.

Register listener: `var.trace(Literal['r','w','u'], callback_fn)`

`Checkbutton(window, text, variable)`

`widget(command=fn)` takes a parameterless callback. `.bind(fn)` takes a one-parameter event handler.

Notable `Event` properties:
- `widget`: reference to the object that triggered the event.
- `x, y`: mouse coords relative to target widget.
- `x_root, y_root`: mouse coords relative to screen.
- `char`: Unicode character code of the keypress (keyboard events only)
- `keysym`: key symbol of the keypress
- `keycode`: numerical code of the pressed key 
- `num`: the number identifier of the clicked mouse button
- `type` the event's type

Get config:
- `widget["prop"]`
- `widget.cget("prop")`

Set config
- `widget["prop"] = new_value`
- `widget.config(prop=new_value)`

`Label(app, text, font=("font_family_name", "font_size"[, "font_style"])`

`widget.after(ms, callback_fn) -> int`: executes a callback after a given delay. Returns the ID of the callback's schedule entry.

`widget.after_cancel(id)`: cancels the schedule entry with the given ID.

# Module 2 - Widgets

`Frame` is a widget holder. It can hold anything, even other Frames. A Frame can utilize its own geometry manager independently of those of its parents or children.

`LabelFrame` is a frame with a label.

`Entry` is a text field.

Git rid of the 'tearoff' separator in menus with the `tearoff=0` argument.

Keyboard accesibility with menus: use the `menu.add_command(label=..., underline=...)`

`menu.add_command`
- `accelerator` is just a label for the hotkey; the actual hotkey binding must be done separately (i.e. `window.bind_all('<Control-q>', evt_handler)`).

Menu items are configured with `menu.entryconfigure(index, prop=val)`

Changing the window icon requires a low-level call:
- `window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file='logo.png'))`

Programmatically changing the window size is done through `window.geometry(f"{w}x{h}")`

Set window resizing bounds:
- `window.minsize(width, height)`
- `window.maxsize(width, height)`

Set window resizability:
- `window.resizable(width=False, height=False)`

Main window's close operation doesn't raise a `<Delete>` event. Instead, bind callback to `window.protocol('WM_DELETE_WINDOW', callback_fn)`.

`messagebox.askyesno` returns boolean. `messagebox.askquestion` returns `"Yes"` or `"No"`.

`Canvas(window, width, height, bg)`
- `.create_line(x0, y0, x1, y1, *xn_yn, arrow: Optional[Literal[tk.FIRST,tk.LAST,tk.BOTH]] = None, fill='black', smooth=False, width=1)`
- `.create_rectangle`
- `.create_polygon`
- `.create_arc`
	- `style` in `PIESLICE, CHORD, ARC`
	- `start, extent`: counter-clockwise where 0 is right and 90 is up.
- `.create_text(x, y, text, font, justify, fill)`
- `create_image(x, y, image: tk.PhotoImage)`

Only GIF and PNG work with Tk out of the box. For other types, use the PIL:
```python
image = PIL.ImageTk.PhotoImage(PIL.Image.open("filepath"))
```

# Module 3 - Projects

## Tic Tac Toe

TicTacToeButton(tk.Button)
- self.row
- self.column
- self.mark_with_x()
- self.mark_with_o()

## Pocket Calculator

### Specs

Has 3 modes:
- Left operand mode (LOP)
- Right operand mode (ROP)
- Result mode (RES)

Default is LOP mode.

At all times:
- Pressing the clear button resets the calculator state, thus entering LOP mode.

While in LOP:
- Pressing a numpad button appends a digit to the left operand. 
- Pressing the negator button inverts the sign of the left operand.
- Pressing the equal button causes the operator buttons to pulse.
- Pressing an operator button selects that operator and switches to ROP mode.

While in ROP:
- Pressing a numpad button appends a digit to the right operand.
- Pressing the negator button inverts the sign of the right operand.
- Pressing 

# End-of-Course Test

Grade: 79%

Takeaways:
- An event that binds to the Q key is just `'q'`, not `'<Q>'`or `'<Key-Q>'`.
- Changing a button's status is done with `.config(state=)`, not `status=`.
- Give focus to a widget with `.focus_set()`, not `.give_focus()`.