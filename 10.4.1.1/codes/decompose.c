#include <stdio.h>
#include <stdlib.h>

#define N 2

double **make_mat(){
    double **mat = malloc(sizeof(double *) * N);
    for (int i = 0; i < N; i++){
        mat[i] = malloc(sizeof(double) * N);
    }
    return mat;
}

double ***get_LU(){
    double **U = make_mat();
    double **L = make_mat();
    
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            L[i][j] = (i == j) ? 1 : 0;
        }
    }

    for (int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            scanf("%lf", &U[i][j]);
        }
    }

    int step_no = 0;
    while(step_no < N - 1){
        if (U[step_no][step_no] == 0) {
            int check = 0;
            for (int i = step_no + 1; i < N; i++){
                if(U[i][step_no] != 0){
                    double *temp = U[step_no];
                    U[step_no] = U[i];
                    U[i] = temp;
                    check = 1;
                    break;
                }
            }
            if(check == 0){
                printf("Singular Matrix, can't decompose.\n");
                exit(-1);
            }
        }
        for(int i = step_no+1; i < N; i++){
            double multiplier = U[i][step_no] / U[step_no][step_no];
            L[i][step_no] = multiplier;
            for(int j = step_no; j < N; j++){
                U[i][j] -= multiplier * U[step_no][j];
            }
        }
        step_no++;
    }

    double ***ret_arr = malloc(sizeof(double **) * 2);
    ret_arr[0] = L;
    ret_arr[1] = U;
    return ret_arr;
}

int main(){
    double ***LU = get_LU();
    
    printf("L matrix:\n");
    for (int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            printf("%lf ", LU[0][i][j]);
        }
        printf("\n");
    }
    
    printf("U matrix:\n");
    for (int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            printf("%lf ", LU[1][i][j]);
        }
        printf("\n");
    }
    
    return 0;
}

