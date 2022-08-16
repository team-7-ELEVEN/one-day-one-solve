package com.four;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BJ2805 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        int N=Integer.parseInt(st.nextToken());
        int M=Integer.parseInt(st.nextToken());

        int[] tree=new int[N];
        long left=0;
        long right=0;

        st=new StringTokenizer(br.readLine());
        for(int i=0;i<N;i++){
            tree[i]=Integer.parseInt(st.nextToken());
            if(right<tree[i]) {
                right = tree[i];
            }
        }

        while(left<right){
            long mid=(left+right)/2;
            long sum=0;
            for(int i=0;i<N;i++){
                if(mid<tree[i]){
                    sum+=(tree[i]-mid);
                }
            }
            if(sum<M){
                right=mid;
            }else{
                left=mid+1;
            }
        }

        System.out.println(left-1);
    }
}
