
# Modifying Global Scope
enemies = "Skeleton"# Global Scope  Variable and a function

def increase_enemies():
    global enemies
    enemies = "Zombie"
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")
