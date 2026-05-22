# try, except, else e finally
try:
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print(' dividiu por zero')
else:
    print('não deu erro')
finally:
    print('fechar arquivo')