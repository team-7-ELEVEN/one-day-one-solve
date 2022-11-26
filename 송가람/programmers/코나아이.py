def solution(n):
    n = str(n)
    def make_one(n, cnt):
        sum = 0
        str_n = str(n)
        for i in str_n:
            sum += (int(i) ** 2)
        cnt += 1
        if sum == (int(n) ** 2):
            return -1

        elif sum == 1:
            return cnt

        else:
            return make_one(sum, cnt)

    return make_one(n, 0)

print(solution(19))


# select mc.id, mc.name, sum(cu.amount) sa from merchants mc, card_usages cu where mc.id=cu.id group by mc.id, mc.name order by sa desc;

# 자바버전
# class Solution {
#     public int solution(int n) {
#         String newN = String.valueOf(n);

#         return makeOne(n,0);
#     }

#     private int makeOne (int n, int cnt) {
#         int sum = 0;
#         String strN = String.valueOf(n);
#         for (char c : strN.toCharArray()) {
#             double temp = Math.pow(Character.getNumericValue(c), 2);
#             sum += temp;
#         }
#         cnt += 1;
#         if (sum == Math.pow(Character.getNumericValue(n),2)) return -1;
#         else if (sum == 1) return cnt;
#         else return makeOne(sum, cnt);
#     }
# }