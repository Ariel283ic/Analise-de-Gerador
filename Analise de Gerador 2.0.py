import sympy as sp
import tkinter as tk



# Creating an input area:
def input_numbers():
    global E1, U1, Ui1, R1, Ri1, I1
    E1 = input("E: ")
    U1 = input("U: ")
    Ui1 = input("Ui: ")
    R1 = input("R: ")
    Ri1 = input("Ri: ")
    I1 = input("I: ")


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

    Equations = [eq1, eq2, eq3]  # Grouping equation

    Equations[:] = [x for x in Equations if x != True]  # Subs can replace equations with a boolean, that give an
    # error later.
    return Equations


def solve_equations(Equations):
    # Solving equations:
    already_solved = False  # Fail-Safe for errors
    global answer

    if len(unknown_symbols) >= 4:  # This will give an error if its 4 or 5 or 6.
        print("Erro, impossivel de calcular.")
        already_solved = True

    elif len(unknown_symbols) == 3 and 'R' in unknown_symbols and 'Ri' in unknown_symbols and 'I' in unknown_symbols:
        if eq1:
            answer[f'R'] = '[0, Infinito)'
            answer[f'Ri'] = '[0, Infinito)'
            answer[f'I'] = '[0, Infinito)'
        else:
            answer[f'E'] = f'{E1} mas deveria ser {U1 + Ui1} = {U1} - {Ui1}'
            answer[f'U'] = f'{U1} mas deveria ser {E1 - Ui1} = {E1} - {Ui1}'
            answer[f'Ui'] = f'{Ui1} mas deveria ser {E1 - U1} = {E1} - {U1}'
            answer[f'R'] = 'Erro, tem algo de errado com os valores \"E\", \"U\" e \"Ui\"'
            answer[f'Ri'] = 'Erro, tem algo de errado com os valores \"E\", \"U\" e \"Ui\"'
            answer[f'I'] = 'Erro, tem algo de errado com os valores \"E\", \"U\" e \"Ui\"'
        already_solved = True

    if not already_solved:
        solved = sp.nonlinsolve(Equations, unknown_symbols)

        # Parsing solved data:
        solved = list(solved).pop()  # Transforming FiniteSet in a Tuple.

        for number, symbol in zip(solved, unknown_symbols):
            answer[f'{symbol}'] = f'{number}'
    print(answer)


# Outputting solved data:
def output_print():
    print('E = ' + str(answer['E']))
    print('U = ' + str(answer['U']))
    print('Ui = ' + str(answer['Ui']))
    print('R = ' + str(answer['R']))
    print('Ri = ' + str(answer['Ri']))
    print('I = ' + str(answer['I']))

def initiate():
    input_numbers()
    check_inputs()
    separate_data()
    eq1, eq2, eq3 = creating_equations()
    solve_equations(defining_equations(eq1, eq2, eq3))
    output_print()

if __name__ == "__main__":
    #Creating Gui:
    root = tk.Tk()  #Main window
    root.title("Análise de Gerador")
    root.iconbitmap("battery.ico")
    root.geometry('500x200')

    frame = tk.Frame(root, bg="gray")
    frame.pack(fill="both", expand=True)

    SLWid = 0.08  # It's easier to change if you set a var.
    SLHei = 1/6
    VEWid = 0.25

    # Labels to the entry
    symbol_label1 = tk.Label(frame, font=("Lucida Grande", 15), text="E", borderwidth=2, relief="groove")
    symbol_label1.place(relx=0, rely=0, relwidth=SLWid, relheight=SLHei)
    symbol_label2 = tk.Label(frame, font=("Lucida Grande", 15), text="U", borderwidth=2, relief="groove")
    symbol_label2.place(relx=0, rely=SLHei, relwidth=SLWid, relheight=SLHei)
    symbol_label3 = tk.Label(frame, font=("Lucida Grande", 15), text="Ui", borderwidth=2, relief="groove")
    symbol_label3.place(relx=0, rely=SLHei*2, relwidth=SLWid, relheight=SLHei)
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
    calculate_button.place(relx=SLWid+VEWid, rely=0, relwidth=0.15, relheight=1)

    # Label to answer:
    answer_label1 = tk.Label(frame, font=("Lucida Grande", 15), borderwidth=2, relief="sunken")
    answer_label1.place(relx=SLWid+VEWid+0.15, rely=0, relwidth=1-(SLWid+VEWid+0.15), relheight=SLHei)
    answer_label2 = tk.Label(frame, font=("Lucida Grande", 15), borderwidth=2, relief="sunken")
    answer_label2.place(relx=SLWid+VEWid+0.15, rely=SLHei, relwidth=1-(SLWid+VEWid+0.15), relheight=SLHei)
    answer_label3 = tk.Label(frame, font=("Lucida Grande", 15), borderwidth=2, relief="sunken")
    answer_label3.place(relx=SLWid+VEWid+0.15, rely=SLHei*2, relwidth=1-(SLWid+VEWid+0.15), relheight=SLHei)
    answer_label4 = tk.Label(frame, font=("Lucida Grande", 15), borderwidth=2, relief="sunken")
    answer_label4.place(relx=SLWid+VEWid+0.15, rely=SLHei*3, relwidth=1-(SLWid+VEWid+0.15), relheight=SLHei)
    answer_label5 = tk.Label(frame, font=("Lucida Grande", 15), borderwidth=2, relief="sunken")
    answer_label5.place(relx=SLWid+VEWid+0.15, rely=SLHei*4, relwidth=1-(SLWid+VEWid+0.15), relheight=SLHei)
    answer_label6 = tk.Label(frame, font=("Lucida Grande", 15), borderwidth=2, relief="sunken")
    answer_label6.place(relx=SLWid+VEWid+0.15, rely=SLHei*5, relwidth=1-(SLWid+VEWid+0.15), relheight=SLHei)













    root.mainloop()