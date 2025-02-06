## Projeto
O projeto é uma iniciativa do uso de criptografia com python utilizando o algoritmo AES. A criptografia AES emprega um tamanho de chave variável de 128, 192 ou 256 bits com um tamanho de bloco fixo de 128 bits. É uma técnica de criptografia rápida e eficaz que pode ser usada em muitos aplicativos diferentes. Ataques de força bruta e criptografia diferencial não podem quebrar a criptografia AES.

Neste projeto, temos um texto no arquivo message.txt que será criptografado ou decriptogrado e um arquivo de saída com o resultado será escrito.

## Requisitos do projeto

Para rodar esta aplicação, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Python + pip](https://www.python.org/downloads/) e [virtualenv](https://virtualenv.pypa.io/en/latest/).

## Execute o projeto

Execute os comandos abaixo:
```bash
# Clone este repositório
$ git clone https://github.com/Daniel-Alencar/aes

# Acesse a pasta do projeto no terminal/cmd
$ cd aes

# Crie um ambiente virtual para instalar as dependências
$ virtualenv myENV

# Entre no ambiente virtual
$ source myENV/bin/activate

# Instale as dependências
$ pip3 install -r requirements.txt

# Execute a aplicação
$ python3 aes.py
```

## Passo-a-passo

- Utilize o comando "python3 aes.py" para inicializar o programa
- Ao iniciar o programa, ele lhe dará opção de escolher entre 'encriptar' ou 'decriptar'
  - Se escolher encriptar (1) ou decriptar (2), ele encriptará ou decriptará o texto do arquivo "message.txt"
- Logo após, você deve fornecer a chave (key) com 32 caracteres
  - Sugestão de Chave: E$JurYWpmmQ@Mom$&Wd3xktjtC%8ePjC

Ao final do processo, você terá um novo arquivo criado com o seu texto criptografado ou decriptografado (dependendo da sua escolha).
