package com.two;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BJ1436 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        StringBuilder sb=new StringBuilder();

        int N=Integer.parseInt(st.nextToken());
        int num=666;
        int cnt=0;

        while(true){
            if(String.valueOf(num).contains("666")){
                cnt++;
            }
            if(cnt==N)
                break;
            num++;

        }
        System.out.println(num);
    }
}
