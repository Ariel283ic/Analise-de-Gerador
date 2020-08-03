import sympy as sp




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


if __name__ == "__main__":
    input_numbers()
    check_inputs()
    separate_data()
    eq1, eq2, eq3 = creating_equations()
    solve_equations(defining_equations(eq1, eq2, eq3))
    output_print()
