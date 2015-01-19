#include <stdio.h>
#include <stdlib.h>

int main(){
	int frames = 0;

	while (1){
		if (!(frames = (frames + 1)%20) == 0){
		  printf("%d %d\n", rand() % 400, rand() % 400 ); // generates random coordinates to turn on 
	    } else {
          printf("break\n");
	    }
	}
}