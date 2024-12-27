import random
import matplotlib.pyplot as plt
import time
import string
from prettytable import PrettyTable
import sys

#GENERATE RANDOM NAME
def generate_random_block_name():
    name_length = 4 
    random_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=name_length))
    return f"Block{random_name}"

#GENERATE INVENTORY
def generate_inventory(size):
    inventory = []
    while len(inventory) < size:
        item_name = generate_random_block_name()  # Generating random block names
        quantity = random.randint(1, 64)
        inventory.append({"name": item_name, "quantity": quantity})
    return inventory

# Iterative sorting
def iterative_sort(inventory):
    n = len(inventory)
    for i in range(n):
        for j in range(0, n - i - 1):
            if inventory[j]['quantity'] > inventory[j + 1]['quantity']:
                inventory[j], inventory[j + 1] = inventory[j + 1], inventory[j]
    return inventory

# BUBBLE SORT
def recursive_sort(inventory):
    def sort_helper(inv, n):
        if n <= 1: 
            return inv
        for i in range(n - 1):  
            if inv[i]['quantity'] > inv[i + 1]['quantity']:
                inv[i], inv[i + 1] = inv[i + 1], inv[i]
        return sort_helper(inv, n - 1)  # Recur for the rest

    return sort_helper(inventory, len(inventory))

# Linear Search
def iterative_search(inventory, target):
    for item in inventory:
        if item['name'] == target:
            return item
    return None

# BINARY SEARCH
def recursive_search(inventory, target):
    if not inventory:
        return None
    if inventory[0]['name'] == target:
        return inventory[0]
    return recursive_search(inventory[1:], target)

def compare_sorting_times(inventory):
    start_iterative = time.time()
    iterative_sort(inventory.copy())
    end_iterative = time.time()

    start_recursive = time.time()
    recursive_sort(inventory.copy())
    end_recursive = time.time()

    return end_iterative - start_iterative, end_recursive - start_recursive

def compare_search_times(inventory, target):
    start_iterative = time.time()
    iterative_search(inventory, target)
    end_iterative = time.time()

    start_recursive = time.time()
    recursive_search(inventory, target)
    end_recursive = time.time()

    return end_iterative - start_iterative, end_recursive - start_recursive

def main():
    inventory = []
    
    iter_search_times = []
    rec_search_times = []
    iter_sort_times = []
    rec_sort_times = []
    
    run_labels = [] 

    while True:
        print("\n=== Minecraft Inventory Algorithm Performance ===")
        print("7. Compare Algorithm Performance")
        print("0. Exit")

        choice = input("Enter your choice: ")

        sys.setrecursionlimit(999999)

        if choice == "7":
            size = int(input("Enter the number of items to generate: "))
            inventory = generate_inventory(size)

            it_sort_time, rec_sort_time = compare_sorting_times(inventory)

            target = inventory[random.randint(0, len(inventory) - 1)]['name']
            print(f"\nRandomly chosen block for searching: {target}")

            index_found = next((i for i, item in enumerate(inventory) if item['name'] == target), -1)
            if index_found != -1:
                print(f"Target found at index: {index_found}")
            else:
                print("Target not found in the inventory.")

            it_search_time, rec_search_time = compare_search_times(inventory, target)

            iter_search_times.append(it_search_time)
            rec_search_times.append(rec_search_time)
            iter_sort_times.append(it_sort_time)
            rec_sort_times.append(rec_sort_time)

            run_labels.append(f"{len(run_labels) + 1}st run (Size: {size})")

            table = PrettyTable(["Run", "Iterative Search (s)", "Recursive Search (s)", "Iterative Sort (s)", "Recursive Sort (s)"])
            
            for i in range(len(run_labels)):
                table.add_row([run_labels[i],
                               f"{iter_search_times[i]:.6f}",
                               f"{rec_search_times[i]:.6f}",
                               f"{iter_sort_times[i]:.6f}",
                               f"{rec_sort_times[i]:.6f}"])

            print(table)

            # Plot results (showing the progress of times)
            plt.clf() 
            plt.plot(run_labels, iter_sort_times, label="Iterative Sort", color='blue', marker='o')
            plt.plot(run_labels, rec_sort_times, label="Recursive Sort", color='pink', marker='o')
            plt.plot(run_labels, iter_search_times, label="Iterative Search", color='black', marker='o')
            plt.plot(run_labels, rec_search_times, label="Recursive Search", color='red', marker='o')

            plt.ylabel("Time (seconds)")
            plt.title("Algorithm Performance Comparison")
            plt.xlabel("Run")
            plt.xticks(rotation=45) 
            plt.legend()
            plt.show()

        elif choice == "0":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
