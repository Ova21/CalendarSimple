import os
import customtkinter as ctk

def test_font():
    # FIXED PATH: Start looking directly from the "assets" folder!
    font_path = os.path.abspath(os.path.join("assets", "pixel_3", "pixelfont.ttf"))

    # Let's verify if the path issue is solved
    if not os.path.exists(font_path):
        print(f"❌ ERROR: File still not found at:\n{font_path}")
        print("Double check if 'assets' is spelled exactly right!")
        return
    else:
        print(f"✅ SUCCESS: Found font file at:\n{font_path}")

    root = ctk.CTk()
    root.geometry("300x300")

    # Load it into CustomTkinter
    ctk.FontManager.load_font(font_path)

    # (Remember to check the True Font Name if it falls back to Arial!)
    retro_small = ctk.CTkFont(family="Minecraft", size=16)
    retro_large = ctk.CTkFont(family="Minecraft", size=90)

    text_small = ctk.CTkLabel(root, text="SMALL TEXT", font=retro_small)
    text_small.pack(pady=20)

    text_large = ctk.CTkLabel(root, text="12", font=retro_large)
    text_large.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    test_font()