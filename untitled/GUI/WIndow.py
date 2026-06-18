import customtkinter as ctk
import os
from untitled.Data import Date_Time
import pywinstyles # Run: pip install pywinstyles

def run_win():

    date = Date_Time.date()

    root = ctk.CTk()
    root.title("") # Strips text
    root.geometry("260x315")
    root.configure(fg_color="#c0b89b")

    #What file am i in again??? (without this main file wont structure whole way into assets and wont find the fontú
    current_dir = os.path.dirname(os.path.abspath(__file__))
    font_path = os.path.join(current_dir, "assets", "pixel_3", "pixelfont.ttf")
    ctk.FontManager.load_font(font_path)

    font_month = ctk.CTkFont(family="Minecraft", size=36)
    font_day = ctk.CTkFont(family="Minecraft", size=160)

    month_box = ctk.CTkFrame(
        master=root,
        width=220,
        height=60,
        corner_radius=15,
        fg_color="#31353f"
    )
    month_box.pack_propagate(False)
    month_box.pack(pady=10)

    # Text for the month box
    month_text = ctk.CTkLabel(master=month_box, text=f"{date[0]}", font=font_month, text_color="white")
    month_text.pack(expand=True)

    day_box = ctk.CTkFrame(
        master=root,
        width=220,
        height=215,
        corner_radius=15,
        fg_color="#7c7f82"
    )

    day_box.pack_propagate(False)
    day_box.pack(pady=5)

    box_text = ctk.CTkLabel(master=day_box, text=f"{date[1]}", font=font_day, text_color="white")
    box_text.place(relx=0.525, rely=0.60, anchor="center") #Tbh i have no idea why just anchor center didnt worked so i finely tuned it to place it into perfect spot

    root.mainloop()

#if __name__ == "__main__":
#    run_win()