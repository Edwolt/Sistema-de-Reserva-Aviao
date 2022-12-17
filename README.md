# Sistema de Reserva de Avião
### [Link do Projeto](https://github.com/Edwolt/Sistema-de-Reserva-Aviao)

- Antonio Italo Lima Lopes - 12542290
- Eduardo Souza Rocha - 11218692
- Mateus Israel Silva - 11735042
- Pedro Guilherme Reis Teixeira - 12542477
- Pedro Henrique Vilela do Nascimento - 12803492

## Introdução
Projeto final da disciplina de Sistemas Operacionais do segundo semestre de 2022, SSC0140, ensinada pelo docente **Rodolfo Ipolito Meneguette**.

O objetivo do nosso projeto é a implementação de um servidor que simula o sistema de reservas de um avião e dos clientes que utilizariam do mesmo.

### Threads
Threads são utilizadas para representar o fluxo do uso do servidor por multiplos clientes, todas quais podem acessar e manipular um mesmo conjunto de dados que representa as poltronas do servidor.

### Semáforos
Caso 2 ou mais clientes busquem reservar uma mesma poltrona em um mesmo período de tempo Semáforos foram implementados e utilizados na resolução do conflito.
## Dependências

python 3.10

## Instalação

Instalando dependências
```bash
pip install pysimplegui
```

## Utilização

Ligar o servidor
```bash
python3 server.py
```

Para criar um cliente use
```bash
python3 client.py
```
O cliente possui uma interface gráfica

Pode se criar quantos clientes quiser

## Referências
- [Digital Ocean: Python Socket](https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client)
- [Real Python: Python Thread](https://realpython.com/intro-to-python-threading/)
- [Documentação de Threading do Python](https://docs.python.org/3/library/threading.html)
