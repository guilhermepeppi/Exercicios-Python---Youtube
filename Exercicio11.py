# Considerar que para 2m² precisa de 1L de tinta para ser pintado

largura = float(input('Largura da parede: '))  # 2.5
altura = float(input('Altura da parede: '))  # 1.75

area = largura * altura
total_tinta = area / 2

print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area}m2.')
print(f'Para pintar essa parede, você precisará de {total_tinta}L de tinta')
