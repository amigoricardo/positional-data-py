# Positional Data
Conversion of positional data files to csv.

## Installation
1. Install `pipx`:
Follow these [instructions](https://pypa.github.io/pipx/installation/)

2. Make sure you have `awk` installed:
```shell
awk --version
```

3. Install `positional-data`:
```shell
pipx install positional-data
```
## Usage
```shell
positional-data -c <Columns Definition File> <Data File>
```
### `<Columns Definition File>`
File defining the position of each field in a row. 
It must follow the format `<initial_position>,<length>,<field_name>`.
Example:
```csv
1,4,Random four digit code
5,2,Two digits starting at the fifth 
5,8,Another field
13,3,Second last
16,2,Last field
```

### `<Data File>`
File containing positional data.
Example:
```
20151100001500101227021992023111814
20151100001500301404051992023111214
20151100001500401404011980035111814
20151100001500402205061981034221814
```