class Solution {
public:
    string minWindow(string s, string t) {
        if(t == "") return "";

        unordered_map<char, int> countT;
        unordered_map<char, int> window;

        for (char c : t) {
            countT[c]++;
        }

        int have = 0, need = countT.size();
        int resLen = INT_MAX;
        int l = 0;
        int resL = -1, resR = -1;

        for(int r = 0; r < s.size(); r++){
            char c = s[r];
            window[c]++;

            if(countT.count(c) && window[c] == countT[c]){
                have++;
            }

            while (have == need){
                int winLen = r - l + 1;

                if(winLen < resLen){
                    resL = l;
                    resR = r;
                    resLen = winLen;
                }

                window[s[l]]--;

                if(countT.count(s[l]) && window[s[l]] < countT[s[l]]){
                    have--;
                }

                l++;
            }
        }

        return resLen == INT_MAX ? "" : s.substr(resL, resLen);

    }
};
