import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("電卓")
        self.root.resizable(False, False)

        self.expression = ""
        self.display_var = tk.StringVar(value="0")

        self._build_ui()

    def _build_ui(self):
        display = tk.Entry(
            self.root,
            textvariable=self.display_var,
            font=("Arial", 24),
            justify="right",
            state="readonly",
            readonlybackground="white",
            bd=10,
        )
        display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

        buttons = [
            ("C",  1, 0), ("±", 1, 1), ("%",  1, 2), ("÷", 1, 3),
            ("7",  2, 0), ("8", 2, 1), ("9",  2, 2), ("×", 2, 3),
            ("4",  3, 0), ("5", 3, 1), ("6",  3, 2), ("−", 3, 3),
            ("1",  4, 0), ("2", 4, 1), ("3",  4, 2), ("+", 4, 3),
            ("0",  5, 0), (".", 5, 2), ("=",  5, 3),
        ]

        for text, row, col in buttons:
            is_zero = text == "0"
            colspan = 2 if is_zero else 1

            if text in ("÷", "×", "−", "+", "="):
                bg, fg = "#FF9500", "white"
            elif text in ("C", "±", "%"):
                bg, fg = "#A5A5A5", "black"
            else:
                bg, fg = "#333333", "white"

            btn = tk.Button(
                self.root,
                text=text,
                font=("Arial", 18, "bold"),
                bg=bg,
                fg=fg,
                activebackground=bg,
                activeforeground=fg,
                bd=0,
                relief="flat",
                command=lambda t=text: self._on_click(t),
            )
            btn.grid(
                row=row, column=col,
                columnspan=colspan,
                sticky="nsew",
                padx=2, pady=2,
                ipady=15,
            )

        for i in range(6):
            self.root.rowconfigure(i, weight=1)
        for i in range(4):
            self.root.columnconfigure(i, weight=1)

    def _on_click(self, text):
        if text == "C":
            self.expression = ""
            self.display_var.set("0")

        elif text == "=":
            try:
                expr = (
                    self.expression
                    .replace("÷", "/")
                    .replace("×", "*")
                    .replace("−", "-")
                )
                result = eval(expr)
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                self.expression = str(result)
                self.display_var.set(self.expression)
            except ZeroDivisionError:
                self.display_var.set("ゼロ除算エラー")
                self.expression = ""
            except Exception:
                self.display_var.set("エラー")
                self.expression = ""

        elif text == "±":
            try:
                val = float(self.expression) * -1
                if val == int(val):
                    val = int(val)
                self.expression = str(val)
                self.display_var.set(self.expression)
            except Exception:
                pass

        elif text == "%":
            try:
                val = float(self.expression) / 100
                if val == int(val):
                    val = int(val)
                self.expression = str(val)
                self.display_var.set(self.expression)
            except Exception:
                pass

        else:
            if self.display_var.get() in ("エラー", "ゼロ除算エラー"):
                self.expression = ""
            if self.expression == "0" and text.isdigit():
                self.expression = text
            else:
                self.expression += text
            self.display_var.set(self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
