# BrainSpin

Created by me. It's a brainfuck derivative where all memory spins every character

More details [here](https://esolangs.org/wiki/brainspin)

## Hello w/ input

```
 ,  type 72 for Cell #1 to be the ascii for H
 ,  type 69 for Cell #2 to be the ascii for E
 ,  type 76 for Cell #3 to be the ascii for L
 ...**.**+**+**+**.
```

## Hello w/o

Could be more efficient w/ some [] movement but I didn't want to think that hard.

```
 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 +++++++*++*++*++*.+.*+**+**+**.**.**+**+**+**.
```

### How to use

Just run with argument of brainspin file.

```
python interpret.py hello.bspin
```