from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

Window.size = (400, 600)
Window.resizable = False
Window.left = 500

class IMCCalculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        # CAMPO DE ENTRADA DO PESO
        self.add_widget(Label(text="Peso (kg):"))
        self.weight_input = TextInput(hint_text="Digite seu peso", multiline=False, input_filter="float")
        self.add_widget(self.weight_input)

        # CAMPO DE ENTRADA DA ALTURA 
        self.add_widget(Label(text="Altura (m):"))
        self.height_input = TextInput(hint_text="Digite sua altura", multiline=False, input_filter="float")
        self.add_widget(self.height_input)

        # BOTAO QUE VAI FAZER O CALCULO 
        self.calculate_button = Button(text="Calcular IMC", )
        self.calculate_button.bind(on_press=self.calculate_imc)
        self.add_widget(self.calculate_button)
        

        # ONDE VAI SAIR O RESULTADO
        self.result_label = Label(text="")
        self.add_widget(self.result_label)

    def calculate_imc(self, instance):
        try:
            altura = float(self.weight_input.text)
            peso = float(self.height_input.text)

            if altura <= 0 or peso <= 0:
                self.result_label.text = "Altura e peso devem ser positivos."
                return

            # CALCULO DO IMC 
            imc = altura / (peso** 2)

            # AQUI SAO AS CLASSIFICAÇOES 
            if imc < 18.5:
                classification = "Baixo peso"
            elif 18.5 <= imc < 24.9:
                classification = "Peso normal"
            elif 25 <= imc < 29.9:
                classification = "Sobrepeso"
            else:
                classification = "Obesidade"

            self.result_label.text = f"IMC: {imc:.2f} ({classification})"
        except ValueError:
            self.result_label.text = "Por favor, insira valores válidos."

class IMCApp(App):
    def build(self):
        return IMCCalculator()

if __name__ == "__main__":
    IMCApp().run()

