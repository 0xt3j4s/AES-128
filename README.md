# AES-128

A pure Python implementation of encryption of AES-128 written with the goal to resemble [this](https://www.ijser.org/researchpaper/Implementation-of-Advanced-Encryption-Standard-Algorithm.pdf) paper as closely as possible; although it is compiled from different references as mentioned below. As of now, it supports the key size of 128 bits. For padding I have used '{', the text is encrypted accordingly. 

<br />


## Required Python Dependencies
- NumPy

<br />


## Usage

For trying it, clone the repo using:
```bash 
git clone https://github.com/0xt3j4s/AES-128.git
```

## Run
Run the file ``aes.py`` using:
```bash
python aes.py
```
It returns the encrypted text for the message entered.

<br />

## To-Do
- Add 192 and 256 bit versions.
- Deploy this project on a web-page.

<br />

## Documentations and References

### For AES: 
1. https://www.ijser.org/researchpaper/Implementation-of-Advanced-Encryption-Standard-Algorithm.pdf
2. https://csrc.nist.gov/csrc/media/publications/fips/197/final/documents/fips-197.pdf
3. https://engineering.purdue.edu/kak/compsec/NewLectures/Lecture8.pdf
4. https://en.wikipedia.org/wiki/AES_key_schedule
5. A lecture from Prof. Christof Paar: https://www.youtube.com/watch?v=NHuibtoL_qk

<br />

### For Galois Field:
1. https://www.youtube.com/watch?v=x1v2tX4_dkQ
2. https://sites.math.washington.edu/~morrow/336_12/papers/juan.pdf


