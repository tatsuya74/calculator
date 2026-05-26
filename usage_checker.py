import tkinter as tk
import webbrowser


def open_usage():
    webbrowser.open("https://claude.ai/settings/usage")


root = tk.Tk()
root.title("Claude 使用量確認")
root.resizable(False, False)
root.attributes("-topmost", True)

tk.Label(root, text="Claude Code", font=("Arial", 13, "bold"), pady=8).pack()
tk.Label(root, text="使用量はブラウザで確認できます", font=("Arial", 10), fg="#555").pack()

btn = tk.Button(
    root,
    text="使用量を確認する",
    font=("Arial", 12, "bold"),
    bg="#D97706",
    fg="white",
    activebackground="#B45309",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=10,
    cursor="hand2",
    command=open_usage,
)
btn.pack(pady=15, padx=20)

root.mainloop()
