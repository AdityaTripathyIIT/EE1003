#include <stdio.h>
#include <openssl/rand.h>
//1 - tails; 0 - heads
void run_sim(int max_tosses, double *points){
  int count = 0;
  for(int i = 1; i <= max_tosses; i++){
    unsigned char buffer1[2];
    if(RAND_bytes(buffer1, sizeof(buffer1)) != 1){
      printf("Error in generating random bytes.\n");
    }
    int toss1 = 1 & buffer1[0];
    int toss2 = 1 & buffer1[1];
    if (toss1 || toss2){
      count++;
    }
    points[2*i] = i;
    points[2*i + 1] = ((float)(count))/(i);
    printf("%d %lf\n", i, points[2*i+1]);
  }
  return ;
}
