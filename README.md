# JerseyCTF — Fantaxotic Fledgeling

**Category:** Binary Exploitation
**Difficulty:** Medium
**Event:** JerseyCTF (Jeopardy-style)
**Author:** Reuvi (Challenge Writer)

**Fantaxotic Fledgeling** is a pwn challenge authored for JerseyCTF. The repo includes the challenge source/binary and a reference solve to help competitors (or instructors) re-host and practice the exploit path.

---

## Build (Local)

Requirements: a Linux-like environment with **gcc** and **make**.

```bash
git clone https://github.com/Reuvi/JerseyCTF-Fantaxotic_Fledgeling
cd JerseyCTF-Fantaxotic_Fledgeling

make
```

---

## Run

Run the binary directly:

```bash
./fantaxotic_fledgling
```

Expose it as a TCP service to simulate the remote challenge:

```bash
# Listen on port 1337 and fork for each connection
socat -T 60 TCP-LISTEN:1337,reuseaddr,fork EXEC:./fantaxotic_fledgling
# In another terminal:
nc 127.0.0.1 1337
```

---

## Solving

```bash
python3 -m pip install --upgrade pwntools
# Local example:
python3 solve.py
# Or
python3 solve.py HOST PORT
```
## Flag Format

Typical JerseyCTF flags look like:

```
jctf{...}
```

## Educational Use

This repository is provided for learning and re-hosting in CTF practice environments. If you reuse or adapt the challenge, please credit the author and the event.

---

##  Attribution

**Challenge Writer:** Reuvi
**Event:** JerseyCTF (Binary Exploitation)
