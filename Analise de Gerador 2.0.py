import sympy as sp
import tkinter as tk
from tkinter import messagebox
import time


# Creating an input area:
def input_numbers():
    E1 = value_entry1.get()
    U1 = value_entry2.get()
    Ui1 = value_entry3.get()
    R1 = value_entry4.get()
    Ri1 = value_entry5.get()
    I1 = value_entry6.get()

    return [E1, U1, Ui1, R1, Ri1, I1]


# Parsing all inputs:
def parse_data(values):
    global answer, unknown_symbols
    answer = {}  # Creating a dict to organize final data.
    unknown_symbols = []  # Creating list for unknown symbols
    symbols = ['E', 'U', 'Ui', 'R', 'Ri', 'I']

    for value, symbol in zip(values, symbols):  # Much easier to parse with loops.
        if value:
            answer[symbol] = sp.S(value)
        else:
            unknown_symbols.append(symbol)


# Setting Equations:
def creating_equations():
    E, U, Ui, R, Ri, I = sp.symbols('E U Ui R Ri I')  # Setting Equation Symbols
    eq1 = sp.Eq(U + Ui - E, 0)
    eq2 = sp.Eq(Ri * I - Ui, 0)
    eq3 = sp.Eq(R * I - U, 0)

    # Replacing known data in equations:
    for symbol, data in answer.items():
        eq1 = eq1.subs(symbol, data)
        eq2 = eq2.subs(symbol, data)
        eq3 = eq3.subs(symbol, data)

    equations = [eq1, eq2, eq3]

    return equations


# Merging all checks:
def checks(equations):
    length = len(unknown_symbols)

    global already_solved, empty_symbols, nonlinear, infinite

    if False in equations:
        something_is_wrong(equations)
    else:
        equations[:] = [x for x in equations if x != True]

        if length == 6:  # Empty data check.
            messagebox.showwarning('Sério?', 'Nenhuma informação foi providenciada.')
            empty_symbols = True
            already_solved = True

        elif length >= 4:  # Not enough data check.
            if len(unknown_symbols) >= 4:
                messagebox.showerror('Erro', 'Não foi possível realizar o cálculo devido a falta de informações.')
                already_solved = True

        elif length == 3:  # Infinite check.
            infinite_check = ['E' in unknown_symbols and 'U' in unknown_symbols and 'R' in unknown_symbols,
                              'E' in unknown_symbols and 'Ui' in unknown_symbols and 'Ri' in unknown_symbols,
                              'R' in unknown_symbols and 'Ri' in unknown_symbols and 'I' in unknown_symbols]

            if any(infinite_check):
                infinite = True
                already_solved = True

        elif length == 2:  # Non linear check.
            check_linearity = ['Ri' in unknown_symbols and 'I' in unknown_symbols,
                               'E' in unknown_symbols and 'U' in unknown_symbols,
                               'R' in unknown_symbols and 'I' in unknown_symbols]

            if any(check_linearity):
                nonlinear = True

        elif length == 0:  # Complete set check.
            already_solved = True

        return equations


def something_is_wrong(equations):
    # Finding where is wrong.
    global different_output, already_solved
    error_equation = []
    for equation in equations:
        if equation == False:
            error_equation.append(True)
        else:
            error_equation.append(False)

    if error_equation[0]:
        different_output = True
        try:
            messagebox.showerror('Erro', f"E, U e Ui não batem, {answer['E']} = {answer['U']} + {answer['Ui']}")
            answer_label1['text'] = f"{answer['E']} = {answer['U']} + {answer['Ui']}"
            answer_label2['text'] = f"{answer['U']} = {answer['E']} - {answer['Ui']}"
            answer_label3['text'] = f"{answer['Ui']} = {answer['E']} - {answer['U']}"
            answer_label1['bg'] = answer_label2['bg'] = answer_label3['bg'] = 'red'
        except:
            messagebox.showerror('Erro', 'E, U e Ui não batem')
        else:
            already_solved = True

    if error_equation[1]:
        different_output = True
        try:
            messagebox.showerror('Erro', f"Ui, Ri e I não batem, {answer['Ui']} = {answer['Ri']} × {answer['I']}")
            answer_label3['text'] = f"{answer['Ui']} = {answer['Ri']} × {answer['I']}"
            answer_label5['text'] = f"{answer['Ri']} = {answer['Ui']} ÷ {answer['I']}"
            answer_label6['text'] = f"{answer['I']} = {answer['Ui']} ÷ {answer['Ri']}"
            answer_label3['bg'] = answer_label5['bg'] = answer_label6['bg'] = 'red'
        except:
            messagebox.showerror('Erro', 'Ui, Ri e I não batem')
        else:
            already_solved = True

    if error_equation[2]:
        different_output = True
        try:
            messagebox.showerror('Erro', f"U, R e I não batem, {answer['U']} = {answer['R']} × {answer['I']}")
            answer_label2['text'] = f"{answer['U']} = {answer['R']} × {answer['I']}"
            answer_label4['text'] = f"{answer['R']} = {answer['U']} ÷ {answer['I']}"
            answer_label6['text'] = f"{answer['I']} = {answer['U']} ÷ {answer['R']}"
            answer_label2['bg'] = answer_label4['bg'] = answer_label6['bg'] = 'red'
        except:
            messagebox.showerror('Erro', 'U, R e I não batem')
        else:
            already_solved = True


