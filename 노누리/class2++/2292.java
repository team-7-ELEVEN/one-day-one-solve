package com.four;

import java.util.Scanner;

//계차수열을 이용하려 했으나 필요없었다~~
public class BJ2292 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int num=sc.nextInt();

        //3n(n-1)+1
        int n=1;
        int sum=1;
        while(num>sum){
            sum+=n*6;
            n++;
        }

        System.out.println(n);
    }
}
