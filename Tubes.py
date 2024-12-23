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
