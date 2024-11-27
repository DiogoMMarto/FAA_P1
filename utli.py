# Updated labels for the models
updated_labels = [
    "Ranjeet Jain",
    "Sayak Dasgupta",
    "Vítor Santos and Tiago Pereira (CNN)",
    "Vítor Santos and Tiago Pereira (KNN)"
]

# Create the updated bar plot
plt.figure(figsize=(10, 6))
plt.bar(updated_labels, accuracies)
plt.ylim(0, 100)
plt.xlabel("Researchers", fontsize=12)
plt.ylabel("Accuracy (%)", fontsize=12)
plt.title("Accuracy Comparison of Sign Language Classification Models", fontsize=14)
plt.xticks(rotation=15, fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()
