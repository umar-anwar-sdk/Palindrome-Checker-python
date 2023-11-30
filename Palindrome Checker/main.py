import tkinter as tk

def is_palindrome(input_str):
    clean_str = ''.join(input_str.split()).lower()
    return clean_str == clean_str[::-1]

def check_palindrome():
    user_input = entry.get()
    if is_palindrome(user_input):
        result_label.config(text="It's a palindrome!")
    else:
        result_label.config(text="It's not a palindrome.")

# Create the main window
window = tk.Tk()
window.title("Palindrome Checker")

# Create and place widgets
label = tk.Label(window, text="Enter a string:")
label.pack(pady=10)

entry = tk.Entry(window)
entry.pack(pady=10)

check_button = tk.Button(window, text="Check Palindrome", command=check_palindrome)
check_button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Start the GUI event loop
window.mainloop()

