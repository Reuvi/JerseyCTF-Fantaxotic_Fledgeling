#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>

#define MESSAGE_SIZE 64
#define CANARY_SIZE 16
#define LOCK_SIZE 9

//Challenge Author: Buffer_Overbyte

void win() {
    printf("You solved it locally\n");
    exit(0);
}

void vuln() {
    char lock[LOCK_SIZE];
    unsigned short canary[CANARY_SIZE];
    char message[MESSAGE_SIZE];
    
    canary[0] = (rand() % 255) & 0xFFFF;
    lock[0] = 'D';
    lock[1] = 'E';
    lock[2] = 'A';
    lock[3] = 'D';
    lock[4] = 'R';
    lock[5] = 'I';
    lock[6] = 'C';
    lock[7] = 'E';
    lock[8] = '\0';

    printf("Send your message: ");
    fflush(stdout);

    unsigned short stack_canary = canary[0];
    
    scanf("%s", &message);
    
    if (stack_canary != canary[0]) {
        printf("Stack corruption detected!\n");
        exit(1);
    }
    
    if (strcmp(lock, "DEADBEEF") == 0) {
        win();
    }

    printf("Message sent!\n");
}

int main() {
    srand(time(NULL));
    setbuf(stdout, NULL);
    vuln();
    return 0;
}
