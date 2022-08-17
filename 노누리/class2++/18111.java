package com.six;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BJ18111 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        StringBuilder sb=new StringBuilder();

        int N=Integer.parseInt(st.nextToken());
        int M=Integer.parseInt(st.nextToken());
        int B=Integer.parseInt(st.nextToken());
        int max=0;
        int min=Integer.MAX_VALUE;
        int ans=Integer.MAX_VALUE;
        int g=0;

        int[][] ground=new int[N][M];
        for(int i=0;i<N;i++){
            st=new StringTokenizer(br.readLine());
            for(int j=0;j<M;j++){
                ground[i][j]=Integer.parseInt(st.nextToken());
                if(max<ground[i][j]){
                    max=ground[i][j];
                }
                if(min>ground[i][j]){
                    min=ground[i][j];
                }
            }
        }

        for(int m=max;m>=min;m--){
            int in=B;
            int sum=0;
            for(int i=0;i<N;i++){
                for(int j=0;j<M;j++){
                    if(m<ground[i][j]){ //깎아야할때
                        sum+=2*(ground[i][j]-m);
                        in+=(ground[i][j]-m);
                    }else if(m>ground[i][j]){   //쌓아야할때
                        in-=(m-ground[i][j]);
                        sum+=(m-ground[i][j]);
                    }
                }
            }
            if(sum<ans && sum>=0 && in>=0){
                ans=sum;
                g=m;
            }
        }

        sb.append(ans+" "+g+"\n");
        System.out.println(sb);
    }
}
