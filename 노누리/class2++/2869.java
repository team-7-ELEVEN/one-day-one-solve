package com.five;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

//Scanner 쓰면 시간초과 발생
public class BJ2869 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        double A=Integer.parseInt(st.nextToken());
        double B=Integer.parseInt(st.nextToken());
        double V=Integer.parseInt(st.nextToken());

        double ans=(V-B)/(A-B);

        System.out.println((int)Math.ceil(ans));
    }
}
