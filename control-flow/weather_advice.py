request = input("What's the weather like today? (sunny/rainy/cold): ").lower()

if request == 'sunny':
    print("\nWear a t-shirt and sunglasses.")
elif request == 'rainy':
    print("\nDon't forget your umbrella and a raincoat.")
elif request == 'cold': 
    print("\nMake sure to wear a warm coat and a scarf.")
else:
    print("\nSorry, I don't have recommendations for this weather.")