from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import threading
import time
import app # This must match your app.py filename

class AndroidFlask(App):
    def build(self):
        # Start Flask in the background so it doesn't freeze the App
        webapp_thread = threading.Thread(target=self.start_flask)
        webapp_thread.daemon = True
        webapp_thread.start()

        layout = BoxLayout()
        # This shows while the server is starting
        self.lbl = Label(text="Starting Local Server...\nOpen localhost:5000 in your browser if screen is blank", halign="center")
        layout.add_widget(self.lbl)
        return layout

    def start_flask(self):
        # Android requires 0.0.0.0 to allow internal connections
        app.app.run(host='0.0.0.0', port=5000, debug=False)

if __name__ == '__main__':
    AndroidFlask().run()