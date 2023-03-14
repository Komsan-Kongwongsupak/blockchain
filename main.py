from components.Transaction import Transaction
from components.Token import Token

tr1 = Transaction(10, '11', '22')
tr2 = Transaction(20, '33', '44')
tr3 = Transaction(30, '55', '66')
tr4 = Transaction(40, '77', '88')

tk = Token(2)
tk.update_nodes([tr1, tr2])
tk.update_nodes([tr3, tr4])

print(tk)