def solve_equations(Equations):
    # Solving equations:
    success_solved = False
    global answer, nonlinear, already_solved, empty_symbols, different_output, infinite
    nonlinear = False
    infinite = False
    different_output = False
    empty_symbols = False
    already_solved = False

    equations = checks(Equations)

    if not already_solved:
        if nonlinear:
            solved = sp.nonlinsolve(equations, unknown_symbols)
        else:
            solved = sp.linsolve(equations, unknown_symbols)
        success_solved = True

    if success_solved:
        # Parsing solved data:
        solved = list(solved).pop()  # Transforming FiniteSet in a Tuple.

        for number, symbol in zip(solved, unknown_symbols):
            answer[f'{symbol}'] = f'{number}'

    elif infinite:
        for symbol in unknown_symbols:
                answer[f'{symbol}'] = "[0, infinito)"


# Outputting solved data:
def output_print():
    if different_output:
        pass
    elif empty_symbols:
        answer_label1['text'] = "E = U + Ui"
        answer_label2['text'] = "U = I × R"
        answer_label3['text'] = "Ui = I × Ri"
        answer_label4['text'] = "R = U ÷ I"
        answer_label5['text'] = "Ri = Ui ÷ I"
        answer_label6['text'] = "I = U ÷ R ou Ui ÷ Ri"
    else:
        try:
            answer_label1['text'] = "E = " + str(answer['E']) + ' Volts'
            answer_label2['text'] = "U = " + str(answer['U']) + ' Volts'
            answer_label3['text'] = "Ui = " + str(answer['Ui']) + ' Volts'
            answer_label4['text'] = "R = " + str(answer['R']) + ' Ohms'
            answer_label5['text'] = "Ri = " + str(answer['Ri']) + ' Ohms'
            answer_label6['text'] = "I = " + str(answer['I']) + ' Ampere'
        except KeyError:
            pass


def initiate():
    answer_label1['text'] = "==================="
    answer_label2['text'] = "==================="
    answer_label3['text'] = "==================="
    answer_label4['text'] = "==================="
    answer_label5['text'] = "==================="
    answer_label6['text'] = "==================="
    answer_label1['bg'] = answer_label2['bg'] = answer_label3['bg'] = answer_label4['bg'] = answer_label5['bg'] = answer_label6['bg'] = 'honeydew'
    answer_label1.update()  # For some motive this updates all of them

    parse_data(input_numbers())
    solve_equations(creating_equations())
    time.sleep(0.1)
    output_print()


