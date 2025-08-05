#Sets Data Structures
# sterilized equipment sets

sterile_lab_equipment = {"Microscope", "Centrifu", "Pipettes"}
sterile_er_equipment = {"Stethoscope", "Defibrillator", "Sutures"}

#contaminated items
contaminated = {"Defibrillator", "Sutures", "Scalpel"}
print("Sterile ER Equipment:", sterile_er_equipment)
print("Sterile Lab Equipment:", sterile_lab_equipment)

#Concantinating/ combining
all_sterile = sterile_lab_equipment | sterile_er_equipment
print("All sterile Equipment:", all_sterile)
print("All contaminated items:", contaminated)