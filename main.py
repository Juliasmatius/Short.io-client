


# The domain you have in short.io
domain_shortio = "example.command"

# Shortio auth token DO NOT SHARE
auth_token = "lorem ipsum"

# Check readme.md for more info




# Import all the stuff
import tkinter as tk
from tkinter import Label, Entry, Button, PhotoImage
import pyperclip3

import requests
import json


def make_url(originurl):
  url = "https://api.short.io/links"
  payload = {
    "domain": domain_shortio,
    "allowDuplicates": False,
    "originalURL": originurl
  }
  headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": auth_token
  }

  response = requests.post(url, json=payload, headers=headers)

  create_response_json = json.loads(response.text)
  print(create_response_json)
  return create_response_json

def get_qr(create_response_json):
  url = "https://api.short.io/links/qr/"+create_response_json["idString"]

  payload = { "type": "png" }
  headers = {
    "accept": "image/png",
    "content-type": "application/json",
    "Authorization": auth_token
  }

  response = requests.post(url, json=payload, headers=headers)

  file =open("qr.png","wb")
  file.write(response.content)
  file.close()
  return "qr.png"







def ui():
# Create the main application window
  app = tk.Tk()
  app.title("URL shortener")
  app.geometry("350x500")

# Function to handle button clicks
  def handle_exit():
    app.destroy()
    exit()
  def copy_url():
    global shortened_json
    pyperclip3.copy(shortened_json["shortURL"])
  def button_click():
    global shortened_json
    text_label.pack_forget()
    entry1.pack_forget()
    url_label.pack_forget()
    image_label.pack_forget()
    image_widget.pack_forget()
    button2.pack_forget()
    button1.pack_forget()
    button3.pack_forget() 
    # Retrieve text from the text entry fields
    text1 = entry1.get()
    shortened_json =  make_url(text1)
    get_qr(shortened_json)
    image_widget.destroy()
    new_image = PhotoImage(file="qr.png")
        # Update the image displayed in the label
    image_label.configure(image=new_image)
    image_label.image = new_image
    if shortened_json["archived"]:
      is_archived = "WARNING! This URL has been *Archived*"
    else:
      is_archived =""
    url_label.configure(text=f"""
Original url : 
{shortened_json["originalURL"]}

Shortened url : 
{shortened_json["shortURL"]}
{is_archived}""")
    text_label.pack()
    entry1.pack()
    url_label.pack()
    image_label.pack()
    button3.pack()
    button2.pack()
    button1.pack()

    image_widget.pack()

# Create buttons

# Create text entry fields
  entry1 = Entry(app, width=30)

# Create a label for the image
  image_label = tk.Label(app)

# Load an image (replace 'your_image.png' with your image file)
  image = PhotoImage(file='qr.png')

# Create an image widget
  image_widget = tk.Label(app, image=image)
  image_widget.image = image
  button1 = Button(app, text="Exit", command=handle_exit)
  button2 = Button(app, text="Shorten", command=button_click)
  
  button3 = Button(app, text="Copy URL", command=copy_url)

  text_label = Label(app, text="Type or paste your long url below")
  text_label.pack()

  url_label = Label(app, text="Your url will be here")



# Pack the widgets
  entry1.pack()
  url_label.pack()
  image_label.pack()
  image_widget.pack()
  button2.pack()
  button1.pack()

# Start the Tkinter main loop
  app.mainloop()
ui()