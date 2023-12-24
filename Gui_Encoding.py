import tkinter as tk
import Codes.RLC as RLC
import Codes.VLC as VLC
import Codes.huff as hfm
import Codes.LZW as LZW
import Codes.LZ77 as LZ77
import Codes.AE_encode as AE
import Codes.AE_Prob as AE_Prob
import Codes.BWT as bwt


def create_gui1():
    def button_click(button_text):
        new_text = " "
        if button_text == "RLC":
            new_text = RLC.run_length_encoding(input_box.get())
        elif button_text == "VLC":
            new_text = VLC.VLC_encode(input_box.get())[0]

        elif button_text == "Huffman":
            new_text = hfm.HuffmanEncoding(input_box.get())[0]

        elif button_text == "LZW":
            new_text = LZW.code_lzw(input_box.get())
        elif button_text == "LZ77":
            new_text = str(LZ77.code_LZ77(input_box.get()))
        elif button_text == "AE":
            msg = input_box.get()
            x = set(msg)
            oredred_dic = {char: None for char in x}
            oredred = set(oredred_dic.keys())
            prob = AE_Prob.create_gui(oredred)
            new_text = AE.AE(input_box.get(), prob)
        elif button_text == "JPEG":
            from Codes.jpeg25 import JPEGApp

            jpeg = tk.Tk()
            app = JPEGApp(jpeg)
            jpeg.mainloop()
        elif button_text == "BWT":
            new_text = bwt.encode(input_box.get())

        elif button_text == "DECODING":
            import Gui_Decoding as decode

            decode.create_gui2()
        try:
            output_box.configure(state=tk.NORMAL)
            output_box.delete("1.0", tk.END)
            output_box.insert(tk.END, new_text)
            output_box.configure(state=tk.DISABLED)
        except:
            return False
    def copy_text():
        content = output_box.get(
            "1.0", tk.END
        ).strip()  # Get all content from the Text widget
        root.clipboard_clear()  # Clear the clipboard
        root.clipboard_append(content)
        # Append the content to the clipboard
        root.update()  # Update the clipboard

    # Create the main window
    root = tk.Tk()
    root.title("Button App")

    # Create a textbox
    inp_label = tk.Label(root, text="INPUT:")
    inp_label.grid(row=0, column=0, columnspan=1, padx=0, pady=0)
    input_box = tk.Entry(root, width=27)
    input_box.grid(row=0, column=1, columnspan=3, padx=0, pady=10)
    output_label = tk.Label(root, text="OUTPUT:")
    output_label.grid(row=1, column=0, columnspan=1, padx=0, pady=0)
    output_box = tk.Text(root, width=20, height=10, state=tk.DISABLED)
    output_box.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

    # Create buttons
    button_texts = [
        "RLC",
        "VLC",
        "Huffman",
        "LZW",
        "LZ77",
        "AE",
        "BWT",
        "JPEG",
        "DECODING",
    ]
    copy_button = tk.Button(root, text="Copy Output", command=copy_text)
    copy_button.grid(row=2, column=2, padx=5, pady=5)

    row_val = 3
    col_val = 0
    for text in button_texts:
        if text == "DECODING":
            button = tk.Button(
                root,
                text=text,
                padx=20,
                pady=20,
                bg="RED",
                command=lambda t=text: button_click(t),
            )
        else:
            button = tk.Button(
                root,
                text=text,
                padx=20,
                pady=20,
                command=lambda t=text: button_click(t),
            )
        button.grid(row=row_val, column=col_val, padx=5, pady=5)
        col_val += 1
        if col_val > 2:
            col_val = 0
            row_val += 1

    # Start the Tkinter event loop
    root.mainloop()


create_gui1()
