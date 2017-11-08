from main_back import Database
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.widget import Widget

database = Database("data.json")

class MainScreen(Screen):
    pass

class CheckoutScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("main_style.kv")

class MainApp (App):
    def build(self):
        return presentation

    def command_inserir_ponto(self, status):
        database.inserir_ponto(status)

if __name__ == "__main__":
    MainApp().run()
