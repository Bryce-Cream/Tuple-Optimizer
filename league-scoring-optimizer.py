import itertools

def load_pairs(filename):
    pairs = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                try:
                    x, y = map(int, line.split())
                    pairs.append((x, y))
                except ValueError:
                    print(f"Skipping invalid line: {line}")
    return pairs

def find_min_sum(pairs):
    min_sum = float('inf')
    best_combo = None
    total_pairs = len(pairs)
    
    # Pick 3 unique pairs for x-values (first column)
    for x_indices in itertools.combinations(range(total_pairs), 3):
        x_sum = sum(pairs[i][0] for i in x_indices)
        
        # Remaining indices for y-values (second column)
        remaining_indices = set(range(total_pairs)) - set(x_indices)
        
        # Pick 5 unique pairs for y-values
        for y_indices in itertools.combinations(remaining_indices, 5):
            y_sum = sum(pairs[i][1] for i in y_indices)
            total = x_sum + y_sum
            
            if total < min_sum:
                min_sum = total
                best_combo = (x_indices, y_indices)
    
    return min_sum, best_combo

def main():
    filename = 'input.txt' 
    pairs = load_pairs(filename)
    
    if len(pairs) < 8:
        print("Error: Need at least 8 pairs to select from.")
        return
    
    min_sum, best_combo = find_min_sum(pairs)
    
    if best_combo:
        print()
        print(f"Lowest Total: {min_sum} & Final Score: {min_sum-288}")
        print()
        print(f"Gross Scores Used: {[pairs[i][0] for i in best_combo[0]]}")
        print(f"Net Scores Used: {[pairs[i][1] for i in best_combo[1]]}")
        print()
    else:
        print("No valid combination found.")

if __name__ == "__main__":
    main()

