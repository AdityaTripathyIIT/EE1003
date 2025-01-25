#include <stdio.h>
#include <openssl/rand.h>
//1 - tails; 0 - heads
int bernoulli(double p){
    unsigned char random_byte;
    if (RAND_bytes(&random_byte, 1) != 1) {
        fprintf(stderr, "Error generating random byte\n");
        exit(1);
    }
  /*
  * we generate a random number between 0 and 255, then scale it down to a number from   
  * 0 to 1 and we retun 0 only if the number is between 0 and p
  */ 
    double random_value = random_byte / 255.0;
    return random_value < p ? 0 : 1; 
}

void run_sim(int max_tosses, double p, double *points){
  int count = 0;
  for(int i = 1; i <= max_tosses; i++){
    int toss1 = bernoulli(p);
    int toss2 = bernoulli(p);
    if(toss1 || toss2){
      count++;
    }
    points[2*i] = i;
    points[2*i + 1] = ((float)(count))/(i);
    printf("%d %lf\n", i, points[2*i+1]);
  }
  return ;
}
