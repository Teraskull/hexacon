from tkinter import Tk, ttk

window = Tk()
window.title("Hexacon")
window.resizable(False, False)


def center_window(w, h):
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws // 2) - (w // 2)
    y = (hs // 2) - (h // 2)
    window.geometry(f'{w}x{h}+{x}+{y}')


center_window(520, 120)

separator = '\\x'


def ascii_to_hex():
    text = input_ascii.get()
    if text:
        text_box.config(state='enabled')
        text_box.delete(0, 'end')
        text_box.insert(0, f"{separator}{separator.join(hex(ord(x))[2:] for x in text)}")
        text_box.config(state='readonly')


def hex_to_ascii():
    text = input_hex.get()
    if text:
        text_box.config(state='enabled')
        text_box.delete(0, 'end')
        try:
            text_box.insert(0, bytearray.fromhex(text.replace(separator, '')).decode())
        except ValueError as e:
            input_hex.delete(0, 'end')
        text_box.config(state='readonly')


def copy_result():
    text = text_box.get()
    window.clipboard_clear()
    window.clipboard_append(text)


label_hex = ttk.Label(window, text="To Ascii: ")
input_hex = ttk.Entry(window, width=60)
button_hex = ttk.Button(window, text="Convert", command=hex_to_ascii)

label_ascii = ttk.Label(window, text="To Hex: ")
input_ascii = ttk.Entry(window, width=60)
button_ascii = ttk.Button(window, text="Convert", command=ascii_to_hex)

label_output = ttk.Label(window, text="Output: ")
text_box = ttk.Entry(window, width=60)
button_copy = ttk.Button(window, text="Copy", command=copy_result)
text_box.config(state='readonly')

label_hex.grid(column=0, row=0, pady=(10, 10), sticky='E')
input_hex.grid(column=1, row=0, pady=(10, 10))
button_hex.grid(column=2, row=0, padx=(10, 0), pady=(10, 10))

label_ascii.grid(column=0, row=1, sticky='E')
input_ascii.grid(column=1, row=1)
button_ascii.grid(column=2, row=1, padx=(10, 0))

label_output.grid(column=0, row=2, padx=(10, 0), pady=(15, 0), sticky='E')
text_box.grid(column=1, row=2, pady=(15, 0))
button_copy.grid(column=2, row=2, padx=(10, 0), pady=(15, 0))


if __name__ == '__main__':
    window.mainloop()
