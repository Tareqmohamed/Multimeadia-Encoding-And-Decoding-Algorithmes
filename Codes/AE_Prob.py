import tkinter as tk
from tkinter import messagebox
import math


def create_gui(msg):
    prob = {}
    global total
    total=0
    def validate_float(P):
        if P.strip() == "":
            return True
        try:
            float_value = float(P)
            return 0 <= float_value <= 1
        except ValueError:
            return False

    def update_sum():
        global total
        total = sum(float(entry.get()) if entry.get() else 0 for entry in entry_list)
        sum_label.config(text=f"Sum: {total:.2f}")

    def check_sum():
        global total
        total = sum(float(entry.get()) if entry.get() else 0 for entry in entry_list)
        # Use a small threshold for comparison due to floating-point precision
        threshold = 1e-10
        if math.isclose(total, 1, abs_tol=threshold):
            messagebox.showinfo("Success", "Sum is 1.",)
            update_sum()
            create_prob()
            root1.quit()
            # root1.withdraw()
        else:
            messagebox.showerror("Error", "Sum of values must be 1.")
            update_sum()

    def create_prob():
        for index, cahr in enumerate(msg):
            prob[cahr] = float(entry_list[index].get())

    # Create the main window
    root1 = tk.Tk()
    root1.title("Textbox and Label App")
    n = len(msg)  # Change this to the desired number of textboxes

    # Create and place labels and textboxes using a loop
    labels = []
    entry_list = []

    for i, char in enumerate(msg):
        label = tk.Label(root1, text=char)
        label.grid(row=i, column=0, padx=5, pady=5)
        labels.append(label)

        entry = tk.Entry(
            root1,
            width=10,
            validate="key",
            validatecommand=(root1.register(validate_float), "%P"),
        )
        entry.grid(row=i, column=1, padx=5, pady=5)
        entry_list.append(entry)

    # Create a button to check the sum
    check_button = tk.Button(root1, text="Check Sum", command=check_sum)
    check_button.grid(row=n, column=0, columnspan=2, pady=10)

    # Create a label to display the sum
    sum_label = tk.Label(root1, text="Sum: 0.00")
    sum_label.grid(row=n + 1, column=0, columnspan=2, pady=10)
    # Start the Tkinter event loop
    root1.mainloop()
    root1.destroy()
    return prob




# msg ="1332"
# x = set(msg)
# oredred_dic = {char: None for char in x}
# oredred = set(oredred_dic.keys())
# prob = create_gui(oredred)