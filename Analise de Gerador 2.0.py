import sympy as sp
import tkinter as tk
from tkinter import messagebox
import time


# Creating an input area:
class Window:
    def __init__(self):
        super().__init__()

        self.root = tk.Tk()  # Main window
        self.root.eval('tk::PlaceWindow %s center' % self.root.winfo_toplevel())  # New trick to open window in front.
        self.root.title("Análise de Gerador")
        try:
            self.root.iconbitmap("battery.ico")
        except:
            pass

        self.root.geometry('500x200')

        self.root.minsize(500, 200)  # Minimum size for window

        self.frame = tk.Frame(self.root, bg="gray")
        self.frame.pack(fill="both", expand=True)

        # GUI locational vars:
        self.SLWid = 0.08
        self.SLHei = 1 / 6
        self.VEWid = 0.25

        self.set_ui_components()
        self.reset_output_labels_text()

        self.root.mainloop()

    def set_ui_components(self):
        # Labels to the entry
        self.symbol_label1 = tk.Label(self.frame, font=("Lucida Grande", 15), text="E", borderwidth=2, relief="groove")
        self.symbol_label1.place(relx=0, rely=0, relwidth=self.SLWid, relheight=self.SLHei)

        self.symbol_label2 = tk.Label(self.frame, font=("Lucida Grande", 15), text="U", borderwidth=2, relief="groove")
        self.symbol_label2.place(relx=0, rely=self.SLHei, relwidth=self.SLWid, relheight=self.SLHei)

        self.symbol_label3 = tk.Label(self.frame, font=("Lucida Grande", 15), text="Ui", borderwidth=2, relief="groove")
        self.symbol_label3.place(relx=0, rely=self.SLHei * 2, relwidth=self.SLWid, relheight=self.SLHei)

        self.symbol_label4 = tk.Label(self.frame, font=("Lucida Grande", 15), text="R", borderwidth=2, relief="groove")
        self.symbol_label4.place(relx=0, rely=self.SLHei * 3, relwidth=self.SLWid, relheight=self.SLHei)

        self.symbol_label5 = tk.Label(self.frame, font=("Lucida Grande", 15), text="Ri", borderwidth=2, relief="groove")
        self.symbol_label5.place(relx=0, rely=self.SLHei * 4, relwidth=self.SLWid, relheight=self.SLHei)

        self.symbol_label6 = tk.Label(self.frame, font=("Lucida Grande", 15), text="I", borderwidth=2, relief="groove")
        self.symbol_label6.place(relx=0, rely=self.SLHei * 5, relwidth=self.SLWid, relheight=self.SLHei)

        # Entry to the values
        self.value_entry1 = tk.Entry(self.frame, bg="dark gray")
        self.value_entry1.place(relx=self.SLWid, rely=0, relwidth=self.VEWid, relheight=self.SLHei)

        self.value_entry2 = tk.Entry(self.frame, bg="dark gray")
        self.value_entry2.place(relx=self.SLWid, rely=self.SLHei, relwidth=self.VEWid, relheight=self.SLHei)

        self.value_entry3 = tk.Entry(self.frame, bg="dark gray")
        self.value_entry3.place(relx=self.SLWid, rely=self.SLHei * 2, relwidth=self.VEWid, relheight=self.SLHei)

        self.value_entry4 = tk.Entry(self.frame, bg="dark gray")
        self.value_entry4.place(relx=self.SLWid, rely=self.SLHei * 3, relwidth=self.VEWid, relheight=self.SLHei)

        self.value_entry5 = tk.Entry(self.frame, bg="dark gray")
        self.value_entry5.place(relx=self.SLWid, rely=self.SLHei * 4, relwidth=self.VEWid, relheight=self.SLHei)

        self.value_entry6 = tk.Entry(self.frame, bg="dark gray")
        self.value_entry6.place(relx=self.SLWid, rely=self.SLHei * 5, relwidth=self.VEWid, relheight=self.SLHei)

        # Button to the function:
        self.calculate_button = tk.Button(self.frame, text="Calcular", bg="light gray", command=lambda: self.initiate())
        self.calculate_button.place(relx=self.SLWid + self.VEWid, rely=0, relwidth=0.15, relheight=1)

        # Label to answer:
        self.answer_label1 = tk.Label(self.frame, font=("Lucida Grande", 12), borderwidth=2, relief="sunken")
        self.answer_label1.place(relx=self.SLWid + self.VEWid + 0.15, rely=0,
                                 relwidth=1 - (self.SLWid + self.VEWid + 0.15), relheight=self.SLHei)

        self.answer_label2 = tk.Label(self.frame, font=("Lucida Grande", 12), borderwidth=2, relief="sunken")
        self.answer_label2.place(relx=self.SLWid + self.VEWid + 0.15, rely=self.SLHei,
                                 relwidth=1 - (self.SLWid + self.VEWid + 0.15), relheight=self.SLHei)

        self.answer_label3 = tk.Label(self.frame, font=("Lucida Grande", 12), borderwidth=2, relief="sunken")
        self.answer_label3.place(relx=self.SLWid + self.VEWid + 0.15, rely=self.SLHei * 2,
                                 relwidth=1 - (self.SLWid + self.VEWid + 0.15), relheight=self.SLHei)

        self.answer_label4 = tk.Label(self.frame, font=("Lucida Grande", 13), borderwidth=2, relief="sunken")
        self.answer_label4.place(relx=self.SLWid + self.VEWid + 0.15, rely=self.SLHei * 3,
                                 relwidth=1 - (self.SLWid + self.VEWid + 0.15), relheight=self.SLHei)

        self.answer_label5 = tk.Label(self.frame, font=("Lucida Grande", 13), borderwidth=2, relief="sunken")
        self.answer_label5.place(relx=self.SLWid + self.VEWid + 0.15, rely=self.SLHei * 4,
                                 relwidth=1 - (self.SLWid + self.VEWid + 0.15), relheight=self.SLHei)

        self.answer_label6 = tk.Label(self.frame, font=("Lucida Grande", 13), borderwidth=2, relief="sunken")
        self.answer_label6.place(relx=self.SLWid + self.VEWid + 0.15, rely=self.SLHei * 5,
                                 relwidth=1 - (self.SLWid + self.VEWid + 0.15), relheight=self.SLHei)

    def reset_output_labels_text(self):
        self.answer_label1['text'] = "E = -----------------"
        self.answer_label2['text'] = "U = -----------------"
        self.answer_label3['text'] = "Ui = -----------------"
        self.answer_label4['text'] = "R = -----------------"
        self.answer_label5['text'] = "Ri = -----------------"
        self.answer_label6['text'] = "I = -----------------"

    def color_output_labels(self, color='honeydew'):
        self.answer_label1['bg'] = self.answer_label2['bg'] = self.answer_label3['bg'] = self.answer_label4['bg'] = \
            self.answer_label5['bg'] = self.answer_label6['bg'] = color
        self.answer_label1.update()

    def input_numbers(self):
        e1 = self.value_entry1.get()
        u1 = self.value_entry2.get()
        ui1 = self.value_entry3.get()
        r1 = self.value_entry4.get()
        ri1 = self.value_entry5.get()
        i1 = self.value_entry6.get()

        return [e1, u1, ui1, r1, ri1, i1]

    def parse_data(self, values, second_run=False):
        symbols = ['E', 'U', 'Ui', 'R', 'Ri', 'I']
        self.unknown_symbols = []
        if second_run:
            for symbol in self.answer.keys():
                symbols.remove(symbol)
            self.unknown_symbols = symbols
        else:
            self.answer = {}  # Creating a dict to organize final data.
            for value, symbol in zip(values, symbols):  # Much easier to parse with loops.
                if value:
                    self.answer[symbol] = sp.S(value)
                else:
                    self.unknown_symbols.append(symbol)

    def creating_equations(self, eq1_check=True, eq2_check=True, eq3_check=True):
        E, U, Ui, R, Ri, I = sp.symbols('E U Ui R Ri I')  # Setting Equation Symbols
        eq1 = sp.Eq(U + Ui - E, 0)
        eq2 = sp.Eq(Ri * I - Ui, 0)
        eq3 = sp.Eq(R * I - U, 0)
        equations = []

        # Replacing known data in equations:
        for symbol, data in self.answer.items():
            eq1 = eq1.subs(symbol, data)
            eq2 = eq2.subs(symbol, data)
            eq3 = eq3.subs(symbol, data)

        if eq1_check: equations.append(eq1)
        if eq2_check: equations.append(eq2)
        if eq3_check: equations.append(eq3)
        return equations

    # Merging all checks:
    def all_checks(self, equations):
        length = len(self.unknown_symbols)

        if False in equations:
            self.check_and_output_print_errors(equations)
        else:
            equations[:] = [x for x in equations if x != True]

            if length == 6:  # Empty data check.
                messagebox.showwarning('Sério?', 'Nenhuma informação foi providenciada.')
                self.output_print_empty()

            elif length >= 4:  # Not enough data check. STILL NEED TO DO
                self.two_symbols_process_initiate()

            elif length == 3:  # Infinite check.
                infinite_check = [
                    'E' in self.unknown_symbols and 'U' in self.unknown_symbols and 'R' in self.unknown_symbols,
                    'E' in self.unknown_symbols and 'Ui' in self.unknown_symbols and 'Ri' in self.unknown_symbols,
                    'R' in self.unknown_symbols and 'Ri' in self.unknown_symbols and 'I' in self.unknown_symbols]

                if any(infinite_check):
                    self.output_set_infinite()
                else:
                    self.solve_equations_nonlinear(equations)

            elif length == 2:  # Non linear check.
                check_linearity = ['Ri' in self.unknown_symbols and 'I' in self.unknown_symbols,
                                   'E' in self.unknown_symbols and 'U' in self.unknown_symbols,
                                   'R' in self.unknown_symbols and 'I' in self.unknown_symbols]

                if any(check_linearity):
                    self.solve_equations_nonlinear(equations)
                else:
                    self.solve_equations_linear(equations)

            elif length == 0:  # Complete set check.
                self.output_print_normal()

    def check_and_output_print_errors(self, equations):
        # Finding where is wrong.
        error_equation = []
        for equation in equations:
            if equation == False:
                error_equation.append(True)
            else:
                error_equation.append(False)

        if error_equation[0]:
            try:
                messagebox.showerror('Erro',
                                     f"E, U e Ui não batem, {self.answer['E']} = {self.answer['U']} + {self.answer['Ui']}")
                self.answer_label1['text'] = f"{self.answer['E']} = {self.answer['U']} + {self.answer['Ui']}"
                self.answer_label2['text'] = f"{self.answer['U']} = {self.answer['E']} - {self.answer['Ui']}"
                self.answer_label3['text'] = f"{self.answer['Ui']} = {self.answer['E']} - {self.answer['U']}"
                self.color_output_labels('red')
            except:
                messagebox.showerror('Erro', 'E, U e Ui não batem')

        if error_equation[1]:
            try:
                messagebox.showerror('Erro',
                                     f"Ui, Ri e I não batem, {self.answer['Ui']} = {self.answer['Ri']} × {self.answer['I']}")
                self.answer_label3['text'] = f"{self.answer['Ui']} = {self.answer['Ri']} × {self.answer['I']}"
                self.answer_label5['text'] = f"{self.answer['Ri']} = {self.answer['Ui']} ÷ {self.answer['I']}"
                self.answer_label6['text'] = f"{self.answer['I']} = {self.answer['Ui']} ÷ {self.answer['Ri']}"
                self.color_output_labels('red')
            except:
                messagebox.showerror('Erro', 'Ui, Ri e I não batem')

        if error_equation[2]:
            try:
                messagebox.showerror('Erro',
                                     f"U, R e I não batem, {self.answer['U']} = {self.answer['R']} × {self.answer['I']}")
                self.answer_label2['text'] = f"{self.answer['U']} = {self.answer['R']} × {self.answer['I']}"
                self.answer_label4['text'] = f"{self.answer['R']} = {self.answer['U']} ÷ {self.answer['I']}"
                self.answer_label6['text'] = f"{self.answer['I']} = {self.answer['U']} ÷ {self.answer['R']}"
                self.color_output_labels('red')
            except:
                messagebox.showerror('Erro', 'U, R e I não batem')

    def solve_equations_nonlinear(self, equations):
        solved = sp.nonlinsolve(equations, self.unknown_symbols)
        self.parse_solved_data_to_answer(solved)

    def solve_equations_linear(self, equations, go_on=True):
        solved = sp.linsolve(equations, self.unknown_symbols)
        self.parse_solved_data_to_answer(solved, go_on)

    def parse_solved_data_to_answer(self, solved, print=True):
        solved = list(solved).pop()
        for number, symbol in zip(solved, self.unknown_symbols):
            self.answer[f'{symbol}'] = f'{number}'
        if print:
            self.output_print_normal()

    # Outputting solved data:
    def output_print_normal(self):
        time.sleep(0.1)
        self.answer_label1['text'] = "E = " + str(self.answer['E']) + ' Volts'
        self.answer_label2['text'] = "U = " + str(self.answer['U']) + ' Volts'
        self.answer_label3['text'] = "Ui = " + str(self.answer['Ui']) + ' Volts'
        self.answer_label4['text'] = "R = " + str(self.answer['R']) + ' Ohms'
        self.answer_label5['text'] = "Ri = " + str(self.answer['Ri']) + ' Ohms'
        self.answer_label6['text'] = "I = " + str(self.answer['I']) + ' Ampere'
        self.color_output_labels('light green')

    def output_print_empty(self):
        time.sleep(0.1)
        self.answer_label1['text'] = "E = U + Ui"
        self.answer_label2['text'] = "U = I × R"
        self.answer_label3['text'] = "Ui = I × Ri"
        self.answer_label4['text'] = "R = U ÷ I"
        self.answer_label5['text'] = "Ri = Ui ÷ I"
        self.answer_label6['text'] = "I = U ÷ R ou Ui ÷ Ri"
        self.color_output_labels('light yellow')

    def output_set_infinite(self):
        for symbol in self.unknown_symbols:
            self.answer[f'{symbol}'] = "[0, infinito)"
        self.output_print_normal()

    def two_symbols_process_initiate(self):
        equation_1_symbols = ('E', 'U', 'Ui')
        equation_2_symbols = ('Ui', 'Ri', 'I')
        equation_3_symbols = ('U', 'R', 'I')
        self.symbols_new_group = []

        equation_1_add = self.find_the_right_equation(equation_1_symbols)
        equation_2_add = self.find_the_right_equation(equation_2_symbols)
        equation_3_add = self.find_the_right_equation(equation_3_symbols)

        if not any([equation_1_add, equation_2_add, equation_3_add]):
            messagebox.showerror('Erro', 'Não foi possível realizar o cálculo devido a falta de informações.')
        else:
            self.unknown_symbols = self.symbols_new_group

            self.solve_equations_linear(self.creating_equations(equation_1_add, equation_2_add, equation_3_add), False)
            self.parse_data(0, True)
            self.all_checks(self.creating_equations())

    def find_the_right_equation(self, symbols):
        symbols_in_equation = 0
        symbols_not_in_equation = []
        for symbol in symbols:
            if symbol in self.answer.keys():
                symbols_in_equation += 1
            else:
                symbols_not_in_equation.append(symbol)
        if symbols_in_equation == 2:
            self.symbols_new_group.append(symbols_not_in_equation[0])
            return True
        else:
            return False

    def initiate(self):
        self.reset_output_labels_text()
        self.parse_data(self.input_numbers())
        self.all_checks(self.creating_equations())


if __name__ == "__main__":
    window = Window()
