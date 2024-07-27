import os
import sys

alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzáàâãäéèêëíìîïóòôõöúùûü!@#$%¨&*()_-+=][}{:;?\/°1234567890<>,.^~ '

parametrosInformados = sys.argv[1:]
print(parametrosInformados)

if len(parametrosInformados) == 3:
    arquivo,chave,acao = parametrosInformados
else:
    print('É preciso informar os 3 parâmetros para executar a criptografia: caminho do arquivo, chave e ação!')
    exit()

def deslocar_alfabeto(alfabeto, shift):
    return alfabeto[shift:] + alfabeto[:shift]

def pegarConteudoArquivo():
    try:
        with open(arquivo, "r", encoding='utf-8') as texto:
            conteudo = texto.read()
        return conteudo
    except FileNotFoundError:
        print("Caminho do arquivo não encontrado, tente novamente!")

def multiplicarChave(conteudo):
    if(not chave.isalpha()):
         print('A chave deve conter apenas letras!')
         exit()
    chave_nova = chave
    # se o tamanho da chave for menor que o tamanho do texto à ser criptografado 
    if len(str(chave)) < len(str(conteudo)):
            # dividir o tamanho do texto do arquivo pelo tamanho da chave
            # multiplicar a conta de cima pela chave, para repetir o texto o máximo de vezes possivel com o texto inteiro
            chave_nova = chave * (len(conteudo)//len(chave))
            if len(chave_nova) < len(conteudo):
                # aplicando substring para adicionar ao final da chave nova somente os caracteres que faltam para o fim do tamanho do texto à ser criptografado
                chave_nova += chave_nova[:(len(conteudo)-len(chave_nova))]
    else: 
        chave_nova = chave[:len(conteudo)]
    chave_nova = chave_nova.upper()
    return chave_nova

def criarArquivo(texto_cripto, acao):
    nome_do_arquivo = os.path.splitext(os.path.basename(arquivo))[0]

    if nome_do_arquivo.find('_') != -1:
        nome_do_arquivo = nome_do_arquivo.split('_')[0]

    with open('./'+nome_do_arquivo+'_'+acao+".txt", "w", encoding='utf-8') as arquivo_cripto:
        arquivo_cripto.write(texto_cripto)

def criptografia(conteudo,chave,acao):
    texto_cripto = ''
    for i, letra in enumerate(conteudo):
        id_chave = alfabeto.find(chave[i])
        alfabeto_deslocado = deslocar_alfabeto(alfabeto, id_chave)

        if acao == 'descriptografar':
            letra_cripto = alfabeto_deslocado.find(letra)
            texto_cripto += alfabeto[letra_cripto]
        elif acao == 'criptografar':
            letra_cripto = alfabeto.find(letra)
            texto_cripto += alfabeto_deslocado[letra_cripto]
        else:
            print('A ação deve ser inserida como criptografar ou descriptografar')
            exit()

    if acao == 'criptografar':
        acao = 'cripto'
    elif acao == 'descriptografar':
        acao = 'decripto'

    criarArquivo(texto_cripto, acao)

conteudo_arquivo = pegarConteudoArquivo()
chave_multiplicada = multiplicarChave(conteudo_arquivo)
criptografia(conteudo_arquivo,chave_multiplicada,acao)

