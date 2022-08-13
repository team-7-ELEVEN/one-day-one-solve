package com.four;

import java.util.Arrays;
import java.util.Scanner;

public class BJ2775 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int T=sc.nextInt();

        for(int tc=0;tc<T;tc++){
            int K=sc.nextInt();
            int N=sc.nextInt();
            int[][] apt=new int[K][N];

            for(int i=0;i<K;i++){
                if(i==0){
                    for(int j=0;j<N;j++)
                        apt[i][j]=j+1;
                }else{
                    for(int j=0;j<N;j++){
                        for(int k=0;k<=j;k++){
                            apt[i][j]+=apt[i-1][k];
                        }
                    }
                }
            }

            System.out.println(Arrays.stream(apt[K-1]).sum());
        }
    }
}
