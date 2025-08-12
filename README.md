# JerseyCTF — Fantaxotic Fledgeling

**Category:** Binary Exploitation
**Difficulty:** Medium
**Event:** JerseyCTF (Jeopardy-style)
**Author:** Reuvi (Challenge Writer)

**Fantaxotic Fledgeling** is a pwn challenge authored for JerseyCTF. The repo includes the challenge source/binary and a reference solve to help competitors (or instructors) re-host and practice the exploit path.

---

## 🗂 Repo Contents

> Filenames may vary slightly; check the repo root for exact names.

* `fantaxotic_fledgling.c` – C source of the challenge
* `fantaxotic_fledgling` – compiled binary (for local testing)
* `Makefile` – convenience build rules (if provided)
* `solve.py` – reference exploit using pwntools (if provided)
* `notes.txt` / `Challenge Design.pdf` – author notes, intended path, constraints
* `fantaxotic_fledgling.tar.gz` – deployable artifact for CTF infra (if provided)

---

## 🔧 Build (Local)

Requirements: a Linux-like environment with **gcc** and **make**.

```bash
git clone https://github.com/Reuvi/JerseyCTF-Fantaxotic_Fledgeling
cd JerseyCTF-Fantaxotic_Fledgeling

# Preferred:
make

# If no Makefile is present, try a basic build:
gcc -o fantaxotic_fledgling fantaxotic_fledgling.c
# (If the challenge requires specific flags, see notes/Makefile in the repo.)
```

---

## ▶️ Run (Local)

Run the binary directly:

```bash
./fantaxotic_fledgling
```

Expose it as a TCP service for testing:

```bash
# Listen on port 1337 and fork for each connection
socat -T 60 TCP-LISTEN:1337,reuseaddr,fork EXEC:./fantaxotic_fledgling
# In another terminal:
nc 127.0.0.1 1337
```

---

## 🚀 Deploy (CTF Infra)

Common options (pick what your infra supports):

* **xinetd / systemd socket / socat** wrapping the binary
* **Containerized** service (Docker) exposing a TCP port
* Use the included `fantaxotic_fledgling.tar.gz` if present as the challenge artifact

**Notes:**

* Disable core dumps, set resource limits as needed
* Run as an unprivileged user in a locked-down working directory
* If ASLR/PIE/RELRO/SSP settings matter to the intended path, configure the host/container accordingly

---

## 🧪 Solving (Reference)

If `solve.py` is provided (pwntools):

```bash
python3 -m pip install --upgrade pwntools
# Local example:
python3 solve.py
# Or, if the script supports args:
python3 solve.py HOST PORT
```

If the script uses constants, edit `HOST`/`PORT` at the top of `solve.py` and re-run.

The intended vulnerability/technique is discussed in the **design notes**; read those for the exact constraints, memory layout, and mitigation assumptions.

---

## 🏁 Flag Format

Typical JerseyCTF flags look like:

```
jctf{...}
```

(Confirm your event’s exact format if you are re-hosting.)

---

## 📚 Educational Use

This repository is provided for learning and re-hosting in CTF practice environments. If you reuse or adapt the challenge, please credit the author and the event.

---

## 📄 License

See `LICENSE` if present; otherwise contact the author for permissions.

---

## ✍️ Attribution

**Challenge Writer:** Reuvi
**Event:** JerseyCTF (Binary Exploitation)
