package com.two;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.StringTokenizer;

public class BJ1654 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        StringBuilder sb=new StringBuilder();

        int K=Integer.parseInt(st.nextToken());
        int N=Integer.parseInt(st.nextToken());

        ArrayList<Integer> arr=new ArrayList<>();
        for(int i=0;i<K;i++) {
            st = new StringTokenizer(br.readLine());
            arr.add(Integer.parseInt(st.nextToken()));
        }

        // 이분탐색
        Collections.sort(arr);
        int left=0;
        int right=arr.get(arr.size()-1);
        int mid=0;

        //mid가 잘라야하는 랜선 길이
        //left==right인 경우에는 mid가 0이 될 수 있어 오류가 생기기 때문에 같을 때의 경우는 빼준다.
        //답을 출력할때는 mid-1를 해주면 된다.
        while(left<right){
            mid=(left+right)/2;

            int cnt=0;

            for(int i=0;i<arr.size();i++){
                cnt+=(arr.get(i)/mid);
            }

            if(cnt<N)
                right=mid;
            else
                left=mid+1;
        }

        System.out.println(mid-1);
        /*
        // 시간초과
        while(cnt<N){
            Collections.sort(arr);
            int num=arr.get(arr.size()-1);
            arr.remove(arr.size()-1);
            if(num%2!=0){
                arr.add(num/2);
                arr.add(num/2+1);
            }else{
                arr.add(num/2);
                arr.add(num/2);
            }

            cnt+=2;
        }
        Collections.sort(arr);
        System.out.println(arr.get(0));
         */
    }
}
