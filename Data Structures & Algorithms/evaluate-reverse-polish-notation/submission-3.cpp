class Solution {
public:
    int evalRPN(vector<string>& tokens) {

        stack<int> stk;

        for (string c : tokens) {
            if(c == "+") {
                // C++ does not return the removed element
                int a = stk.top(); stk.pop(); 
                int b = stk.top(); stk.pop();
                stk.push(b + a);
            }
            else if(c == "-") {
                int a = stk.top(); stk.pop(); 
                int b = stk.top(); stk.pop();
                stk.push(b - a);
            }
            else if(c == "*") {
                int a = stk.top(); stk.pop(); 
                int b = stk.top(); stk.pop();
                stk.push(b * a);
            }
            else if(c == "/") {
                int a = stk.top(); stk.pop(); 
                int b = stk.top(); stk.pop();
                stk.push(b / a);
            }
            else {
                stk.push(stoi(c)); //converts a string to an integer
            }
        }
        return stk.top();
    }
};
