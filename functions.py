from collections import Counter
from typing import Generator
from itertools import combinations
from datetime import datetime
import os
## Challenge 1 
def most_common_word(words: list[str]) -> tuple[str, int]:
    if not words:
        raise ValueError("List of words is empty")
    
    word_counts = Counter(words)
    most_common = word_counts.most_common(1)[0]
    return most_common

## Challenge 2
def transpose(matrix: list[list[int]]) -> list[list[int]]:
    if not matrix or not matrix[0]:
        raise ValueError("Matrix is empty or has emtpy rows")
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

## Challenge 3
def sort_by_key(data: list[dict], key: str, secondary_key = '') -> list[dict]:
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Elements in the data should be dictionaries")
    if secondary_key:
        return sorted(data, key=lambda x: (x.get(key, None), x.get(secondary_key, None)))
    else:
        return sorted(data, key=lambda x: x.get(key, None))

## Challenge 4
def prime_generator() -> Generator[int, None, None]:
    def es_primo(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    num = 2 
    while True:
        if es_primo(num):
            yield num
        num += 1
        
## Challenge 5
def find_combinations(nums: list[int]) -> list[tuple[int, int, int]]:
    if len(nums) < 3:
        raise ValueError("Input list must have min 3 numbers")
    
    return list(combinations(nums, 3))

## Challenge 6
def file_stats(filepath: str) -> dict[str, int]:
    stats = {"lines": 0, "words": 0, "characters": 0}
    
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                stats["lines"] += 1
                stats["words"] += len(line.split())
                stats["characters"] += len(line)
    except FileNotFoundError:
        raise FileNotFoundError(f"File at {filepath} not found")
    except Exception as e:
        raise RuntimeError(f"Error ocurred while procesing {e}")
    return stats

## Challenge 7
def create_and_list_dir(dir_path: str) -> list[str]:
    os.makedirs(dir_path, exist_ok=True)
    
    def list_files_recursive(current_path: str) -> list[str]:
        files = []
        for entry in os.listdir(current_path):
            entry_path = os.path.join(current_path, entry)
            if os.path.isdir(entry_path):
                files.extend(list_files_recursive(entry_path))
            else:
                files.append(entry_path)
        return files
    
## Challenge 8
def date_difference(date1: str, date2: str) -> int:
    try:
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")
        
        difference = (d2 - d1).days
        return abs(difference)
    except ValueError:
        raise ValueError("Invalid format. Use 'YYYY-MM-DD'")