if __name__ == "__main__":
    # Creating Gui:
    root = tk.Tk()  # Main window
    root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())  # New trick to open window in front.
    root.title("Análise de Gerador")
    root.iconbitmap("battery.ico")
    root.geometry('500x200')

    root.minsize(500, 200)  # Minimum size for window

    frame = tk.Frame(root, bg="gray")
    frame.pack(fill="both", expand=True)

    # GUI locational vars:
    SLWid = 0.08
    SLHei = 1 / 6
    VEWid = 0.25

    # Labels to the entry
    symbol_label1 = tk.Label(frame, font=("Lucida Grande", 15), text="E", borderwidth=2, relief="groove")
    symbol_label1.place(relx=0, rely=0, relwidth=SLWid, relheight=SLHei)

    symbol_label2 = tk.Label(frame, font=("Lucida Grande", 15), text="U", borderwidth=2, relief="groove")
    symbol_label2.place(relx=0, rely=SLHei, relwidth=SLWid, relheight=SLHei)

    symbol_label3 = tk.Label(frame, font=("Lucida Grande", 15), text="Ui", borderwidth=2, relief="groove")
    symbol_label3.place(relx=0, rely=SLHei * 2, relwidth=SLWid, relheight=SLHei)

    symbol_label4 = tk.Label(frame, font=("Lucida Grande", 15), text="R", borderwidth=2, relief="groove")
    symbol_label4.place(relx=0, rely=SLHei * 3, relwidth=SLWid, relheight=SLHei)

    symbol_label5 = tk.Label(frame, font=("Lucida Grande", 15), text="Ri", borderwidth=2, relief="groove")
    symbol_label5.place(relx=0, rely=SLHei * 4, relwidth=SLWid, relheight=SLHei)

    symbol_label6 = tk.Label(frame, font=("Lucida Grande", 15), text="I", borderwidth=2, relief="groove")
    symbol_label6.place(relx=0, rely=SLHei * 5, relwidth=SLWid, relheight=SLHei)

    # Entry to the values
    value_entry1 = tk.Entry(frame, bg="dark gray")
    value_entry1.place(relx=SLWid, rely=0, relwidth=VEWid, relheight=SLHei)

    value_entry2 = tk.Entry(frame, bg="dark gray")
    value_entry2.place(relx=SLWid, rely=SLHei, relwidth=VEWid, relheight=SLHei)

    value_entry3 = tk.Entry(frame, bg="dark gray")
    value_entry3.place(relx=SLWid, rely=SLHei * 2, relwidth=VEWid, relheight=SLHei)

    value_entry4 = tk.Entry(frame, bg="dark gray")
    value_entry4.place(relx=SLWid, rely=SLHei * 3, relwidth=VEWid, relheight=SLHei)

    value_entry5 = tk.Entry(frame, bg="dark gray")
    value_entry5.place(relx=SLWid, rely=SLHei * 4, relwidth=VEWid, relheight=SLHei)

    value_entry6 = tk.Entry(frame, bg="dark gray")
    value_entry6.place(relx=SLWid, rely=SLHei * 5, relwidth=VEWid, relheight=SLHei)

    # Button to the function:
    calculate_button = tk.Button(frame, text="Calcular", bg="light gray", command=lambda: initiate())
    calculate_button.place(relx=SLWid + VEWid, rely=0, relwidth=0.15, relheight=1)

    # Label to answer:
    answer_label1 = tk.Label(frame, font=("Lucida Grande", 12), borderwidth=2, relief="sunken")
    answer_label1.place(relx=SLWid + VEWid + 0.15, rely=0, relwidth=1 - (SLWid + VEWid + 0.15), relheight=SLHei)

    answer_label2 = tk.Label(frame, font=("Lucida Grande", 12), borderwidth=2, relief="sunken")
    answer_label2.place(relx=SLWid + VEWid + 0.15, rely=SLHei, relwidth=1 - (SLWid + VEWid + 0.15), relheight=SLHei)

    answer_label3 = tk.Label(frame, font=("Lucida Grande", 12), borderwidth=2, relief="sunken")
    answer_label3.place(relx=SLWid + VEWid + 0.15, rely=SLHei * 2, relwidth=1 - (SLWid + VEWid + 0.15), relheight=SLHei)

    answer_label4 = tk.Label(frame, font=("Lucida Grande", 13), borderwidth=2, relief="sunken")
    answer_label4.place(relx=SLWid + VEWid + 0.15, rely=SLHei * 3, relwidth=1 - (SLWid + VEWid + 0.15), relheight=SLHei)

    answer_label5 = tk.Label(frame, font=("Lucida Grande", 13), borderwidth=2, relief="sunken")
    answer_label5.place(relx=SLWid + VEWid + 0.15, rely=SLHei * 4, relwidth=1 - (SLWid + VEWid + 0.15), relheight=SLHei)

    answer_label6 = tk.Label(frame, font=("Lucida Grande", 13), borderwidth=2, relief="sunken")
    answer_label6.place(relx=SLWid + VEWid + 0.15, rely=SLHei * 5, relwidth=1 - (SLWid + VEWid + 0.15), relheight=SLHei)

    root.mainloop()
