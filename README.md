# pybancodobrasil

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pybancodobrasil)
[![PyPI version](https://badge.fury.io/py/pybancodobrasil.svg)](https://badge.fury.io/py/pybancodobrasil)
[![Coverage Status](https://coveralls.io/repos/github/andreroggeri/pybancodobrasil/badge.svg?branch=master)](https://coveralls.io/github/andreroggeri/pybancodobrasil?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/e550387e85d315a212af/maintainability)](https://codeclimate.com/github/andreroggeri/pybancodobrasil/maintainability) [![Join the chat at https://gitter.im/pybancodobrasil/pybancodobrasil](https://badges.gitter.im/pybancodobrasil/pybancodobrasil.svg)](https://gitter.im/pybancodobrasil/pybancodobrasil?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Acesse seus extratos do Banco do Brasil pelo Python utilizando selenium-wire.

## Instalação

Disponível via pip

`pip install pybancodobrasil`

## Aquisitando dados

Você ainda precisa ter o Warsaw instalado visto que este é um web crawler

```python
import BrazilBank from pybancodobrasil

# baixando o driver automaticamente do chrome
banco_do_brasil = BrazilBank() # or BrazilBank(driver_name='chrome')

# baixando o driver automaticamente do firefox com a janela escondida
banco_do_brasil = BrazilBank(driver_name='firefox', headless=True)

# utilizando um outro driver
banco_do_brasil = BrazilBank(driver=MeuDriver())

# fazendo login
banco_do_brasil.login(agencia, conta, senha)

# aquisitando transações
def transacoes_callback(transacao):
    print(transacao)
    
transacoes = banco_do_brasil.get_transactions(mes, ano, transacoes_callback)

# aquisitando dados do cartao de credito
def cc_transacoes_callback(transacao):
    print(transacao)
    
cc_transacoes = banco_do_brasil.get_cardscc_transacoes_callback)
```

## Contribuindo

Envie sua PR para melhorar esse projeto ! 😋