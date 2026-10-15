class TimeMap {
public:
    unordered_map<string, vector<pair<int, string>>> store;

    TimeMap() {}
    
    void set(string key, string value, int timestamp){
        store[key].push_back({timestamp, value});
    }
    
    string get(string key, int timestamp) {
        auto& arr = store[key];

        int l = 0, r = arr.size() - 1;
        string res = "";

        while (l <= r){
            int m = l + ( r - l ) / 2;

            if (arr[m].first <= timestamp) {
                res = arr[m].second;
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
        return res;
    }
};

// auto& creates a reference (an alias) to the original variable instead of making a copy
