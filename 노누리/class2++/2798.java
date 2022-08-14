package com.four;

import java.util.Scanner;

public class BJ2798 {
    static int[] card;
    static int N,M;
    static int max=Integer.MIN_VALUE;
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);

        N=sc.nextInt();
        M=sc.nextInt();
        card=new int[N];

        for(int i=0;i<N;i++){
            card[i]=sc.nextInt();
        }

        comb(0,0,0);
        System.out.println(max);
    }

    private static void comb(int cnt,int start,int sum) {
        if(sum>M) return;
        if(cnt==3){
            if(sum>max){
                max=sum;
            }
            return;
        }

        for(int i=start;i<N;i++){
            comb(cnt+1,i+1,sum+card[i]);
        }
    }
}
