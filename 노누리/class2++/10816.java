package com.five;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

public class BJ10816 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        StringBuilder sb=new StringBuilder();

        int N=Integer.parseInt(st.nextToken());
        HashMap<Integer,Integer> hash=new HashMap<>();
        st=new StringTokenizer(br.readLine());
        for(int i=0;i<N;i++){
            int n=Integer.parseInt(st.nextToken());
            if(hash.get(n)==null){
                hash.put(n,0);
            }
            hash.put(n,hash.get(n)+1);
        }
        st=new StringTokenizer(br.readLine());
        int M=Integer.parseInt(st.nextToken());
        st=new StringTokenizer(br.readLine());
        for(int i=0;i<M;i++){
            int num=Integer.parseInt(st.nextToken());
            if(hash.get(num)==null){
                sb.append("0 ");
            }else{
                sb.append(hash.get(num)+" ");
            }
        }

        System.out.println(sb);
    }
}
