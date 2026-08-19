class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rowMasks = {}
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                bit = seat - 2
                rowMasks[row] = rowMasks.get(row, 0) | (1 << bit)
        
        LEFT = 0b00001111    # seats 2-5
        MIDDLE = 0b00111100  # seats 4-7
        RIGHT = 0b11110000   # seats 6-9
        
        # Rows with no reservations at all (not in dict) can always fit 2 groups
        result = (n - len(rowMasks)) * 2
        
        for mask in rowMasks.values():
            if (mask & LEFT) == 0 and (mask & RIGHT) == 0:
                result += 2
            elif (mask & LEFT) == 0 or (mask & MIDDLE) == 0 or (mask & RIGHT) == 0:
                result += 1
        
        return result