class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int five = 0, ten = 0; // To track the number of $5 and $10 bills

        for (int bill : bills) {
            if (bill == 5) {
                five++; // We receive a $5 bill
            } 
            else if (bill == 10) {
                if (five == 0) return false; // We need one $5 bill to give change
                five--; // Use one $5 bill as change
                ten++; // Receive one $10 bill
            } 
            else { // The bill is $20
                if (ten > 0 && five > 0) { // Prefer giving one $10 and one $5 as change
                    ten--;
                    five--;
                } 
                else if (five >= 3) { // Otherwise, give three $5 bills as change
                    five -= 3;
                } 
                else { // Not enough change
                    return false;
                }
            }
        }

        return true; // Successfully gave change for all customers
    }
};
