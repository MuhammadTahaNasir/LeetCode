class Solution {
public:
    int countSeniors(const vector<string>& details) {
        int seniorCount = 0;

        for (const string& passengerInfo : details) {
            // Directly extract and calculate the age from the characters at indices 11 and 12
            int age = (passengerInfo[11] - '0') * 10 + (passengerInfo[12] - '0');
            
            // Increment count if the age is strictly over 60
            if (age > 60) ++seniorCount;
        }

        return seniorCount;
    }
};