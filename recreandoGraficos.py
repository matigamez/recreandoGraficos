import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el dataset
df = sns.load_dataset('tips')

# Crear una figura y un eje
fig, ax = plt.subplots(figsize=(12, 6))

# Gráfico de dispersión con cuadrícula, leyenda, anotaciones y flechas
sns.scatterplot(data=df, x='total_bill', y='tip', hue='time', style='day', s=100, ax=ax)
ax.set_title('Relación entre Total Bill y Tip con Anotaciones y Flechas', fontsize=20)
ax.set_xlabel('Total Bill ($)', fontsize=15)
ax.set_ylabel('Tip ($)', fontsize=15)
ax.legend(loc='upper right', fontsize='large', shadow=True, title='Detalles')

# Añadir cuadrícula
ax.grid(True, which='both', linestyle='--', linewidth=0.7, color='gray')

# Añadir anotación
ax.annotate('Mayor tip en la cena', xy=(50, 10), xytext=(60, 15),
            arrowprops=dict(facecolor='black', shrink=0.05))

# Añadir flecha
ax.arrow(30, 3, 10, 5, head_width=0.8, head_length=1, fc='green', ec='green')

# Mostrar el gráfico
plt.show()
