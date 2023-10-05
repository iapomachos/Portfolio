#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define f(x) (1/(1+pow(x,2)))

double myexp(double x);
main(){
    
    int exit=0;
    double x;
    
    printf("dwse x");
    printf("\n");
    scanf("%lf",&x);
    
    
    
    printf("%20.16lf \t %20.16lf \n",myexp(x),exp(x));
    
    system("Pause");
    }
double myexp(double x){
    
    double sum=1,oros=1;
    int i=1;
    
    while(fabs(oros)>pow(10,-15)){
       // printf("dwse x");
        oros=oros*x/i++;
        sum+=oros;
        
        }
        
        return sum;
    
    }
