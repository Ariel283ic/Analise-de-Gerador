import sympy as sp
import tkinter as tk
from tkinter import messagebox
import time


# Creating an input area:
def input_numbers():
    global E1, U1, Ui1, R1, Ri1, I1
    E1 = value_entry1.get()
    U1 = value_entry2.get()
    Ui1 = value_entry3.get()
    R1 = value_entry4.get()
    Ri1 = value_entry5.get()
    I1 = value_entry6.get()


# Organizing inputs given:
def check_inputs():
    global answer
    answer = {}  # Creating a dict to organize final data

    if E1:
        answer['E'] = sp.S(E1)
    if U1:
        answer['U'] = sp.S(U1)
    if Ui1:
        answer['Ui'] = sp.S(Ui1)
    if R1:
        answer['R'] = sp.S(R1)
    if Ri1:
        answer['Ri'] = sp.S(Ri1)
    if I1:
        answer['I'] = sp.S(I1)


# Separating unknown symbols:
def separate_data():
    symbols_used = ['E', 'U', 'Ui', 'R', 'Ri', 'I']  # All symbols for parsing
    data_given = [E1, U1, Ui1, R1, Ri1, I1]  # All data for parsing

    global unknown_symbols
    unknown_symbols = []  # Creating list for unknown symbols

    for data, symbol in zip(data_given, symbols_used):
        if not data:
            unknown_symbols.append(symbol)


# Setting Equations:
def creating_equations():
    E, U, Ui, R, Ri, I = sp.symbols('E U Ui R Ri I')  # Setting Equation Symbols
    eq1 = sp.Eq(U + Ui - E, 0)
    eq2 = sp.Eq(Ri * I - Ui, 0)
    eq3 = sp.Eq(R * I - U, 0)
    return eq1, eq2, eq3


def defining_equations(eq1, eq2, eq3):
    # Replacing known data in equations:
    for symbol, data in zip(answer.keys(), answer.values()):
        eq1 = eq1.subs(symbol, data)
        eq2 = eq2.subs(symbol, data)
        eq3 = eq3.subs(symbol, data)

    Equations = [eq1, eq2, eq3]

    Equations[:] = [x for x in Equations if x != True]  # Subs can replace equations with a boolean, that give an
    # error later.
    return Equations


def check_linearity():
    global nonlinear
    if 'Ri' in unknown_symbols and 'I' in unknown_symbols:
        nonlinear = True
    elif 'E' in unknown_symbols and 'U' in unknown_symbols:
        nonlinear = True
    elif 'R' in unknown_symbols and 'I' in unknown_symbols:
        nonlinear = True


def infinite_simulations():
    global already_solved
    for symbol in unknown_symbols:
        answer[f'{symbol}'] = "[0, infinito)"
    already_solved = True


def infinite_or_not():
    if 'E' in unknown_symbols:
        if 'U' in unknown_symbols and 'R' in unknown_symbols:
            infinite_simulations()
        elif 'Ui' in unknown_symbols and 'Ri' in unknown_symbols:
            infinite_simulations()
    elif 'R' in unknown_symbols and 'Ri' in unknown_symbols and 'I' in unknown_symbols:
        infinite_simulations()


def solve_equations(Equations):
    # Solving equations:
    success_solved = False  # Fail-safe for less than 2 var given.
    global answer, nonlinear, already_solved
    nonlinear = False
    already_solved = False  # Fail-Safe for errors

    if len(unknown_symbols) == 6:
        messagebox.showwarning('Sério?', 'Nenhuma informação foi providenciada.')
        answer_label1['text'] = "E = U + Ui"
        answer_label2['text'] = "U = I × R"
        answer_label3['text'] = "Ui = I × Ri"
        answer_label4['text'] = "R = U ÷ I"
        answer_label5['text'] = "Ri = Ui ÷ I"
        answer_label6['text'] = "I = U ÷ R ou Ui ÷ Ri"
        already_solved = True

    elif len(unknown_symbols) >= 4:  # This will give an error if its 4 or 5 or 6.
        messagebox.showerror('Erro', 'Não foi possível realizar o cálculo devido a falta de informações.')
        already_solved = True

    elif len(unknown_symbols) == 3:  # Sending the checks to a function
        infinite_or_not()

    if not already_solved and len(unknown_symbols) > 2:
        solved = sp.nonlinsolve(Equations, unknown_symbols)
        success_solved = True

    elif not already_solved and len(unknown_symbols) <= 2 and len(unknown_symbols) != 0:
        check_linearity()
        if nonlinear:
            solved = sp.nonlinsolve(Equations, unknown_symbols)
        else:
            solved = sp.linsolve(Equations, unknown_symbols)
        success_solved = True

    if success_solved:
        # Parsing solved data:
        solved = list(solved).pop()  # Transforming FiniteSet in a Tuple.

        for number, symbol in zip(solved, unknown_symbols):
            answer[f'{symbol}'] = f'{number}'


# Outputting solved data:
def output_print():
    try:
        answer_label1['text'] = "E = " + str(answer['E'])
        answer_label2['text'] = "U = " + str(answer['U'])
        answer_label3['text'] = "Ui = " + str(answer['Ui'])
        answer_label4['text'] = "R = " + str(answer['R'])
        answer_label5['text'] = "Ri = " + str(answer['Ri'])
        answer_label6['text'] = "I = " + str(answer['I'])

    except KeyError:
        pass


def initiate():
    answer_label1['text'] = "==================="
    answer_label2['text'] = "==================="
    answer_label3['text'] = "==================="
    answer_label4['text'] = "==================="
    answer_label5['text'] = "==================="
    answer_label6['text'] = "==================="
    answer_label1.update()  # For some motive this updates all of them

    input_numbers()
    check_inputs()
    separate_data()
    eq1, eq2, eq3 = creating_equations()
    solve_equations(defining_equations(eq1, eq2, eq3))
    time.sleep(0.3)
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

    SLWid = 0.08  # It's easier to change if you set a var.
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
