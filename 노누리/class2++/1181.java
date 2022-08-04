package com.one;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashSet;
import java.util.StringTokenizer;

public class BJ1181 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        StringBuilder sb=new StringBuilder();

        int N=Integer.parseInt(st.nextToken());
        String[] arr=new String[N];

        for(int i=0;i<N;i++){
            st=new StringTokenizer(br.readLine());
            arr[i]=st.nextToken();
        }

        //중복 제거
        HashSet<String> set=new HashSet<>(Arrays.asList(arr));
        arr=set.toArray(new String[0]);

        //다중 정렬
        //정렬 기준 변경 -> 문자열 길이, 알파벳 순서
        Arrays.sort(arr, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                int ans=o1.length()-o2.length();
                //문자열 길이가 같지 않으면 문자열 길이로 정렬
                if(ans!=0)
                    return o1.length()-o2.length();
                //문자열 길이가 같으면 알파벳순서로 정렬
                else
                    return o1.compareTo(o2);
            }
        });

        for(int i=0;i<arr.length;i++){
            sb.append(arr[i]+"\n");
        }

        System.out.println(sb);
    }
}
