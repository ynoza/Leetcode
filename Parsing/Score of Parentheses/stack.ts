// https://leetcode.com/problems/score-of-parentheses/
function scoreOfParentheses(S: string): number {
    let lst=[];
    for (let i =0; i< S.length; i++){
        if (S[i] === ')'){
            let sum=0;
            while(lst.length>0 && lst[lst.length-1] !== '('){
                sum+=lst.pop();
            }
            lst.pop();
            if (sum==0) lst.push(1);
            else lst.push(2*sum);
        }
        else{
            lst.push('(');
        }
        // console.log(lst);
    }
    return lst.reduce((a, b) => a + b, 0)
};