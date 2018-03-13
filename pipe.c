#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

int main(){
    int fd[2];
    pid_t pid;
    int result;
    result = pipe (fd);
    if (result < 0)
    {
        perror("pipe");
        exit (1);
    }
    pid = fork();
    if (pid < 0) {
         perror ("fork");
         exit(2);
    }

    if (pid == 0) {
         char message[80];
	 printf("From child with pid: %d\n",pid);
         printf ("Enter a message: ");
         scanf ("%s",message);
         write(fd[1], message, strlen(message));
    }
    else {
         char received[80];
         read (fd[0], received, sizeof(received));
	 printf("From parent with pid: %d\n",pid);
         printf("Message entered %s\n",received);
     }
}
