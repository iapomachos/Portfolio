#include <stdio.h>
#include <stdlib.h>
#include <math.h>


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
            if(fabs(x)<1)
                y=1/(sqrt(1-pow(x,2)));
            else if(fabs(x)==1)
                y=0;
            else
                y=1/(sqrt(pow(x,2)-1));          
            printf("to x einai: %f  \n",x);
            printf("to y einai: %f  \n",y);
            printf(" \n");
            x=x+h;
       }
      system("Pause"); 
}
