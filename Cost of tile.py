# Calculate the total cost of tile it would take to cover a floor plan of width and height,
# using a cost entered by the user.
print("App which calculate total cost of covering floor with tiles.\n")

tile_width = int(input("Enter a tile widht in centimeters: "))
tile_height = int(input("Enter a tile height in centimeters: "))
cost = int(input("Enter a cost of one tile: "))
floor = int(input("Enter how many square meters of floor you need to cover: "))

square_tile = tile_width * tile_height
floor_in_cm2 = floor * 10000
amount_of_tiles = floor_in_cm2 / square_tile
total = amount_of_tiles * cost

print("\nTo cover a", floor, "square meters floor, you need to buy", amount_of_tiles, "tiles, which will cost you", total, ".")


input("\n\nEnter")