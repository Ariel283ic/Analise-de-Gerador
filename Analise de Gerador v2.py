import sympy as sp


class program:
    def get_inputs(self):
        e1 = input('Força Eletrostática: ')
        u1 = input('Tensão total do circuito: ')
        ui1 = input('Tensão do gerador: ')
        r1 = input('Resistência do circuito: ')
        ri1 = input('Resistência do gerador: ')
        i1 = input('Corrente do circuito: ')
        return self.check_inputs_for_letters([e1, u1, ui1, r1, ri1, i1])

    def check_inputs_for_letters(self, inputs):
        check = []
        for input in inputs:
            check.append(input.isnumeric() or not input)
        if all(check):
            return inputs
        else:
            print('ERRO: Apenas utilizar números no local de input!')
            return False

    def parse_input_data(self, input_data):
        self.answer = {}
        self.unknown_values = []
        symbols = ['E', 'U', 'Ui', 'R', 'Ri', 'I']
        for value, symbol in zip(input_data, symbols):
            if value:
                self.answer[symbol] = sp.S(int(value))
            else:
                self.unknown_values.append(symbol)


if __name__ == "__main__":
    test = program()
    test.parse_input_data(test.get_inputs())
    print(test.answer)
