package com.five;

import java.util.Scanner;

public class BJ2839 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);

        int N=sc.nextInt();
        int ans=0;

        if(N%5==0){
            ans+=N/5;
            System.out.println(ans);
        }else{
            while(N>0){
                if(N%5==0){
                    ans+=N/5;
                    System.out.println(ans);
                    break;
                }else if(N==0){
                    System.out.println(ans);
                    break;
                }else if(N<3){
                    System.out.println(-1);
                    break;
                }
                N-=3;
                ans++;
            }
        }
    }
}
