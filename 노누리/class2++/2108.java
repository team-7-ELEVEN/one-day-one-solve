package com.four;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BJ2108 {
    public static void main(String[] args) throws IOException {
        BufferedReader bre=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(bre.readLine());
        StringBuilder sb=new StringBuilder();

        int N=Integer.parseInt(st.nextToken());
        int[] arr=new int[N];
        for(int i=0;i<N;i++){
            st=new StringTokenizer(bre.readLine());
            arr[i]=Integer.parseInt(st.nextToken());
        }

        int[] copy=arr;
        Arrays.sort(copy);

        //산술평균
        double avg= (double)Arrays.stream(arr).sum()/N;
        //중앙값
        int mid=copy[N/2];
        //최빈값
        int mode=copy[0];
        int max=-1;
        int cnt=0;
        boolean flag=false;
        for(int i=0;i<N-1;i++){
            if(copy[i]==copy[i+1]){
                cnt++;
            }else{
                cnt=0;
            }

            if(max<cnt){
                max=cnt;
                mode=copy[i];
                flag=true;
            }else if(max==cnt && flag==true){
                mode=copy[i];
                flag=false;
            }
        }
        //범위
        int range=copy[N-1]-copy[0];

        sb.append(Math.round(avg)+"\n"+mid+"\n"+mode+"\n"+range);
        System.out.println(sb);
    }
}
