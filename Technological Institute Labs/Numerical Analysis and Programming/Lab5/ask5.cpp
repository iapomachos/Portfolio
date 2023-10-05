#include <stdio.h>
#include <stdlib.h>
#include <math.h>

main()
{
       
    int n;      
    printf("Askhsh horner\n");
            
    printf("dwse timh n\n");
    scanf("%d",&n);  
      
    float p[n+1];
    float q[n+1]; 
       
    float x;
    printf("dwse timh X\n");
    scanf("%f",&x);  
     
    for(int i=0;i<=n;i++)
	{
        printf("dwse timh p %d\n",i);
        scanf("%f",&p[i]);
    }
            
    q[0]=p[0];
             
             
    for(int i=1;i<=n;i++)
	{
        q[i]=p[i]+q[i-1]*x;          
    }  
        
    for(int i=0;i<=n;i++)
	{ 
        printf("gia n = %d q = %f\n",i,q[i]); 
    }      
      
    system("Pause"); 
}
