package com.six;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BJ1003 {
    static int[][] memo;
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb=new StringBuilder();

        int T=Integer.parseInt(br.readLine());
        memo=new int[41][2];
        memo[0][0]=1;
        memo[0][1]=0;
        memo[1][0]=0;
        memo[1][1]=1;
        for(int t=0;t<T;t++){
            int num=Integer.parseInt(br.readLine());

            fibonacci(num);
            sb.append(memo[num][0]+" "+memo[num][1]+"\n");
        }
        System.out.print(sb);
    }

    private static int[] fibonacci(int n) {
        if(memo[n][0]==0 && memo[n][1]==0){
            memo[n][0]=fibonacci(n-1)[0]+fibonacci(n-2)[0];
            memo[n][1]=fibonacci(n-1)[1]+fibonacci(n-2)[1];
        }
        return memo[n];
    }
}
