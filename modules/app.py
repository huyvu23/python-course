# options one
import converters

# options two
# from converters import lbs_to_kg, kg_to_lbs
def main():
    weight_lbs = 150
    weight_kg = 68.18

    # Convert pounds to kilograms
    converted_weight_kg = converters.lbs_to_kg(weight_lbs)
    print(f"{weight_lbs} lbs is equal to {converted_weight_kg:.2f} kg")

    # Convert kilograms to pounds
    converted_weight_lbs = converters.kg_to_lbs(weight_kg)
    print(f"{weight_kg} kg is equal to {converted_weight_lbs:.2f} lbs")

main()