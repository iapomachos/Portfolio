
#include <stdio.h>
#include <stdlib.h>

main()
{
       float a,b,h,x,y;
       printf("Askhsh 1\n");
       printf("dwse times\n");
       
       scanf("%f %f %f",&a,&b,&h);
       x=a;
       y=0;
       while(x<b)
       {    
        y=1/(1+x*x);       
        printf("to x einai: %f  \n",x);
        printf("to y einai: %f  \n",y);
        printf(" \n");
        x=x+h;
       }
      system("Pause"); 
}
