import sys
import math
from PyQt5.QtWidgets import *


# Create unique Button that will create instance of QPushButton using given text and
# be connected to event handler to evaluate input and update results appropriately.
# String/Integer String -> String
# Button(text, results)
#   - text: what will be displayed on the button
#   - results: string of buttons clicked by user to be evaluated

class Button:
    def __init__(self, text, results):
        self.b = QPushButton(str(text))
        self.text = text
        self.results = results
        self.b.clicked.connect(lambda: self.handle_input(self.text))

    # When user clicks a button it calls this function and performs appropriate evaluation of input
    # String -> String
    # handle_input(v)
    # -- v : value of the button clicked
    #
    # Evaluate the input and do one of:
    # -- "="  : evaluate the current input string "results" and set "results" to answer
    # -- "AC" : set "results" to blank string
    # -- "√"  : set "results" to the square root of "results"
    # -- "DEL": set "results" to itself minus the last character
    # -- else : add "v" to the end of "results" string

    def handle_input(self, v):
        if v == "=":
            res = eval(self.results.text())
            self.results.setText(str(res))
        elif v == "AC":
            self.results.setText("")
        elif v == "√":
            value = float(self.results.text())
            self.results.setText(str(math.sqrt(value)))
        elif v == "DEL":
            current_value = self.results.text()
            self.results.setText(current_value[:-1])
        else:
            current_value = self.results.text()
            new_value = current_value + str(v)
            self.results.setText(new_value)


class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.create_app()

    def create_app(self):
        # Create our grid
        grid = QGridLayout()

        # Items to add to the grid layout
        # -- results: line displaying string input by user clicking Buttons
        # -- buttons: list containing values to create Buttons with for the Calculator
        results = QLineEdit()
        buttons = ["AC", "√", "DEL", "/",
                     7,    8,    9, "*",
                     4,    5,    6, "-",
                     1,    2,    3, "+",
                     0,   ".",    "="]

        # Adding the results line to the first row of the application grid
        # stretches across the entire row
        grid.addWidget(results, 0, 0, 1, 4)

        # Buttons will be placed on grid beginning on second row and first column
        # There will be five rows, and four columns
        # Iterate through "buttons" list and create Button instance to add to the grid
        # in appropriate place.

        row = 1
        column = 0

        for button in buttons:
            if column > 3:
                column = 0
                row += 1

            button_object = Button(button, results)

            if button == "=":
                grid.addWidget(button_object.b, row, column, 1, 2)
            else:
                grid.addWidget(button_object.b, row, column, 1, 1)

            column += 1

        self.setLayout(grid)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec())
