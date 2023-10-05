#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define f(x,a) (x*x-a)
#define g(x) (2*x)
//float

main()
{
       float a,x;
       printf("Askhsh 7\n");
       printf("Dwse a thetiko \n");
       scanf("%f",&a);
       
       while(a<=0) //elegxos tou a
       {
          printf("Dwse a thetiko \n");
          scanf("%f",&a);  
       }
       
       x=a;
       while( (fabs(f(x,a)) > pow(10,-6)) & (g(x) > pow(10,-6)) )
       {    
            x = x-(f(x,a)/g(x));       
            printf("x,f(x) %1.20f %1.20f  \n",x,f(x,a));
            printf(" \n");
       }
       
       printf("sqrt   %1.20f  \n",sqrt(a));
       
       system("Pause"); 
}
