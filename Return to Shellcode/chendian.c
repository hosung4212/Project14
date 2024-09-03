#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>
 int main(){
     char name[100];
     int howlong;
     int count=1;
     scanf("%s",name);
     howlong=strlen(name);
     for (int i=howlong; i>0;i--){
         printf("%x",name[i-1]);
         if (count%8==0){
             printf("\n");
         }
         count++;
     }
     return 0;
 }               
