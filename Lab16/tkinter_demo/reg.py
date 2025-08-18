import tkinter as tk
from db import DB


class RegistrationApp:
    """Represents the main Tkinter application for user registration."""

    def __init__(self, master, db):
        self.master = master
        self.db = db
        self.master.title("User Registration")
        self.master.geometry("400x400")
        self.master.resizable(False, False)
        self.master.config(bg="#f0f0f0")

        self._create_widgets()

    def _create_widgets(self):
        """Creates and places all GUI elements."""
        font_style = ("Arial", 12)
        label_font_style = ("Arial", 12, "bold")
        button_font_style = ("Arial", 12, "bold")

        # Create main app Frame
        form_frame = tk.Frame(
            self.master, padx=20, pady=20, bg="#ffffff", bd=2, relief="groove"
        )
        form_frame.pack(pady=30, padx=20, fill="both", expand=True)

        # Username Label and Entry
        username_label = tk.Label(
            form_frame, text="Username:", font=label_font_style, bg="#ffffff"
        )
        username_label.grid(row=0, column=0, pady=5, sticky="w")
        self.username_entry = tk.Entry(
            form_frame, font=font_style, width=30, bd=2, relief="solid"
        )
        self.username_entry.grid(row=0, column=1, pady=5, padx=10, sticky="ew")

        # Password Label and Entry
        password_label = tk.Label(
            form_frame, text="Password:", font=label_font_style, bg="#ffffff"
        )
        password_label.grid(row=1, column=0, pady=5, sticky="w")
        self.password_entry = tk.Entry(
            form_frame, font=font_style, show="*", width=30, bd=2, relief="solid"
        )
        self.password_entry.grid(row=1, column=1, pady=5, padx=10, sticky="ew")

        # Email Label and Entry
        email_label = tk.Label(
            form_frame, text="Email:", font=label_font_style, bg="#ffffff"
        )
        email_label.grid(row=2, column=0, pady=5, sticky="w")
        self.email_entry = tk.Entry(
            form_frame, font=font_style, width=30, bd=2, relief="solid"
        )
        self.email_entry.grid(row=2, column=1, pady=5, padx=10, sticky="ew")

        # Register Button
        register_button = tk.Button(
            form_frame,
            text="Register",
            command=self._submit_registration,
            font=button_font_style,
            bg="#4CAF50",
            fg="white",
            activebackground="#45a049",
            activeforeground="white",
            relief="raised",
            bd=3,
            padx=10,
            pady=5,
        )
        register_button.grid(row=3, column=0, columnspan=2, pady=20)

        # Message Label (for feedback)
        self.message_label = tk.Label(
            form_frame, text="", font=("Arial", 10), bg="#ffffff"
        )
        self.message_label.grid(row=4, column=0, columnspan=2, pady=5)

        # Configure column weights so the entry fields expand
        form_frame.grid_columnconfigure(1, weight=1)
        # Configure the row containing the message label to expand
        form_frame.grid_rowconfigure(4, weight=1)

    def _submit_registration(self):
        """Handles the registration button click event."""
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()

        # Basic input validation
        if not username or not password or not email:
            self.message_label.config(text="All fields are required!", fg="red")
            return

        # Attempt to register user using the DB
        if self.db.register_user(username, password, email):
            self.message_label.config(text="Registration successful!", fg="green")
            # Clear the input fields after successful registration
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
        else:
            self.message_label.config(
                text="Registration failed. Username or email might already exist.",
                fg="red",
            )


# --- Main execution ---
if __name__ == "__main__":
    db = DB()  # Initialize database manager

    root = tk.Tk()
    app = RegistrationApp(root, db)  # Initialize the GUI app
    root.mainloop()  # Start the Tkinter event loop
