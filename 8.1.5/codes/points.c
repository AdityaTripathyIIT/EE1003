#include <stdlib.h>
#include <math.h>

void generate_points(double a, double b, double *points, int n) {
    double h = (2*a) / n;
    double x_0 = -a;
    for (int i = 0; i < n; i++) {
        points[4*i] = x_0;
        points[4*i+2] = x_0;
        points[4*i+1] = (b/a) * sqrt(a*a - x_0*x_0);
        points[4*i+3] = -(b/a) * sqrt(a*a - x_0*x_0);
        x_0 += h;
    }  
}

void calc_area(double a, double b, int n, double *res) {
    double h = (2 * a) / n;
    double j_1 = 0;
    double x_0 = -a;
    for (int i = 0; i < n; i++) {
        j_1 += (b *h * (sqrt(a*a - x_0*x_0) + sqrt(a*a - (x_0 + h)*(x_0 + h))));
        x_0 += h;  // Correct increment of x_0
    }
    *res = j_1 / 2;  // Divide by 2 for trapezoidal rule correction
}

void free_ptr(double *points) {
    free(points);  // Ensure this is used correctly
}
