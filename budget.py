import kivy
kivy.require('1.9.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.listview import ListItemButton
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty

class ExpenseListButton(ListItemButton):
    pass


class Budget(BoxLayout):

    allowance = 100
    expenseTotal = 0
    expenseInput = ObjectProperty()
    expenseList = ObjectProperty()
    budgetOutput = StringProperty()

    def __init__(self):
        BoxLayout.__init__(self)
        self.budgetOutput = str(220)

    def calcBalance(self):
        expense = 0
        for i in self.expenseList.adapter.data:
            expense += int(i)
        self.budgetOutput = str(self.allowance - expense)

    def addExpense(self):
        # Get expense from expenseInput
        expense = self.expenseInput.text

        # Add to expenseList
        self.expenseList.adapter.data.extend([expense])

        # Reset expenseList
        self.expenseList._trigger_reset_populate()

        # Update balance
        self.calcBalance()

    def removeExpense(self):
        # If a list item in expenseList is selected
        if self.expenseList.adapter.selection:

            # Get the text from the selected item
            selection = self.expenseList.adapter.selection[0].text

            # Remove matching item from expenseList
            self.expenseList.adapter.data.remove(selection)

            # Reset expenseList
            self.expenseList._trigger_reset_populate()

        # Update balance
        self.calcBalance()


class BudgetApp(App):

    def build(self):
        return Budget()


if __name__ == '__main__':
    BudgetApp().run()