package com.four;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BJ4153 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        while(true){
            st=new StringTokenizer(br.readLine());
            int a=Integer.parseInt(st.nextToken());
            int b=Integer.parseInt(st.nextToken());
            int c=Integer.parseInt(st.nextToken());

            if(a==0 && b==0 && c==0){
                break;
            }
            int[] arr={a,b,c};
            Arrays.sort(arr);
            int max=arr[2];
            int mid=arr[1];
            int min=arr[0];

            if(max*max==(mid*mid + min*min)){
                System.out.println("right");
            }else{
                System.out.println("wrong");
            }

        }
    }
}
