import sympy as sp

E, U, Ui, R, Ri, I = sp.symbols('E U Ui R Ri I')  # Setting Equation Symbols

# Creating an input area:
E1 = input("E: ")
U1 = input("U: ")
Ui1 = input("Ui: ")
R1 = input("R: ")
Ri1 = input("Ri: ")
I1 = input("I: ")

# Organizing inputs given:

answer = {}  # Creating a dict to organize final data

if E1:
    E = sp.S(E1)
    answer['E'] = E1
if U1:
    U = sp.S(U1)
    answer['U'] = U1
if Ui1:
    Ui = sp.S(Ui1)
    answer['Ui'] = Ui1
if R1:
    R = sp.S(R1)
    answer['R'] = R1
if Ri1:
    Ri = sp.S(Ri1)
    answer['Ri'] = Ri1
if I1:
    I = sp.S(I1)
    answer['I'] = I1

# Separating unknown symbols:

symbols_used = ['E', 'U', 'Ui', 'R', 'Ri', 'I']  # All symbols for parsing
data_given = [E1, U1, Ui1, R1, Ri1, I1]  # All data for parsing

unknown_symbols = []  # Creating list for unknown symbols

for data, symbol in zip(data_given, symbols_used):
    if not data:
        unknown_symbols.append(symbol)

# Setting Equations:
eq1 = sp.Eq(U + Ui - E, 0)
eq2 = sp.Eq(Ri * I - Ui, 0)
eq3 = sp.Eq(R * I - U, 0)

# Replacing known data in equations:
for symbol, data in zip(answer.keys(), answer.values()):
    eq1.subs(symbol, data)
    eq2.subs(symbol, data)
    eq3.subs(symbol, data)

Equations = [eq1, eq2, eq3]  # Grouping equation

Equations[:] = [x for x in Equations if x != True]  # Subs can replace equations with a boolean, that give an error later.

# Solving equations:
already_solved = False  # Fail-Safe for errors

if len(unknown_symbols) >= 4:  # This will give an error if its 4 or 5 or 6.
    print("Erro, impossivel de calcular.")
    already_solved = True

elif len(unknown_symbols) == 3 and 'R' in unknown_symbols and 'Ri' in unknown_symbols and 'I' in unknown_symbols:
    if eq1:
        answer[f'R'] = '[0, Infinito)'
        answer[f'Ri'] = '[0, Infinito)'
        answer[f'I'] = '[0, Infinito)'
    else:
        answer[f'E'] = f'{E} but should be {U + Ui}'
        answer[f'U'] = f'{U} but should be {E - Ui}'
        answer[f'Ui'] = f'{Ui} but should be {E - U}'
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

# Outputting solved data:
print('E = ' + answer['E'])
print('U = ' + answer['U'])
print('Ui = ' + answer['Ui'])
print('R = ' + answer['R'])
print('Ri = ' + answer['Ri'])
print('I = ' + answer['I'])
