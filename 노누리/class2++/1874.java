package com.three;

import java.util.Scanner;
import java.util.Stack;

public class BJ1874 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        StringBuilder sb=new StringBuilder();
        boolean flag=false;

        int N=sc.nextInt();
        Stack<Integer> stack=new Stack<>();
        boolean[] numbers=new boolean[N];

        for(int i=0;i<N;i++) {
            int num = sc.nextInt();

            if(stack.size()!=0){
                if (stack.peek() == num) {
                    stack.pop();
                    sb.append("-\n");
                } else if (stack.peek() > num) {
                    flag = true;
                    break;
                } else {
                    for(int n=stack.peek()+1;n<num+1;n++){
                        if(numbers[n-1]) continue;
                        stack.push(n);
                        numbers[n-1]=true;
                        sb.append("+\n");
                    }
                    stack.pop();
                    sb.append("-\n");
                }
            }else{
                for(int n=1;n<num+1;n++){
                    if(numbers[n-1]) continue;
                    stack.push(n);
                    numbers[n-1]=true;
                    sb.append("+\n");
                }
                stack.pop();
                sb.append("-\n");
            }
        }

        if(flag){
            System.out.println("NO");
        }else{
            System.out.println(sb);
        }
    }
}
