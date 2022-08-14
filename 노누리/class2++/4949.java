package com.five;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Stack;

public class BJ4949 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb=new StringBuilder();

        while(true){
            String[] str=br.readLine().split("");
            Stack<String> stack=new Stack<>();
            String ans="";

            if(str.length==1 && str[0].equals(".")){
                break;
            }

            for(int i=0;i<str.length;i++){
                System.out.println(str[i]);
                if(str[i].equals(")")){
                    if(stack.isEmpty()){
                        ans="no";
                    }
                    while(!stack.isEmpty()){
                        String s=stack.pop();
                        if(s.equals("[")){
                            ans="no";
                            break;
                        }else if(s.equals("(")){
                            break;
                        }
                    }
                }else if(str[i].equals("]")){
                    if(stack.isEmpty()){
                        ans="no";
                    }
                    while(!stack.isEmpty()){
                        String s=stack.pop();
                        if(s.equals("(")){
                            ans="no";
                            break;
                        }else if(s.equals("[")){
                            break;
                        }
                    }
                }else if(str[i].equals("(") || str[i].equals("[")){
                    stack.push(str[i]);
                }
            }

            if(!stack.isEmpty())
                ans="no";

            if(ans.equals("no")){
                sb.append("no\n");
            }else{
                sb.append("yes\n");
            }
        }
        System.out.println(sb);
    }
}
