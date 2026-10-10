#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();

        // Store {position, speed} for each car
        vector<pair<int, int>> cars;

        for (int i = 0; i < n; i++) {
            cars.push_back({position[i], speed[i]});
        }

        // Process cars from closest to target to farthest
        sort(cars.begin(), cars.end(),
             [](const pair<int, int>& a, const pair<int, int>& b) {
                 return a.first > b.first;
             });

        vector<double> fleets;

        for (auto& car : cars) {
            int pos = car.first;
            int spd = car.second;

            double time = static_cast<double>(target - pos) / spd;

            // This car forms a new fleet only if it cannot catch
            // the fleet ahead of it.
            if (fleets.empty() || time > fleets.back()) {
                fleets.push_back(time);
            }
        }

        return fleets.size();
    }
};