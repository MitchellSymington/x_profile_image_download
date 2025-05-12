import os
import requests
from PIL import Image, ImageDraw
from io import BytesIO
import tkinter as tk
from tkinter import filedialog, messagebox
import logging

# Function to process usernames using unavatar.io and save circular images
def process_usernames(file_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    log_file = os.path.join(output_dir, "log.txt")
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")

    # Read usernames from text file
    with open(file_path) as f:
        usernames = [line.strip().replace("@", "").split("/")[-1] for line in f if line.strip()]

    for username in usernames:
        try:
            # Update GUI status
            status_label.config(text=f"Processing {username}...")
            root.update_idletasks()

            # Use Unavatar.io to fetch the profile image from X (formerly Twitter)
            url = f"https://unavatar.io/x/{username}"
            response = requests.get(url, timeout=10)

            if response.status_code == 200:
                img = Image.open(BytesIO(response.content)).convert("RGBA")
                size = img.size

                # Create circular mask
                mask = Image.new('L', size, 0)
                draw = ImageDraw.Draw(mask)
                draw.ellipse((0, 0) + size, fill=255)

                # Apply mask to image
                output = Image.new('RGBA', size)
                output.paste(img, (0, 0), mask)

                output_path = os.path.join(output_dir, f"{username}.png")
                output.save(output_path)
                logging.info(f"Downloaded and saved: {output_path}")
            else:
                logging.warning(f"Failed to download image for {username}")
        except Exception as e:
            logging.error(f"Error with {username}: {str(e)}")

    status_label.config(text="✅ Done! Check the selected folder.")

# GUI start function
def start_process():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not file_path:
        return
    output_dir = filedialog.askdirectory()
    if not output_dir:
        return
    process_usernames(file_path, output_dir)

# GUI setup
root = tk.Tk()
root.title("X (Twitter) Profile Image Downloader")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

title_label = tk.Label(frame, text="Download X Profile Images", font=("Helvetica", 14, "bold"))
title_label.pack(pady=10)

instruction_label = tk.Label(frame, text="1. Select a usernames.txt file\n2. Choose a folder to save images")
instruction_label.pack(pady=5)

select_button = tk.Button(frame, text="Start Download", command=start_process, width=30)
select_button.pack(pady=5)

status_label = tk.Label(frame, text="", fg="green")
status_label.pack(pady=10)

root.mainloop()
