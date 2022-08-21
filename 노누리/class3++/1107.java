package com.seven;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BJ1107 {
    static boolean[] numbers=new boolean[10];
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

        int N=Integer.parseInt(br.readLine());
        int M=Integer.parseInt(br.readLine());
        int comp=Integer.MAX_VALUE;
        if(M!=0){
            StringTokenizer st=new StringTokenizer(br.readLine());
            for(int i=0;i<M;i++){
                int num=Integer.parseInt(st.nextToken());
                numbers[num]=true;
            }

            for(int t=0;t<=999999;t++){
                String tmp=String.valueOf(t);
                boolean flag=false;
                for(int i=0;i<tmp.length();i++){
                    if(numbers[tmp.charAt(i)-'0']){
                        flag=true;
                        break;
                    }
                }
                if(flag) continue;

                comp=Math.min(comp,Math.abs(t-N)+tmp.length());
            }
            comp=Math.min(Math.abs(100-N),comp);
        }else{
            comp=Math.min(Math.abs(100-N),String.valueOf(N).length());
        }

        System.out.println(comp);
    }
}
