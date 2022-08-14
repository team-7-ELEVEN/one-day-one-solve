package com.five;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BJ1929 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        StringBuilder sb=new StringBuilder();

        int M=Integer.parseInt(st.nextToken());
        int N=Integer.parseInt(st.nextToken());

        boolean[] arr=new boolean[N+1];

        for(int i=2;i<N+1;i++){
            for(int j=2;j<N+1;j++){
                if(i*j>N) break;
                arr[i*j]=true;
            }
        }

        for(int i=M;i<N+1;i++){
            if(i<2) continue;
            if(!arr[i]){
                sb.append(i+"\n");
            }
        }

        System.out.print(sb);
    }
}
