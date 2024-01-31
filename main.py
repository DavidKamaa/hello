from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class HelloWorldApp(App):
    def build(self):
        # Create a BoxLayout as the root widget
        layout = BoxLayout(orientation='vertical', padding=10)

        # Create a button with the text "Hello World"
        btn_hello = Button(text='Hello World', size_hint=(None, None), size=(200, 100))

        # Bind the button press event to a function
        btn_hello.bind(on_press=self.on_button_press)

        # Add the button to the layout
        layout.add_widget(btn_hello)

        return layout

    def on_button_press(self, instance):
        # Event handler for button press
        print("Hello World Button Pressed!")

if __name__ == '__main__':
    HelloWorldApp().run()
