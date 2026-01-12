from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import threading
import app # This imports your app.py

class FlaskAndroidApp(App):
    def build(self):
        layout = BoxLayout()
        # Simple text to show app is running
        self.label = Label(text="Server starting on Port 5000...", font_size='20sp')
        layout.add_widget(self.label)
        
        # Run Flask in a background thread
        server_thread = threading.Thread(target=self.start_server)
        server_thread.daemon = True
        server_thread.start()
        return layout

    def start_server(self):
        # Host 0.0.0.0 is important for Android
        app.app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    FlaskAndroidApp().run()