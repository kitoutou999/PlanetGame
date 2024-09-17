import os
from PIL import Image, ImageEnhance

image_path = "Chevals.png"
num_rows = 1
num_cols = 2



image = Image.open(image_path)



# Créer un dossier pour la sortie
output_dir = os.path.splitext(image_path)[0] + f"_pieces_{num_rows}x{num_cols}"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Découper l'image en pièces
width, height = image.size
piece_width = int(width/num_cols)
piece_height = int(height/num_rows)

for i in range(num_rows):
    for j in range(num_cols):
        left = j*piece_width
        upper = i*piece_height
        right = left + piece_width
        lower = upper + piece_height
        piece = image.crop((left, upper, right, lower))

        # Appliquer le filtre de luminosité de 2%
        enhancer = ImageEnhance.Brightness(piece)
        piece = enhancer.enhance(1.02)

        # Enregistrer la pièce de l'image dans le dossier de sortie
        piece_path = os.path.join(output_dir, f"piece_{i}_{j}.png")
        piece.save(piece_path)
