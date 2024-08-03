# kouriae

Ten-segment encoder/decoder. Intended to be used via the CLI.

## Install

Fetch the latest version:

```console
python3 -m pip install git+https://github.com/tainn/kouriae.git@0.1.2
```

## Usage

The script is accessible under the `kr` or `kouriae` command. By default, or by passing in the `-e/--encode` flag, it
will encode the message. By passing in the `-d/--decode` flag, it will decode the message.

- encode: 1 parameter in (text), 2 out (encoded text, key)
- decode: 2 parameters in (encoded text, key), 1 out (decoded text)

Standard help can be output via the `-h/--help` flag:

```console
$ kr -h
usage: kr [-h] [-e] [-d]

options:
  -h, --help    show this help message and exit
  -e, --encode  Encode the text
  -d, --decode  Decode the text
```

## Example

Sample encode and decode:

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
