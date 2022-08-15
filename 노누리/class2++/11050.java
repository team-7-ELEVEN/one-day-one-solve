package com.five;

import java.util.Scanner;

public class BJ11050 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);

        int N=sc.nextInt();
        int K=sc.nextInt();
        int[] fac=new int[N+1];
        fac[0]=1;
        for(int i=1;i<N+1;i++){
            fac[i]=i*fac[i-1];
        }

        System.out.println(fac[N]/(fac[N-K]*fac[K]));
    }
}

