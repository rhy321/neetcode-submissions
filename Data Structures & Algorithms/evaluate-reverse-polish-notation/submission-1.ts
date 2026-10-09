class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens: string[]): number {
        const stk: number[] = [];
        for (const c of tokens) {
            if(c === "+") {
                const a = stk.pop()!;
                const b = stk.pop()!;
                stk.push(b + a);
            }
            else if(c === "-") {
                const a = stk.pop()!;
                const b = stk.pop()!;
                stk.push(b - a);
            }
            else if(c === "*") {
                const a = stk.pop()!;
                const b = stk.pop()!;
                stk.push(b * a);
            }
            else if(c === "/") {
                const a = stk.pop()!;
                const b = stk.pop()!;
                stk.push(Math.trunc(b / a));
            } else {
                stk.push(Number(c))
            }
        }
        return stk[stk.length - 1];
    }
}
