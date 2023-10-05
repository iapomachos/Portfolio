#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define f(x) ((1/(1+pow(x,2)))

//for loop

main()
{
       float a,b,h,y;
       printf("Askhsh 1\n");
       printf("dwse times\n");
       
       scanf("%f %f %f",&a,&b,&h);
       y=0;
       for(float x=a; x<=b; x+=h)
       {    
        y=f(x);      
        printf("to x einai: %f  \n",x);
        printf("to y einai: %f  \n",y);
        printf(" \n");
       }
      system("Pause"); 
}
