# Cifra de Vigenère

Algoritmo de cifra de Vigenère com Python 3.10.9

# Entradas

- Caminho de um arquivo (\*.txt File)
- Uma chave com somente letras
- Ação à ser executada (criptografar ou descriptografar)

# Saídas

- O arquivo criptografado é salvo no diretório raiz da cifra: ./file_name_cripto.txt
- O arquivo descriptografado é salvo no diretório raiz da cifra: ./file_name_decripto.txt

# Comandos

Executar script

```
python cifra_vigenere.py "<file.txt>" "<key>" "<criptografar | descriptografar>"
```

# Exemplo

teste.txt = "Olá Pessoal!"

Criptografar

```
python cifra_vigenere.py "teste.txt" "grtWyK" "criptografar"

/*
 Resultado: UâùVnoyíêwí_
*/
```

Descriptografar

```
python cifra_vigenere.py "teste_cripto.txt" "grtWyK" "descriptografar"

/*
 Resultado: Olá Pessoal!
*/
```
