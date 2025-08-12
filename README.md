# JerseyCTF V — Fantaxotic Fledgeling

**Category:** Binary Exploitation
**Difficulty:** Medium (dynamic scoring)
**Event:** JerseyCTF V (Mar 29–30, 2025)
**Author:** Reuvi (Challenge writer)

**Fantaxotic Fledgeling** is a pwn challenge written for **JerseyCTF V**. It ships with the original C source, a prebuilt binary, author notes/design doc, and a reference exploit script. On the event scoreboard it appeared under **Binary Exploitation** with a medium rating and \~965 dynamic points. ([ctf.jerseyctf.com][1])

---

## Repo contents

* `fantaxotic_fledgling.c` — challenge source (C)
* `fantaxotic_fledgling` — prebuilt binary
* `Makefile` — local build rules
* `fantaxotic_fledgling.tar.gz` — ready-to-deploy challenge bundle
* `Challenge Design.pdf` — author design notes (theory, goals, constraints)
* `notes.txt` — quick author notes
* `solve.py` — reference exploit (pwntools)
  Files are listed on the repository landing page. ([GitHub][2])

---

## Build (local)

Requirements: a POSIX-like environment with **gcc** and **make**.

```bash
git clone https://github.com/Reuvi/JerseyCTF-Fantaxotic_Fledgeling
cd JerseyCTF-Fantaxotic_Fledgeling
make           # builds ./fantaxotic_fledgling from the C source
```

Run locally:

```bash
./fantaxotic_fledgling
```

> If you need a network service for local testing, one simple option is:
>
> ```bash
> socat -T 60 TCP-LISTEN:1337,reuseaddr,fork EXEC:./fantaxotic_fledgling
> ```
>
> Then connect with `nc 127.0.0.1 1337`.

---

## Deploy (CTF infra)

You can use the included **`fantaxotic_fledgling.tar.gz`** as the challenge artifact for your infrastructure. Typical approaches:

* **xinetd/systemd socket/socat** service wrapping the binary.
* Containerize with your event’s base image and expose the port used above.

The repository does not include a Dockerfile—infra specifics are left to the hosting platform.

---

## Solving (reference)

A **reference exploit** is provided in `solve.py` (pwntools). Typical usage:

```bash
python3 -m pip install pwntools
# Local (example):
python3 solve.py
# Remote (if the script supports args):
python3 solve.py HOST PORT
```

If the script doesn’t take CLI args, set host/port constants at the top of `solve.py` and re-run.

> The intended path and constraints are discussed in **Challenge Design.pdf** and `notes.txt`. See those documents for the exact vulnerability model and guard rails used during the competition (stack layout, mitigations, and any “ret2win/ROP” style targets). ([GitHub][3])

---

## Flag format

JerseyCTF flags typically follow the form **`jctf{...}`**. Confirm with the event’s rules if you’re hosting a mirror or re-running the challenge. ([Inv1nc’s blog][4])

---

## Attribution

* **Author/Challenge Writer:** Reuvi
* **Event:** JerseyCTF V (hosted by NJIT orgs; Jeopardy-style) ([ctftime.org][5], [jerseyctf.com][6])

---

## Educational use

This repository is provided for learning and re-hosting in CTF practice environments. Please credit the author and event if you reuse or adapt the challenge.

[1]: https://ctf.jerseyctf.com/challenges?utm_source=chatgpt.com "Challenges"
[2]: https://github.com/Reuvi/JerseyCTF-Fantaxotic_Fledgeling "GitHub - Reuvi/JerseyCTF-Fantaxotic_Fledgeling"
[3]: https://github.com/Reuvi/JerseyCTF-Fantaxotic_Fledgeling/blob/main/Challenge%20Design.pdf "JerseyCTF-Fantaxotic_Fledgeling/Challenge Design.pdf at main · Reuvi/JerseyCTF-Fantaxotic_Fledgeling · GitHub"
[4]: https://inv1nc.github.io/jerseyctf-2024-writeup?utm_source=chatgpt.com "JerseyCTF IV Writeup"
[5]: https://ctftime.org/event/2667/?utm_source=chatgpt.com "JerseyCTF V"
[6]: https://www.jerseyctf.com/?utm_source=chatgpt.com "JerseyCTF"
