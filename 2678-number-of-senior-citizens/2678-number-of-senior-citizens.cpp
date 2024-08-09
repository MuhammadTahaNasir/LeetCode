class Solution {
public:
    int countSeniors(const vector<string>& details) {
        int seniorCount = 0;

        for (const string& passengerInfo : details) {
            // Extract the age directly from characters at index 11 and 12
            int age = (passengerInfo[11] - '0') * 10 + (passengerInfo[12] - '0');

            // Check if the passenger is a senior (strictly over 60 years old)
            if (age > 60) {
                ++seniorCount;
            }
        }

        return seniorCount;
    }
};