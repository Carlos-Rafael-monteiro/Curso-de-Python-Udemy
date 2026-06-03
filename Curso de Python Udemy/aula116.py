# Criando arquivos com Python
# Usamos a função open para abrir
#um arquivo em Python ( ele pode ou não existir)
# Modos:
# r (leitura, w (escrita, x (para criação
# a (escreve ao final), b (binário
# t (modo testo), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler) 
# Writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.raname - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
caminho_arquivo = 'C:\\Users\\crafa\\Desktop\\Nova pasta Atenção\\'
caminho_arquivo += 'aula116.txt'

#arquivo = open(caminho_arquivo, 'w')

#arquivo.close()
with open(caminho_arquivo, 'w') as arquivo:
    print('Olá mundo')
    print('Arquivo vai ser fechado')
    