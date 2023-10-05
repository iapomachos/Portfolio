#include <stdio.h>
#include <stdlib.h>
#include <math.h>



main()
{
       double sum,x,i,oros;
       
       printf("Askhsh paragontiko\n");
       printf("dwse timh x\n");
       
       scanf("%lf",&x);
       sum = 1;
       oros = 1;
       i = 1;
       
       while(fabs(oros) > pow(10,-15))
       {    
            oros = oros * x/i;
            sum = sum + oros;
            printf("o oros %1.0f einai o %20.16lf     \n",i,sum);
            i++;  
       }
       printf("                  %20.16lf \n",exp(x));
       
      system("Pause"); 
}
