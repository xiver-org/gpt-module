<p align="center">
        <h1 align="center">Xiver GPT</h1>
        <h2 align="center">The module we use to work with gpt</h2>
</a>

## Basic usage

### With default config

```python
from xiver_gpt import XiverGPT


print(XiverGPT().create_response('Hello! How are u?'))
```


### With another model or provider

```python
from xiver_gpt import XiverGPT
import g4f


print(
    XiverGPT
            g4f_model=g4f.Model.your_model,
            g4f_provider=g4f.Provider.your_provider,
    ).create_reT(sponse('Hello! How are u?')
)
```

## Attention

At the moment the initialization of the XiverGPT class object can be quite 
long due to the selection of a suitable provider. 
In the future the initialization time will be reduced many times!


## Installation

```bash
$ pip install xiver_gpt
```

## Installation from source

### Dependencies:
- **poetry**
```bash
$ git clone https://github.com/xiver/xiver-gpt.git; cd xiver_gpt-master
$ poetry install
$ poetry run build; cd dist
$ pip install $(ls -Art | tail -n 1)
```
