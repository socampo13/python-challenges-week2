### 📂 **Challenge 6: File Handling**
##* Count the number of lines, words, and characters in a text file.
##* Expected function: `file_stats(filepath: str) -> dict[str, int]`.

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

## Test
if __name__ == "__main__":
    filepath = "C:/Users/Asus/Desktop/software-team-training-path/second_week/Challenges Simon Ocampo/challenge6.txt"
    try:
        print(file_stats(filepath))
    except Exception as e:
        print(e)