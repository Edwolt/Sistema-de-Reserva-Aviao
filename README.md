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
No servidor Threads são utilizadas para representar o fluxo do servidor sendo utilizado por multiplos clientes, todos quais podem acessor e manipular um mesmo conjunto de dados que representam as poltronas do avião. Adicionalmente também existe a Thread timer que possui como função a garantia de uma repetição periódica da atualização do client. 

### Semáforos
No lado do servidor, caso 2 ou mais clientes busquem reservar uma mesma poltrona em um mesmo período de tempo Semáforos foram implementados e utilizados na resolução do conflito. 

No lado do client em si não foi necessária a implementação de nenhum Semáforo, pois além de manter a periodicidade do processo a única ação da Thread timer é chamar uma função write_event que força o loop principal a se atualizar pois é a única função segura de ser usada fora da Thread principal no PySimpleGui.
## Dependências

python 3.10

## Instalação

Instalando dependências.
```bash
pip install pysimplegui
```

## Utilização

Antes de tudo é necessário rodar o servidor.
```bash
python3 server.py
```

Em sequência o comando abaixo pode ser usado para criar um total de no máximo 10 clientes simultaneamente, cada qual possui uma interface gráfica que facilita e interação e visualização de quais poltronas estão disponíveis. 

Poltronas verdes estão disponíveis, vermelhas ocupadas e azuis representam as poltronas escolhidas pelo cliente.
```bash
python3 client.py
```

## Referências
- [Digital Ocean: Python Socket](https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client)
- [Real Python: Python Thread](https://realpython.com/intro-to-python-threading/)
- [Documentação de Threading do Python](https://docs.python.org/3/library/threading.html)
