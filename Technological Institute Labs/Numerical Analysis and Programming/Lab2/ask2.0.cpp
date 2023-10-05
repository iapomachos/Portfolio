#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define f(x) ((1/(1+pow(x,2)))

//while loop

main()
{
       float a,b,h,x,y;
       printf("Askhsh 1\n");
       printf("dwse times\n");
       
       scanf("%f %f %f",&a,&b,&h);
       x=a;
       y=0;
       while(x<=b)
       {    
            y=f(x);       
            printf("to x einai: %f  \n",x);
            printf("to y einai: %f  \n",y);
            printf(" \n");
            x=x+h;
       }
      system("Pause"); 
}
