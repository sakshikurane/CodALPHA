import os
import shutil
from tkinter import Tk, Label, Button, filedialog, messagebox

# Mapping of file extensions to folder names
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".txt", ".pdf", ".docx", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Others": []
}

# Function to organize files
def organize_files(source_dir, destination_dir):
    if not source_dir or not destination_dir:
        messagebox.showwarning("Missing Folders", "Please select both source and destination folders.")
        return

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        if os.path.isdir(file_path):
            continue

        file_extension = os.path.splitext(filename)[1].lower()

        folder_name = "Others"
        for category, extensions in file_types.items():
            if file_extension in extensions:
                folder_name = category
                break

        category_folder = os.path.join(destination_dir, folder_name)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

        shutil.move(file_path, os.path.join(category_folder, filename))

    messagebox.showinfo("Success", "Files have been organized successfully!")

# Function to browse folder
def browse_folder(label):
    folder_selected = filedialog.askdirectory()
    label.config(text=folder_selected)
    return folder_selected

# GUI setup
def main():
    root = Tk()
    root.title("SortEase")  # Set the application name to SortEase
    root.geometry("500x300")
    root.state("zoomed")  # Maximizes the window on startup
    root.resizable(True, True)

    # Center content
    for i in range(5):  # Add enough rows for spacing
        root.grid_rowconfigure(i, weight=1)
    for j in range(3):
        root.grid_columnconfigure(j, weight=1)

    # Font settings
    font_settings = ("Times New Roman", 16, "bold")

    # Labels and buttons for source and destination directories
    Label(root, text="Source Folder:", font=font_settings).grid(row=1, column=0, padx=10, pady=10, sticky="e")
    source_label = Label(root, text="Not selected", bg="white", width=30, font=font_settings)
    source_label.grid(row=1, column=1, padx=10, pady=10)
    Button(root, text="Browse", command=lambda: browse_folder(source_label), font=font_settings).grid(row=1, column=2, padx=10, pady=10)

    Label(root, text="Destination Folder:", font=font_settings).grid(row=2, column=0, padx=10, pady=10, sticky="e")
    dest_label = Label(root, text="Not selected", bg="white", width=30, font=font_settings)
    dest_label.grid(row=2, column=1, padx=10, pady=10)
    Button(root, text="Browse", command=lambda: browse_folder(dest_label), font=font_settings).grid(row=2, column=2, padx=10, pady=10)

    Button(
        root, text="Organize Files",
        command=lambda: organize_files(source_label.cget("text"), dest_label.cget("text")),
        font=font_settings, bg="#4CAF50", fg="white"
    ).grid(row=3, column=1, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
