#include <stdio.h>
#include <stdlib.h>
#include <math.h>



main()
{
       float sum,i,oros,x;
       printf("Askhsh paragontiko\n");
       printf("dwse timh x\n");
       
       scanf("%f",&x);
       sum = 1;
       oros = 1;
       i = 1;
       
       while(fabs(oros) > pow(10,-6))
       {    
            oros = oros * x/i;
            sum = sum + oros;
            printf("o oros %1.0f einai o %f     \n",i,sum);
            i++;
       }
       printf("%f \n",exp(x));
       
      system("Pause"); 
}
