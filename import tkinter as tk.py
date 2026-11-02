import tkinter as tk
from tkinter import messagebox
import subprocess
import sys


def install_package():
    package = package_entry.get().strip()

    if not package:
        messagebox.showerror("Error", "Please enter a package name.")
        return

    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", package],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            messagebox.showinfo(
                "Success",
                f"Successfully installed {package}."
            )
        else:
            messagebox.showerror(
                "Installation Failed",
                result.stderr
            )

    except Exception as e:
        messagebox.showerror("Error", str(e))


def show_installed_packages():
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "list"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            # Clear the text box
            package_list.delete("1.0", tk.END)

            # Display installed packages
            package_list.insert(tk.END, result.stdout)
        else:
            messagebox.showerror(
                "Error",
                result.stderr
            )

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Create the main window
window = tk.Tk()
window.title("Python Package Manager")
window.geometry("600x500")


# Package installation section
tk.Label(
    window,
    text="Enter the name of a Python package:"
).pack(pady=10)

package_entry = tk.Entry(window, width=50)
package_entry.pack()

tk.Button(
    window,
    text="Install Package",
    command=install_package
).pack(pady=10)


# Installed packages button
tk.Button(
    window,
    text="Show Installed Packages",
    command=show_installed_packages
).pack(pady=5)


# Text box for displaying packages
package_list = tk.Text(
    window,
    width=70,
    height=20
)
package_list.pack(pady=10)


# Start the GUI
window.mainloop()