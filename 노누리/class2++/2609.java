package com.four;

import java.util.Scanner;

public class BJ2609 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);

        int a=sc.nextInt();
        int b=sc.nextInt();

        int gcdNum=gcd(a,b);

        System.out.println(gcdNum);
        System.out.println(a*b/gcdNum);
    }

    private static int gcd(int a, int b) {
        if(b==0) return a;
        return gcd(b,a%b);
    }


}
