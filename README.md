# pybancodobrasil
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pybancodobrasil)
[![PyPI version](https://badge.fury.io/py/pybancodobrasil.svg)](https://badge.fury.io/py/pybancodobrasil)
[![Coverage Status](https://coveralls.io/repos/github/andreroggeri/pybancodobrasil/badge.svg?branch=master)](https://coveralls.io/github/andreroggeri/pybancodobrasil?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/e550387e85d315a212af/maintainability)](https://codeclimate.com/github/andreroggeri/pybancodobrasil/maintainability) [![Join the chat at https://gitter.im/pybancodobrasil/pybancodobrasil](https://badges.gitter.im/pybancodobrasil/pybancodobrasil.svg)](https://gitter.im/pybancodobrasil/pybancodobrasil?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Acesse seus extratos do Banco do Brasil pelo Python

## Instalação
Disponível via pip

`pip install pybancodobrasil`

## Aquisitando dados
Você ainda precisa ter o Warsaw instalado visto que este é um web crawler
```python
from pybancodobrasil import get

print(get(agencia, conta, senha))
```

## Contribuindo

Envie sua PR para melhorar esse projeto ! 😋