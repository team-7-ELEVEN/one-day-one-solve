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
        int left=1;
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
                right=mid-1;
            else
                left=mid+1;
        }

        System.out.println(right);
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

/*
* import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int K = sc.nextInt();
        long N = sc.nextLong();
        long[] arr = new long[K];
        long max = 0;
        for (int i = 0; i < K; i++) {
            arr[i] = sc.nextLong();
            max = Math.max(max, arr[i]);
        }
        //이분탐색
        long left = 1; //랜선길이는 자연수므로  최솟값 1로 세팅해야함
        long right = max;
        while (left <= right) {
            long mid = (left + right) / 2;
            long sum = 0;
            for (int i = 0; i < K; i++) { // 자른 개수 합
                sum += (arr[i] / mid);
            }
            if (sum >= N) { //더 많은 랜선 나온 경우 더 크게 잘라줘야함
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        System.out.println(right);
    }
}*/