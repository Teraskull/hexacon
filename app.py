from tkinter import Tk, ttk
import binascii

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


def utf_to_hex() -> None:
    """
    Converts utf-8 to hexadecimal string and inserts in 'text_box' entry.
    """
    text = binascii.hexlify(input_utf.get().encode('utf-8')).decode('utf-8')
    text_box.config(state='enabled')
    text_box.delete(0, 'end')
    if text:
        text_box.insert(0, f"{separator}{separator.join(text[i:i + 2] for i in range(0, len(text), 2))}")
        button_copy.config(text='Copy')
    else:
        text_box.delete(0, 'end')
    text_box.config(state='readonly')


def hex_to_utf() -> None:
    """
    Converts hexadecimal string to utf-8 and inserts in 'text_box' entry.

    Raises:
        ValueError: If passed HEX string is not valid, erase entry.
    """
    text = input_hex.get()
    text_box.config(state='enabled')
    text_box.delete(0, 'end')
    if text:
        try:
            text_box.insert(0, bytearray.fromhex(text.replace(separator, '')).decode('utf-8'))
            button_copy.config(text='Copy')
        except ValueError as e:
            input_hex.delete(0, 'end')
    text_box.config(state='readonly')


def copy_result() -> None:
    text = text_box.get()
    if text:
        window.clipboard_clear()
        window.clipboard_append(text)
        button_copy.config(text='Copied')


label_hex = ttk.Label(window, text="To utf: ")
input_hex = ttk.Entry(window, width=60)
button_hex = ttk.Button(window, text="Convert", command=hex_to_utf)

label_utf = ttk.Label(window, text="To hex: ")
input_utf = ttk.Entry(window, width=60)
button_utf = ttk.Button(window, text="Convert", command=utf_to_hex)

label_output = ttk.Label(window, text="Output: ")
text_box = ttk.Entry(window, width=60)
button_copy = ttk.Button(window, text="Copy", command=copy_result)
text_box.config(state='readonly')

label_hex.grid(column=0, row=0, pady=(10, 10), sticky='E')
input_hex.grid(column=1, row=0, pady=(10, 10))
button_hex.grid(column=2, row=0, padx=(10, 0), pady=(10, 10))

label_utf.grid(column=0, row=1, sticky='E')
input_utf.grid(column=1, row=1)
button_utf.grid(column=2, row=1, padx=(10, 0))

label_output.grid(column=0, row=2, padx=(10, 0), pady=(15, 0), sticky='E')
text_box.grid(column=1, row=2, pady=(15, 0))
button_copy.grid(column=2, row=2, padx=(10, 0), pady=(15, 0))


if __name__ == '__main__':
    window.mainloop()
