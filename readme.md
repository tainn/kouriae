# kouriae

ten-segment encoder/decoder. intended to be used via the cli

## install

fetch the latest version:

```console
python3 -m pip install git+https://github.com/tainn/kouriae.git@0.1.1
```

## usage

the script is accessible under the `kr` or `kouriae` command. by default, or by passing in the `-e/--encode` flag, it
will encode the message. by passing in the `-d/--decode` flag, it will decode the message

- encode: 1 parameter in (text), 2 out (encoded text, key)
- decode: 2 parameters in (encoded text, key), 1 out (decoded text)

standard help can be output via the `-h/--help` flag:

```console
$ kr -h
usage: kr [-h] [-e] [-d]

options:
  -h, --help    show this help message and exit
  -e, --encode  Encode the text
  -d, --decode  Decode the text
```

## example

sample encode and decode:

```console
$ kr
text: hello there! how are you?

ku ra ko re ki
eJzLSM3JyY8ryUgtSlWMy8gvj0ssSo2rzC+1BwCBtQno
```

```console
$ kr -d
text: ku ra ko re ki
key: eJzLSM3JyY8ryUgtSlWMy8gvj0ssSo2rzC+1BwCBtQno

hello there! how are you?
```
