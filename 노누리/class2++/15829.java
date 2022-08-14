package com.five;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class BJ15829 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

        BigInteger ans=new BigInteger("0");
        BigInteger n=new BigInteger("1234567891");
        int N=Integer.parseInt(br.readLine());
        String str=br.readLine();

        for(int i=0;i<N;i++){
            Integer num=(int)(str.charAt(i))-96;
            BigInteger al=new BigInteger(""+num);
            BigInteger pow=new BigInteger("1");
            for(int j=0;j<i;j++){
                pow=pow.multiply(new BigInteger(""+31));
            }
            ans=ans.add(al.multiply(new BigInteger(""+pow)));
            //ans+=((int) (str.charAt(i))-96)*Math.pow(31,i);
        }

        System.out.println(ans.remainder(n));
    }
}
