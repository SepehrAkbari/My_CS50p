def main():
    total_inserted = 0

    print("Amount due: 50")

    while total_inserted < 50:
        coin = int(input("Insert Coin: "))

        if coin in [25, 10, 5]:
            total_inserted += coin
            remaining_due = 50 - total_inserted
            print(f"Amount Due: {remaining_due}")
        else:
            print("Amount Due: 50")

    change = total_inserted - 50
    if change > 0:
        print(f"Change Owed: {change}")
    else:
        print("Change Owed: 0")

if __name__ == "__main__":
    main()
