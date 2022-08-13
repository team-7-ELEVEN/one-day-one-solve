package com.four;


import java.util.Arrays;
import java.util.Scanner;

public class BJ2231 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);

        int num=sc.nextInt();
        int ans=0;
        for(int i=1;i<num+1;i++){
            int sum=i;
            String str=String.valueOf(i);
            String[] s=str.split("");

            for(int j=0;j<s.length;j++){
                sum+=Integer.valueOf(s[j]);
            }

            if(sum==num) {
                ans=i;
                break;
            }
        }

        System.out.println(ans);
    }
}
