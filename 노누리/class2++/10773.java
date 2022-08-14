package com.five;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class BJ10773 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int sum=0;

        int K=Integer.parseInt(br.readLine());
        Stack<Integer> stack=new Stack<>();
        for(int i=0;i<K;i++){
            int N=Integer.parseInt(br.readLine());
            if(N!=0){
                stack.push(N);
            }else{
                stack.pop();
            }
        }

        while(!stack.isEmpty()){
            sum+=stack.pop();
        }

        System.out.println(sum);
    }
}
