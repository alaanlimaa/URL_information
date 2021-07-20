'''Validação de URL com POO
Pontos de Obsevação em uma URL: caracteres padrões →  "?", "&", "https://", "http://", "www." '''

import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.clear_url(url)
        self.url_validation()

    def clear_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def url_validation(self):
        if not self.url: # Para verificar se a url esta vazia ou não,
            raise ValueError('A URL está vazia')

        padraoURL = re.compile('(http(s)?://)(www.)?bytebank.com(.br)?(/cambio)?')
        match = padraoURL.match(self.url.lower().strip())
        if not match:
            raise ValueError('URL não é VÁLIDA')

    def get_url_base(self):
        interrogacaoLocal = self.url.find('?')
        urlBase = self.url[:interrogacaoLocal]
        return urlBase

    def get_url_parameter(self):
        interrogacaoLocal = self.url.find('?')
        urlParameter = self.url[interrogacaoLocal + 1:]
        return urlParameter

    def get_parameter_value(self, parameterName):
        localParameter = self.get_url_parameter().find(parameterName)
        parameterIndex = localParameter + len(parameterName) + 1  # Localizador do parâmetro
        divParameter = self.get_url_parameter().find('&', parameterIndex)
        if divParameter == -1:
            return self.get_url_parameter()[parameterIndex:]
        else:
            return self.get_url_parameter()[parameterIndex:divParameter]

    def __len__(self):
        return len(self.url)

    def __str__(self):
        print()
        return f'A URL é: {self.url}\nBase: {self.get_url_base()}\nParâmetros: {self.get_url_parameter()}\n' \
               f'Tamnho URL: {len(self.url)} chars\n'

    def __eq__(self, other):
        return self.url == other.url


extratorURL = ExtratorURL(input('Copie ou digite a URL: ').lower().strip())
print(extratorURL)
parameterName = 'quantidade'
print(f'O parâmetro "{parameterName.upper()}" é igual à \033[1;33;40m{extratorURL.get_parameter_value(parameterName)}\033[m')

