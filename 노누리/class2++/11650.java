package com.five;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BJ11650 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        StringBuilder sb=new StringBuilder();

        int N=Integer.parseInt(st.nextToken());
        int[][] xy=new int[N][2];
        for(int i=0;i<N;i++){
            st=new StringTokenizer(br.readLine());
            xy[i][0]=Integer.parseInt(st.nextToken());
            xy[i][1]=Integer.parseInt(st.nextToken());
        }

        Arrays.sort(xy,(o1, o2) -> {
            if(o1[0]==o2[0]){
                return o1[1]-o2[1];
            }
            return o1[0]-o2[0];
        });

        for(int i=0;i<N;i++){
            sb.append(xy[i][0]+" "+xy[i][1]+"\n");
        }

        System.out.println(sb);
    }
}
