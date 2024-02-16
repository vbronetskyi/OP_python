"""Chalenge pronlem 5"""
def expected_farm_increase(k, m, j):
    """expected_farm_increase"""
    # Define the probabilities of getting each number on a 12-sided die.
    red_die_probabilities = [1/12] * 6 + [1/12] * 6  # Red die has 6 rabbits and 1 fox.
    blue_die_probabilities = [1/12] * 3 + [1/12] * 9  # Blue die has 3 sheep and 9 other animals.

    # Initialize variables to store the expected values.
    expected_rabbit_increase = 0
    expected_sheep_increase = 0
    expected_dog_increase = 0

    # Calculate the expected increase in rabbits and sheep.
    for red_roll in range(1, 13):
        for blue_roll in range(1, 13):
            rabbit_increase = (k + red_roll) // 2  # Expected rabbit increase on this roll.
            sheep_increase = (m + blue_roll) // 2  # Expected sheep increase on this roll.

            expected_rabbit_increase += red_die_probabilities[red_roll - 1] * \
                                       blue_die_probabilities[blue_roll - 1] * \
                                       rabbit_increase
            expected_sheep_increase += red_die_probabilities[red_roll - 1] * \
                                      blue_die_probabilities[blue_roll - 1] * \
                                      sheep_increase

    # Calculate the expected increase in dogs (if applicable).
    if j == 1:
        for red_roll in range(1, 13):
            if red_roll == 1:  # Fox roll
                dog_increase = (k // 6)  # Expected dog increase on a fox roll.
                expected_dog_increase += red_die_probabilities[red_roll - 1] * dog_increase

    # Calculate the total expected farm increase.
    total_expected_increase = expected_rabbit_increase + expected_sheep_increase + expected_dog_increase

    return total_expected_increase

# Find the optimal strategy for both scenarios.
k_range = range(0, 101)  # Change the range according to your problem constraints.
m_range = range(0, 101)  # Change the range according to your problem constraints.

best_increase_no_dog = 0
best_increase_with_dog = 0
optimal_exchange_no_dog = None
optimal_exchange_with_dog = None

for k in k_range:
    for m in m_range:
        increase_no_dog = expected_farm_increase(k, m, 0)
        increase_with_dog = expected_farm_increase(k, m, 1)

        if increase_no_dog > best_increase_no_dog:
            best_increase_no_dog = increase_no_dog
            optimal_exchange_no_dog = (k, m)

        if increase_with_dog > best_increase_with_dog:
            best_increase_with_dog = increase_with_dog
            optimal_exchange_with_dog = (k, m)
