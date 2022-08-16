package com.four;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BJ1978 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        int N=Integer.parseInt(st.nextToken());
        st=new StringTokenizer(br.readLine());
        int cnt=0;
        for(int i=0;i<N;i++){
            int num=Integer.parseInt(st.nextToken());
            if(num==1) continue;

            boolean[] prime=new boolean[num+1];
            for(int j=2;j<Math.sqrt(num+1);j++){
                int idx=1;
                while(idx*j<num+1){
                    prime[idx*j]=true;
                    idx++;
                }
            }

            if(!prime[num]){
                cnt++;
            }
        }

        System.out.println(cnt);
    }
}
