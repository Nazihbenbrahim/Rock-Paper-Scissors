from RPS_game import play, quincy, abbey, kris, mrugby
from RPS import player

# Test against each bot
print("Testing against Quincy...")
play(player, quincy, 1000)

print("\nTesting against Abbey...")
play(player, abbey, 1000)

print("\nTesting against Kris...")
play(player, kris, 1000)

print("\nTesting against MrRugby...")
play(player, mrugby, 1000)


