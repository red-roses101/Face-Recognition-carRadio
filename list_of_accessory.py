import tkinter as tk
from time import strftime, localtime
import  cv2
import requests
import json
import tkinter as tk

class Listofaccessory(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.create_widgets()

    def create_widgets(self):
        # create three buttons
        button1 = tk.Button(self, text="Radio activate", fg="darkblue", bg="green", font=("Arial", 12), height=2, width=16, command=self.radio_activate)
        button2 = tk.Button(self, text="Windows activate", bg="green", fg="darkblue", font=("Arial", 12), height=2, width=20, command=self.windows_activate)
        button3 = tk.Button(self, text="gps traker" ,bg="green", fg="darkblue", font=("Aeial",12), height=2, width=20, command=self.gps_activate)
        button4 = tk.Button(self, text="calls", bg="green", fg="red", font=("Arial",12), height=2, width=16)

        # create a quit button
        quit_button = tk.Button(self, text="Quit", height=1, width=8, command=self.quit)

        # place the widgets in the grid
        button1.grid(row=1, column=1, padx=3, pady=7)
        button2.grid(row=2, column=1, padx=3, pady=7)
        button3.grid(row=3, column=1, padx=3, pady=7)
        button4.grid(row=4, column=1, padx=3, pady=7)

        quit_button.grid(row=7, column=1, padx=5, pady=32)
        # create a frame for the canvas
        canvas_frame = tk.Frame(self)
        canvas_frame.grid(row=0, column=0, sticky="nsew")



        # create a label for displaying the time
        time_label = tk.Label(self, text="", font=("Arial", 14))
        time_label.grid(row=8, column=1, pady=10)

        # periodically update the time display
        def update_time():
            time_str = strftime("%H:%M:%S", localtime())
            time_label.config(text=time_str)
            time_label.after(1000, update_time)

        # call update_time() to start the periodic update
        update_time()

    def radio_activate(self):
        # create a new window for displaying the image
        image_window = tk.Toplevel(self.parent)
        image_window.title("Image")

        # load and dispaly the image
        Image3 = cv2.imread("Marquardt.png")
        cv2.imshow("Activation", Image3)
        cv2.waitKey(5000)
        cv2.destroyAllWindows()

    def windows_activate(self):
        # create a new window for the car window adjustment buttons
        window_window = tk.Toplevel(self.parent)
        window_window.title("Car Window Adjustment")

        # create four buttons for adjusting the car windows
        button1 = tk.Button(window_window, text="Front Left", fg="darkblue", bg="green", font=("Arial", 12), height=2, width=18)
        button2 = tk.Button(window_window, text="Front Right", bg="green", fg="darkblue", font=("Arial", 12), height=2, width=20)
        button3 = tk.Button(window_window, text="Rear Left", bg="green", fg="darkblue", font=("Arial", 12), height=2, width=18)
        button4 = tk.Button(window_window, text="Rear Right", bg="green", fg="darkblue", font=("Arial", 12), height=2, width=20)
        ok_button = tk.Button(window_window, text="OK", font=("Arial", 14), bg="gray", fg="white",height=1, width=10, command=window_window.destroy)


        # place the buttons in the window
        button1.grid(row=1, column=1, padx=3, pady=7)
        button2.grid(row=1, column=2, padx=3, pady=7)
        button3.grid(row=2, column=1, padx=3, pady=7)
        button4.grid(row=2, column=2, padx=3, pady=7)
                     # center the ok button in the window
        ok_button.grid(row=3, column=1, columnspan=2, padx=5, pady=32)


    def gps_activate(self):

        window = tk.Tk()
        # Set the window title
        window.title("IP Geolocation")

        # Set the window size
        window.geometry("600x250")

        # Send a request to ipinfo.io to get the location information
        response = requests.get('https://ipinfo.io/json')
        data = json.loads(response.text)

        # Create a label widget to display the location information
        location_label = tk.Label(window,
                                  text="Your approximate location is: " + data["city"] + ", " + data["region"] + ", " +
                                       data["country"], font=("Arial", 14), fg="blue")
        location_label.pack(pady=20)

        # Create a label widget to display the latitude and longitude coordinates
        coordinates_label = tk.Label(window, text="Your latitude and longitude are: " + data["loc"], font=("Arial", 14),
                                     fg="blue")
        coordinates_label.pack(pady=20)

        # Create an "OK" button to close the window
        ok_button = tk.Button(window, text="OK", font=("Arial", 14), bg="gray", fg="white", command=window.destroy)
        ok_button.pack(pady=20)

        # Run the Tkinter event loop
        window.mainloop()
if __name__ == "__main__":
    root = tk.Tk()
    app = Listofaccessory(root)
    root.geometry("400x400")
    root.configure(bg="blue")# set the background color of the window to bule
    app.pack()
    root.mainloop()












