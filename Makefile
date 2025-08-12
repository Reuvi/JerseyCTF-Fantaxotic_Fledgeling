CC = clang
CFLAGS = -Wall -Wextra -fstack-protector-strong -fPIE -Wno-deprecated-declarations

all: fantaxotic_fledgling

fantaxotic_fledgling: fantaxotic_fledgling.c
	$(CC) $(CFLAGS) fantaxotic_fledgling.c -o fantaxotic_fledgling

clean:
	rm -f fantaxotic_fledgling
