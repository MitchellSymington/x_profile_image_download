# X (Twitter) Profile Image Downloader with GUI

This Python program downloads profile images from X (formerly Twitter) using the Unavatar.io service. The images are cropped into a circular shape and saved as transparent PNGs. A simple GUI (Graphical User Interface) makes it easy to use.

---

## ✅ Requirements

- Python 3.8+
- Install required packages with:

```
pip install requests pillow
```

---

## 🖱️ How to Use

1. Double-click the `.exe` file (if using the compiled version) or run the script:

```
python x_profile_image_gui.py
```

2. In the GUI:
   - Click "Start Download"
   - Select your `usernames.txt` file
   - Choose a folder to save the images

3. Wait until processing completes. Cropped PNG images and a `log.txt` file will be saved in the selected folder.

---

## 🧾 Input File Format

The `usernames.txt` file should contain one X username or profile URL per line:

```
@jack
elonmusk
https://x.com/BarackObama
```

---

## 🖼️ GUI Layout (Example)

```
+--------------------------------------------+
| X Profile Image Downloader                 |
|                                            |
| 1. Select a usernames.txt file             |
| 2. Choose a folder to save images          |
|                                            |
| [ Start Download ]                         |
|                                            |
| ✅ Done! Check the selected folder.        |
+--------------------------------------------+
```

---

## 🔗 Notes

- Uses: https://unavatar.io/x/{username}
- No login or API key required.
- Automatically handles image download and circular cropping with transparency.
